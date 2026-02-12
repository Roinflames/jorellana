import os
from pathlib import Path
from typing import Any

from psycopg import connect
from psycopg.rows import dict_row


def get_database_url() -> str:
    db_url = os.getenv("DATABASE_URL", "").strip()
    if not db_url:
        raise RuntimeError("DATABASE_URL is not configured")
    return db_url


def get_conn():
    return connect(get_database_url(), row_factory=dict_row)


def apply_migrations() -> None:
    migrations_dir = Path("/app/db/migrations")
    if not migrations_dir.exists():
        return

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                create table if not exists schema_migrations (
                    id serial primary key,
                    filename text not null unique,
                    applied_at timestamptz not null default now()
                );
                """
            )
            conn.commit()

            applied = set()
            cur.execute("select filename from schema_migrations;")
            for row in cur.fetchall():
                applied.add(row["filename"])

        migration_files = sorted(migrations_dir.glob("*.sql"))
        for migration in migration_files:
            if migration.name in applied:
                continue
            sql = migration.read_text(encoding="utf-8")
            with conn.cursor() as cur:
                cur.execute(sql)
                cur.execute(
                    "insert into schema_migrations (filename) values (%s);",
                    (migration.name,),
                )
            conn.commit()


def fetch_one(query: str, params: tuple[Any, ...] = ()) -> dict[str, Any] | None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchone()


def fetch_all(query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return list(cur.fetchall())


def execute(query: str, params: tuple[Any, ...] = ()) -> None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
        conn.commit()

