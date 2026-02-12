# Cloudflare quickstart (para ver el modulo desde internet)

## 1) Crear Tunnel

En Cloudflare Zero Trust:

- Networks -> Tunnels -> Create a tunnel
- Copiar el token (`CLOUDFLARE_TUNNEL_TOKEN`)

## 2) Public hostname

Configurar un hostname, por ejemplo:

- `erp.tu-dominio.cl` -> `http://web:80`

## 3) Variables locales

En `.env`:

```env
CLOUDFLARE_TUNNEL_TOKEN=tu_token
```

## 4) Levantar servicios

```bash
docker compose --profile public up -d --build
```

## 5) URL de prueba

- `https://erp.tu-dominio.cl/mvp-recepcion.html`

Login default si no lo cambiaste:

- `admin / Admin123!`

