# Hallazgos y Matriz de Permisos

## Modulo: Gestion-Residuos

### Matriz por rol
| Accion | Generador | Recolector | Administrador |
|---|---|---|---|
| Ver dashboard | Si | Si | Si |
| Registrar residuo (Generar Residuo) | Si | No | Si |
| Asignar almacenamiento | Si | No | Si |
| Registrar disposicion final | No | Si | Si |
| Ver trazabilidad/listado | Si | Si | Si |
| Exportar / Importar JSON | Si | Si | Si |
| Cargar demo / limpiar datos | Si | Si | Si |

### Limitaciones actuales
- Persistencia local (`localStorage`), sin backend compartido.
- Permisos aplicados en frontend (no hay enforcement server-side).
- Sin sincronizacion multiusuario en tiempo real.
- Integraciones entre modulos dependen de claves locales y pueden desalinearse.

## Hallazgos transversales
- Varios modulos usaban claves `localStorage` distintas a las del dashboard principal.
- Se agregaron fallbacks en dashboard para compatibilidad legacy.
- Se estandarizaron rutas sin espacios para evitar `404` en hosting estatico.
- Se implemento login unificado (`login.html`) y guard global por sesion.

## Pendientes
- [ ] Definir contrato unico de claves de datos por modulo.
- [ ] Migrar modulos clave desde `localStorage` a API/DB (persistencia real).
- [ ] Endurecer permisos en backend (roles server-side).
- [ ] Agregar smoke tests E2E por rol (generador/recolector/admin).
