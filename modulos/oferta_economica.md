# OFERTA ECONÓMICA

**COMUNIDAD VIRTUAL**
**DOCUMENTO CONFIDENCIAL**

---

| Campo | Valor |
|-------|-------|
| **Fecha de emisión** | 23/01/2026 |
| **Código de cotización** | 01-JO-001-ERP |
| **Cliente** | BioCannaPharma (BCP) Chile |
| **Proyecto** | Sistema de Gestión Integrado ERP - Versión Productiva |

---

## 1. Resumen Ejecutivo

**Valor UF al 23/01/2026:** $38.500,00 *(valor referencial, ajustar según UF del día)*

| FASE | SPRINTS | HORAS | MONTO ESTIMADO | DURACIÓN |
|------|---------|-------|----------------|----------|
| Fase 1 | Sprint 1.1 + 1.2 | 105 HH | $4.042.500 | 4 semanas |
| Fase 2 | Sprint 2.1 + 2.2 | 72 HH | $2.772.000 | 3 semanas |
| Fase 3 | Sprint 3.1 + 3.2 | 65 HH | $2.502.500 | 2.5 semanas |
| **TOTAL** | | **242 HH** | **$9.317.000** | **9.5 semanas** |

---

## 2. Detalle de Horas por Sprint

### FASE 1 - Infraestructura Base + Módulos Core

#### Sprint 1.1 — Infraestructura y Arquitectura Base (46 HH)

| Actividad | HH |
|-----------|---:|
| Setup de repositorio, estructura de proyecto, CI/CD básico | 4 |
| Diseño e implementación de base de datos PostgreSQL | 6 |
| Sistema de autenticación y gestión de usuarios/roles | 8 |
| API REST base con documentación (Swagger/OpenAPI) | 5 |
| App Android base con integración de lector de códigos | 8 |
| Módulo de login y sincronización con servidor | 4 |
| Dashboard web: métricas y estadísticas consolidadas | 6 |
| Sistema de generación e impresión de etiquetas QR/Barcode | 5 |
| **Total Sprint 1.1** | **46** |

#### Sprint 1.2 — Módulos de Inventario con Escaneo (59 HH)

| Actividad | HH |
|-----------|---:|
| **Recepción de Flores / Materia Prima** | |
| Backend: CRUD, trazabilidad, códigos de lote | 7 |
| PDA: Pantalla de escaneo para recepción y registro | 6 |
| Web: Panel de consulta, tablas, búsqueda avanzada | 4 |
| Generación de etiquetas QR para materia prima | 3 |
| **Control de Extractos / Línea Productiva** | |
| Backend: procesos RSO/BHO, fracciones, rendimientos | 8 |
| PDA: Escaneo de inicio/fin de proceso, registro de lotes | 7 |
| Web: Flujo de proceso, estados, trazabilidad visual | 5 |
| Reportes de producción y rendimiento | 4 |
| **Gestión de Insumos** | |
| Backend: stock, movimientos, alertas de reposición | 6 |
| PDA: Escaneo para consumo y ajustes de inventario | 5 |
| Web: Inventario, kardex, proyecciones | 4 |
| **Total Sprint 1.2** | **59** |

**Total Fase 1: 105 HH = $4.042.500**

---

### FASE 2 - Módulos de Adquisiciones y Laboratorio

#### Sprint 2.1 — Ciclo de Compras Completo (33 HH)

| Actividad | HH |
|-----------|---:|
| **Sistema de Solicitudes** | |
| Backend: workflow de aprobaciones, estados, notificaciones | 7 |
| Frontend: formularios, seguimiento, historial | 5 |
| **Sistema de Compras** | |
| Backend: órdenes de compra, seguimiento, recepciones | 7 |
| Frontend: gestión de OC, comparativas, reportes | 5 |
| **Gestión de Proveedores** | |
| Backend: registro, evaluación, documentación | 5 |
| Frontend: ficha de proveedor, calificaciones | 4 |
| **Total Sprint 2.1** | **33** |

#### Sprint 2.2 — Módulos de Laboratorio con Escaneo (39 HH)

| Actividad | HH |
|-----------|---:|
| **Reactivos Químicos** | |
| Backend: inventario, hojas de seguridad, vencimientos | 6 |
| PDA: Escaneo para uso de reactivos, registro de consumo | 5 |
| Web: Alertas, fichas técnicas, trazabilidad | 4 |
| Integración con normativas de sustancias peligrosas | 3 |
| **Equipos y Mantenciones** | |
| Backend: inventario equipos, calibraciones, mantenciones | 7 |
| PDA: Escaneo de equipo para registro de uso/mantención | 5 |
| Web: Calendario, alertas, historial | 5 |
| Gestión documental (manuales, certificados) | 4 |
| **Total Sprint 2.2** | **39** |

**Total Fase 2: 72 HH = $2.772.000**

---

### FASE 3 - Módulos Operacionales y Compliance

#### Sprint 3.1 — Control Operacional (23 HH)

