import os
from datetime import UTC, datetime
from typing import Any, Callable

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from .auth import create_access_token, decode_access_token, hash_password, verify_password
from .db import apply_migrations, execute, fetch_all, fetch_one
from .schemas import (
    ExtractBatchCreate,
    FlowerReceptionCreate,
    LoginRequest,
    SupplyCreate,
    SupplyMovementCreate,
    TokenResponse,
)


app = FastAPI(title="BCP MVP API", version="0.2.0")


def _cors_origins() -> list[str]:
    raw = os.getenv("CORS_ORIGINS", "*").strip()
    if raw == "*" or raw == "":
        return ["*"]
    return [item.strip() for item in raw.split(",") if item.strip()]


app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _ensure_seed_admin() -> None:
    admin_username = os.getenv("ADMIN_USERNAME", "admin").strip()
    admin_password = os.getenv("ADMIN_PASSWORD", "Admin123!").strip()
    existing = fetch_one("select id from app_users where username = %s;", (admin_username,))
    if existing:
        return
    execute(
        """
        insert into app_users (username, password_hash, role, full_name)
        values (%s, %s, 'admin', 'Administrador MVP');
        """,
        (admin_username, hash_password(admin_password)),
    )


@app.on_event("startup")
def startup() -> None:
    apply_migrations()
    _ensure_seed_admin()


def _unauthorized(detail: str = "Unauthorized") -> HTTPException:
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


def _get_current_user(authorization: str = Header(default="")) -> dict[str, Any]:
    if not authorization.startswith("Bearer "):
        raise _unauthorized("Missing bearer token")
    token = authorization.removeprefix("Bearer ").strip()
    payload = decode_access_token(token)
    user = fetch_one(
        """
        select id, username, role, full_name, is_active
        from app_users
        where id = %s;
        """,
        (payload["sub"],),
    )
    if not user or not user["is_active"]:
        raise _unauthorized("User is inactive or missing")
    return user


def _require_roles(*allowed_roles: str) -> Callable[[dict[str, Any]], dict[str, Any]]:
    def dependency(user: dict[str, Any] = Depends(_get_current_user)) -> dict[str, Any]:
        if allowed_roles and user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient role",
            )
        return user

    return dependency


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "api"}


@app.get("/db-check")
def db_check(user: dict[str, Any] = Depends(_require_roles("admin", "supervisor"))) -> dict[str, Any]:
    row = fetch_one("select now() as now_utc, current_database() as db_name;")
    return {"status": "ok", "database": row, "checked_by": user["username"]}


@app.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest) -> TokenResponse:
    user = fetch_one(
        """
        select id, username, password_hash, role, full_name, is_active
        from app_users
        where username = %s;
        """,
        (payload.username,),
    )
    if not user or not user["is_active"]:
        raise _unauthorized("Invalid credentials")
    if not verify_password(payload.password, user["password_hash"]):
        raise _unauthorized("Invalid credentials")

    token = create_access_token(sub=str(user["id"]), role=user["role"])
    return TokenResponse(
        access_token=token,
        user={
            "id": user["id"],
            "username": user["username"],
            "role": user["role"],
            "full_name": user["full_name"],
        },
    )


@app.get("/auth/me")
def me(user: dict[str, Any] = Depends(_get_current_user)) -> dict[str, Any]:
    return {"user": user}


