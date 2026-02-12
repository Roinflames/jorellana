# TODO Pendientes

## Despliegue y verificacion
- [ ] Re-crear `web` para aplicar los ultimos cambios de frontend:
  - [ ] `sudo docker compose up -d --force-recreate web`
- [ ] Validar breadcrumb visible en:
  - [ ] `/Dashboard%20Principal.html`
  - [ ] `/ControlExtractos.html`
  - [ ] `/Solicitudes.html`
- [ ] Validar navegacion en misma pestana desde Dashboard (sin `window.open`).

## ControlExtractos
- [ ] Confirmar login API funcional en header (`admin/Admin123!` o usuario valido).
- [ ] Validar bloqueo de acciones sin sesion:
  - [ ] Crear lote
  - [ ] Crear destilado
  - [ ] Registrar egresos
- [ ] Probar flujo completo:
  - [ ] Crear lote (ficha)
  - [ ] Crear destilado
  - [ ] Registrar egreso
- [ ] Revisar UX de selector "Lote de Extraccion" cuando no hay salidas en `bcp_salidas_v82`.
- [ ] Corregir validaciones internas con abortado real en loops (`forEach` -> `for...of`) para evitar guardados parciales.

## Integraciones entre modulos
- [ ] Verificar consistencia de llaves `localStorage` entre modulos (legacy vs nuevas).
- [ ] Confirmar integracion `Solicitudes` usando `bcpOrdenesProduccionV3_4` en todos los modulos.
- [ ] Definir estrategia de migracion de datos legacy.

## Seguridad
- [ ] Rotar token de Cloudflare (expuesto durante pruebas).
- [ ] Rotar credenciales/secretos expuestos en pruebas (`DATABASE_URL`, `JWT_SECRET`, usuarios default).
- [ ] Revisar politica de contrasenas por defecto para ambientes no-dev.

## CI/CD (GitHub Actions + Render)
- [ ] Agregar secrets en GitHub Actions:
  - [ ] `RENDER_API_DEPLOY_HOOK`
  - [ ] `RENDER_WEB_DEPLOY_HOOK`
- [ ] Ejecutar primer deploy manual (`workflow_dispatch`) y validar:
  - [ ] API deploy OK
  - [ ] Static deploy OK
- [ ] Definir rama de release (`main`) y politica de PR.

## Documentacion
- [ ] Revisar `api-explorer.html` y `Mapa Arquitectonico.html` con rutas finales de prod.
- [ ] Agregar seccion de troubleshooting en README (SELinux, breadcrumbs, cache hard refresh).

## Git
- [ ] Push del commit mas reciente si aun no esta remoto:
  - [ ] `6a0f9ce feat: add GitHub Actions CI/CD base and improve extract charts`
