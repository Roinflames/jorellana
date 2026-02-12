create extension if not exists pgcrypto;

create table if not exists app_users (
    id bigserial primary key,
    username text not null unique,
    password_hash text not null,
    role text not null check (role in ('admin', 'supervisor', 'operador')),
    full_name text not null,
    is_active boolean not null default true,
    created_at timestamptz not null default now()
);

create table if not exists flower_receptions (
    id bigserial primary key,
    lot_code text not null unique,
    supplier text not null,
    strain text not null,
    weight_grams numeric(12,2) not null check (weight_grams > 0),
    received_at timestamptz not null,
    notes text,
    created_at timestamptz not null default now(),
    created_by bigint not null references app_users(id)
);

create table if not exists extract_batches (
    id bigserial primary key,
    lot_code text not null unique,
    source_lot_code text not null,
    method text not null,
    status text not null,
    input_grams numeric(12,2) not null check (input_grams > 0),
    output_grams numeric(12,2) not null check (output_grams > 0),
    yield_pct numeric(6,2) not null check (yield_pct >= 0 and yield_pct <= 100),
    started_at timestamptz not null,
    finished_at timestamptz,
    notes text,
    created_at timestamptz not null default now(),
    created_by bigint not null references app_users(id)
);

create table if not exists supplies (
    id bigserial primary key,
    code text not null unique,
    name text not null,
    unit text not null,
    current_stock numeric(12,2) not null default 0 check (current_stock >= 0),
    minimum_stock numeric(12,2) not null default 0 check (minimum_stock >= 0),
    is_active boolean not null default true,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists supply_movements (
    id bigserial primary key,
    supply_id bigint not null references supplies(id),
    movement_type text not null check (movement_type in ('in', 'out', 'adjust')),
    quantity numeric(12,2) not null check (quantity > 0),
    delta numeric(12,2) not null,
    reason text not null,
    created_at timestamptz not null default now(),
    created_by bigint not null references app_users(id)
);

create index if not exists idx_flower_receptions_received_at on flower_receptions(received_at desc);
create index if not exists idx_extract_batches_started_at on extract_batches(started_at desc);
create index if not exists idx_supply_movements_supply_id on supply_movements(supply_id, created_at desc);