@app.get("/flower-receptions")
def list_flower_receptions(
    limit: int = 100,
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    rows = fetch_all(
        """
        select id, lot_code, supplier, strain, weight_grams, received_at, notes, created_at, created_by
        from flower_receptions
        order by received_at desc
        limit %s;
        """,
        (max(1, min(limit, 500)),),
    )
    return {"items": rows, "count": len(rows), "requested_by": user["username"]}


@app.post("/flower-receptions")
def create_flower_reception(
    payload: FlowerReceptionCreate,
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    row = fetch_one(
        """
        insert into flower_receptions (lot_code, supplier, strain, weight_grams, received_at, notes, created_by)
        values (%s, %s, %s, %s, %s, %s, %s)
        returning id;
        """,
        (
            payload.lot_code.strip().upper(),
            payload.supplier.strip(),
            payload.strain.strip(),
            payload.weight_grams,
            payload.received_at,
            payload.notes,
            user["id"],
        ),
    )
    return {"status": "ok", "id": row["id"]}


@app.get("/extract-batches")
def list_extract_batches(
    limit: int = 100,
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    rows = fetch_all(
        """
        select id, lot_code, source_lot_code, method, status, input_grams, output_grams, yield_pct,
               started_at, finished_at, notes, created_at, created_by
        from extract_batches
        order by started_at desc
        limit %s;
        """,
        (max(1, min(limit, 500)),),
    )
    return {"items": rows, "count": len(rows), "requested_by": user["username"]}


@app.post("/extract-batches")
def create_extract_batch(
    payload: ExtractBatchCreate,
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    if payload.output_grams > payload.input_grams:
        raise HTTPException(status_code=400, detail="output_grams cannot exceed input_grams")
    yield_pct = (payload.output_grams / payload.input_grams) * 100
    row = fetch_one(
        """
        insert into extract_batches (
            lot_code, source_lot_code, method, status, input_grams, output_grams, yield_pct,
            started_at, finished_at, notes, created_by
        )
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        returning id;
        """,
        (
            payload.lot_code.strip().upper(),
            payload.source_lot_code.strip().upper(),
            payload.method.strip().upper(),
            payload.status.strip().upper(),
            payload.input_grams,
            payload.output_grams,
            round(yield_pct, 2),
            payload.started_at,
            payload.finished_at,
            payload.notes,
            user["id"],
        ),
    )
    return {"status": "ok", "id": row["id"]}


@app.get("/supplies")
def list_supplies(
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    rows = fetch_all(
        """
        select id, code, name, unit, current_stock, minimum_stock, is_active, updated_at
        from supplies
        where is_active = true
        order by name asc;
        """
    )
    return {"items": rows, "count": len(rows), "requested_by": user["username"]}


@app.post("/supplies")
def create_supply(
    payload: SupplyCreate,
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor")),
) -> dict[str, Any]:
    row = fetch_one(
        """
        insert into supplies (code, name, unit, current_stock, minimum_stock)
        values (%s, %s, %s, %s, %s)
        returning id;
        """,
        (
            payload.code.strip().upper(),
            payload.name.strip(),
            payload.unit.strip().lower(),
            payload.current_stock,
            payload.minimum_stock,
        ),
    )
    return {"status": "ok", "id": row["id"]}


@app.post("/supplies/{supply_id}/movements")
def create_supply_movement(
    supply_id: int,
    payload: SupplyMovementCreate,
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    supply = fetch_one(
        "select id, current_stock from supplies where id = %s and is_active = true;",
        (supply_id,),
    )
    if not supply:
        raise HTTPException(status_code=404, detail="Supply not found")

    current_stock = float(supply["current_stock"])
    if payload.movement_type == "in":
        new_stock = current_stock + payload.quantity
        delta = payload.quantity
    elif payload.movement_type == "out":
        if payload.quantity > current_stock:
            raise HTTPException(status_code=400, detail="Insufficient stock")
        new_stock = current_stock - payload.quantity
        delta = -payload.quantity
    else:
        new_stock = payload.quantity
        delta = payload.quantity - current_stock

    execute(
        """
        insert into supply_movements (supply_id, movement_type, quantity, delta, reason, created_by)
        values (%s, %s, %s, %s, %s, %s);
        """,
        (supply_id, payload.movement_type, payload.quantity, delta, payload.reason, user["id"]),
    )
    execute("update supplies set current_stock = %s, updated_at = now() where id = %s;", (new_stock, supply_id))
    return {"status": "ok", "new_stock": new_stock}


@app.get("/dashboard/summary")
def dashboard_summary(
    user: dict[str, Any] = Depends(_require_roles("admin", "supervisor", "operador")),
) -> dict[str, Any]:
    totals = fetch_one(
        """
        select
            (select count(*) from flower_receptions) as flower_receptions,
            (select coalesce(sum(weight_grams), 0) from flower_receptions) as flower_weight_total,
            (select count(*) from extract_batches) as extract_batches,
            (select count(*) from supplies where is_active = true) as supplies;
        """
    )

    low_stock = fetch_all(
        """
        select id, code, name, current_stock, minimum_stock
        from supplies
        where is_active = true and current_stock <= minimum_stock
        order by current_stock asc
        limit 20;
        """
    )

    recent_activity = fetch_all(
        """
        select 'flower_reception' as kind, id, lot_code as code, received_at as happened_at
        from flower_receptions
        union all
        select 'extract_batch' as kind, id, lot_code as code, started_at as happened_at
        from extract_batches
        order by happened_at desc
        limit 20;
        """
    )

    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "requested_by": user["username"],
        "totals": totals,
        "low_stock": low_stock,
        "recent_activity": recent_activity,
    }