| Actividad | HH |
|-----------|---:|
| **Control de Aseo e Higiene** | |
| Backend: áreas, registros, inventario productos limpieza | 6 |
| Frontend: check-lists, dashboard sanitización | 5 |
| Reportes para auditorías | 3 |
| **Bitácora de Laboratorio** | |
| Backend: registros cronológicos, firma digital | 5 |
| Frontend: timeline, búsqueda, exportación | 4 |
| **Total Sprint 3.1** | **23** |

#### Sprint 3.2 — Gestión Ambiental con Escaneo y Cierre (42 HH)

| Actividad | HH |
|-----------|---:|
| **Gestión de Residuos** | |
| Backend: clasificación RESPEL/no RESPEL, manifiestos | 7 |
| PDA: Escaneo para registro de generación y retiro | 5 |
| Web: Seguimiento, reportes D.S. 148 | 5 |
| Integración con empresas recolectoras | 3 |
| **Integraciones y Ajustes Finales** | |
| Notificaciones por correo/sistema | 4 |
| Exportación de reportes (PDF, Excel) | 5 |
| Pruebas de integración PDA + Web + API | 8 |
| Documentación técnica y manual de usuario PDA | 5 |
| **Total Sprint 3.2** | **42** |

**Total Fase 3: 65 HH = $2.502.500**

---

## 3. Cronograma Estimado

| Hito | Fecha estimada |
|------|----------------|
| Fecha de inicio | Por definir |
| Fecha QA Fase 1 | Inicio + 4 semanas |
| Fecha QA Fase 2 | Inicio + 7 semanas |
| Fecha PROD Final | Inicio + 9.5 semanas |

---

## 4. Distribución del Equipo

| Rol | Dedicación | Responsabilidades |
|-----|------------|-------------------|
| **Semi-Senior** | ~60% del proyecto | Arquitectura, BD, APIs, App PDA, integraciones, code review, deploy |
| **Trainee** | ~40% del proyecto | Panel web, formularios, tablas, testing, documentación básica |
| **IA (Claude/GPT)** | Transversal | Generación de código boilerplate, conversión de maquetas, modelos, documentación, debugging |

---

## 5. Términos y Condiciones

### Soporte y Garantía

- **30 días de soporte gratuito + QA** incluidos en todas las compras.
- Hora adicional de soporte: **1.0 UF/hora** por profesional asistidor.

### Condiciones de Pago

| Concepto | Detalle |
|----------|---------|
| **Descuento al contado** | 5% de descuento |
| **Abono inicial** | 50% mediante transferencia electrónica o Webpay (máx. 3 días hábiles) |
| **Saldo** | Contra entrega del producto final |

### Variabilidad

El cronograma puede aumentar o disminuir en un **±10%** en el cálculo estimativo por la variabilidad de los costos de implementación, retrasos técnicos, de comunicación u otro.

### Confidencialidad

Cualquier difusión de este documento a otra entidad que no sea **BioCannaPharma** está estrictamente prohibida conforme a:
- Ley 19.039 de Propiedad Industrial
- Código Civil de Chile

---

## 6. Costos No Incluidos (Responsabilidad del Cliente)

### Hardware

| Equipo | Precio referencial |
|--------|-------------------|
| PDA Industrial (Zebra TC21/TC26, Honeywell CT40) | ~$400-800 USD c/u |
| Impresora de etiquetas (Zebra ZD220/ZD420) | ~$200-400 USD |
| Etiquetas térmicas/sintéticas | Variable |

### Infraestructura (mensual)

| Servicio | Precio referencial |
|----------|-------------------|
| Servidor cloud (AWS/GCP/Azure) | ~$50-150 USD/mes |
| Dominio + SSL | ~$50-100 USD/año |
| Servicio de email (SendGrid/SES) | ~$0-20 USD/mes |

---

## 7. Notas Importantes

1. Las horas de desarrollo corresponden a **horas profesionales estimadas** por fase, ejecutadas de forma no continua, distribuidas según avance de hitos.

2. **No constituyen dedicación exclusiva** ni ejecución en tiempo corrido, sino una bolsa de horas asociada al cumplimiento de entregables.

3. La estimación considera el **uso de herramientas de IA** para acelerar tareas repetitivas como generación de CRUD y conversión de maquetas.

4. El sistema requiere **conectividad WiFi** en las instalaciones para que las PDA puedan sincronizar con el servidor central.

5. Se recomienda al cliente adquirir **al menos 2 PDAs** para pruebas durante el desarrollo y validación de flujos de trabajo.

6. La impresora de etiquetas debe ser **compatible con ZPL** o similar para integración directa con el sistema.

---

## 8. Firmas

| | |
|---|---|
| **Firma Representante Legal** | **Firma Representante Legal** |
| BioCannaPharma | Comunidad Virtual |
| | |
| _________________________________ | _________________________________ |
| Nombre: | Nombre: |
| RUT: | RUT: |
| Fecha: | Fecha: |

---

*Documento confidencial - Comunidad Virtual*
