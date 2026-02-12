# Plan MVP con Docker + Cloudflare

## 1) Diagnostico de lo que hay hoy

Estado actual revisado en `modulos/`:

- Hay maquetas HTML funcionales por modulo (dashboard, solicitudes, compras, reactivos, etc.).
- La logica de datos vive en `localStorage` del navegador.
- No existe backend API, base de datos, autenticacion central ni control de roles.
- No hay `Dockerfile`, `docker-compose.yml`, `nginx`, CI/CD ni entorno de despliegue.
- No existe una navegacion unificada tipo app (menu principal + rutas + sesion compartida).

Conclusión: hoy hay un **prototipo de interfaz**; aun no hay un **MVP desplegable multiusuario**.

## 2) Alcance MVP recomendado (recorte pragmatico)

Para salir rapido con valor real, el MVP debe cubrir solo lo critico:

- Login + roles basicos (`admin`, `operador`, `supervisor`).
- 3 modulos core:
  - Recepcion de Flores
  - Control de Extractos
  - Insumos
- Dashboard minimo (KPIs basicos).
- Trazabilidad de lotes y movimientos.
- API documentada (OpenAPI) y persistencia en PostgreSQL.
- Despliegue con Docker Compose.
- Publicacion externa segura via Cloudflare Tunnel.

Todo lo demas (compras completas, proveedores avanzados, residuos full compliance, etc.) queda para post-MVP.

## 3) Brechas para pasar de maqueta a MVP

### Producto
- Definir modelo de datos canonical (lotes, movimientos, usuarios, turnos, estados).
- Unificar codigos y nomenclaturas (`QR-MP-*`, `QR-LOT-*`, etc.).
- Definir flujo minimo por modulo y reglas de validacion.

### Ingenieria
- Separar frontend de logica mock.
- Implementar backend REST.
- Persistir en PostgreSQL (migraciones).
- Reemplazar `localStorage` por API.
- Agregar autenticacion y autorizacion.

### Operacion
- Contenerizar servicios.
- Gestion de secretos por `.env`.
- Healthchecks, logs y backups.
- Exposicion por dominio con Cloudflare.

## 4) Arquitectura Docker objetivo (MVP)

Servicios en `docker-compose`:

- `web`: frontend (React/Vite o Next exportado) servido por Nginx.
- `api`: backend (Node/Nest o Python/FastAPI).
- `db`: PostgreSQL 16.
- `adminer` o `pgadmin` (solo entorno interno).
- `cloudflared`: tunel saliente a Cloudflare.

Red:

- Solo `web` expuesto localmente en `:8080`.
- `api` y `db` sin exposicion publica directa.
- `cloudflared` enruta `https://tu-dominio` -> `web:8080`.

## 5) Estructura base sugerida del repo

```txt
/
  docker-compose.yml
  .env.example
  infra/
    nginx/
      default.conf
    cloudflared/
      config.yml
  apps/
    web/
    api/
  db/
    migrations/
    seeds/
  docs/
    api-openapi.yaml
    runbook-deploy.md
```

## 6) Plan por etapas (3 semanas realistas)

## Semana 1: Fundaciones tecnicas

- Crear skeleton `apps/web` y `apps/api`.
- Levantar `docker-compose` con `web`, `api`, `db`.
- Definir esquema inicial DB (usuarios, lotes, movimientos, inventario).
- Implementar autenticacion JWT + refresh.
- Migrar 1 modulo de maqueta a frontend real (Recepcion).

Entregable:
- `docker compose up` levanta stack funcional local.
- Login operativo + CRUD base recepcion.

## Semana 2: Core operacional MVP

- Implementar modulo Control de Extractos (API + UI).
- Implementar modulo Insumos (API + UI).
- Dashboard basico con agregaciones reales.
- Auditoria minima (`created_by`, `updated_at`, eventos clave).
- Tests minimos: smoke + integracion API critica.

Entregable:
- Flujo end-to-end de trazabilidad en 3 modulos core.

## Semana 3: Exposicion externa + hardening minimo

- Configurar `cloudflared` en compose.
- Crear Tunnel en Cloudflare Zero Trust.
- Conectar dominio/subdominio (`erp.tu-dominio.cl`) al tunnel.
- Cerrar accesos directos no necesarios.
- Backup DB diario (script + volumen).
- Runbook operativo + checklist de soporte.

Entregable:
- MVP accesible externamente por HTTPS via Cloudflare.

## 7) Checklist Docker minimo

- `docker-compose.yml` versionado.
- `Dockerfile` por app (`web`, `api`).
- `.env.example` sin secretos reales.
- Volumen persistente para Postgres.
- `healthcheck` en `api` y `db`.
- `depends_on` con condicion de salud.
- Comando de migraciones al iniciar `api`.

## 8) Checklist Cloudflare minimo

- Cuenta Cloudflare + dominio activo.
- Zero Trust habilitado.
- Tunnel creado (token o credencial JSON).
- DNS CNAME del subdominio hacia tunnel.
- Reglas Access (ideal: email allowlist o OTP).
- TLS end-to-end (Cloudflare edge + origen en tunnel).

## 9) Riesgos y mitigacion

- Riesgo: arrastrar todos los modulos al MVP.
  - Mitigacion: congelar alcance a 3 modulos core.
- Riesgo: deuda por migrar logica desde HTML monolitico.
  - Mitigacion: reimplementar flujos, no "copiar/pegar" JS legacy.
- Riesgo: datos sensibles expuestos por mala config.
  - Mitigacion: sin puertos de DB publicos + Access policies en Cloudflare.
- Riesgo: falta de pruebas en campo PDA.
  - Mitigacion: prueba temprana en 1 dispositivo real desde semana 2.

## 10) Definicion de "MVP listo"

Se considera listo cuando:

- 3 perfiles pueden iniciar sesion y operar segun rol.
- 3 modulos core funcionan contra DB real.
- Se puede seguir un lote desde recepcion hasta movimiento de extracto.
- Hay dashboard minimo de estado.
- El sistema corre con `docker compose up -d`.
- Se accede externamente por dominio Cloudflare con HTTPS.
- Existe runbook de operacion y backup basico.

## 11) Proximo paso recomendado inmediato

1. Acordar alcance congelado del MVP (3 modulos core).
2. Elegir stack de backend (`FastAPI` o `NestJS`) y frontend (`React + Vite`).
3. Crear en este repo el bootstrap Docker inicial (compose + nginx + api + db + cloudflared).

