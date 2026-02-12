# MVP Setup (Neon + Docker + Cloudflare)

## Requisitos

- Docker + Docker Compose
- Proyecto Neon creado (PostgreSQL)
- Cuenta Cloudflare con Zero Trust

## 1) Variables de entorno

```bash
cp .env.example .env
```

Editar `.env`:

- `DATABASE_URL`: string de Neon con `sslmode=require`
- `CLOUDFLARE_TUNNEL_TOKEN`: token del tunnel (si vas a publicar)

## 2) Levantar entorno local

```bash
docker compose up -d --build
```

Validaciones:

- Web: `http://localhost:8080`
- API health: `http://localhost:8080/api/health`
- DB check (Neon): `http://localhost:8080/api/db-check`
- Modulo funcional MVP: `http://localhost:8080/mvp-recepcion.html`

Credenciales iniciales por defecto:

- usuario: `admin`
- password: `Admin123!`

Puedes cambiarlas desde `.env` con:

- `ADMIN_USERNAME`
- `ADMIN_PASSWORD`

## 3) Publicar hacia internet con Cloudflare

Ejecutar profile `public`:

```bash
docker compose --profile public up -d
```

El servicio `cloudflared` toma el token desde `.env` y conecta el tunnel hacia `web`.

URL sugerida para revisar desde internet:

- `https://erp.tu-dominio.cl/mvp-recepcion.html`

## 4) Notas operativas

- `web` sirve las maquetas de `modulos/` y redirige `/` a `Dashboard Principal`.
- `api` es base tecnica para iniciar migracion desde `localStorage` a DB real.
- La DB NO se expone por puertos: se consume directo en Neon mediante `DATABASE_URL`.
