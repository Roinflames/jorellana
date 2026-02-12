# OFERTA TÉCNICA

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

## 1. Descripción del Proyecto

### Sistema ERP BioCannaPharma - Desarrollo Productivo

Sistema de trazabilidad y control de línea productiva de extractos para laboratorio farmacéutico.

**Objetivo General:** Desarrollar un sistema ERP productivo para el seguimiento y trazabilidad de la línea productiva de extractos, con escaneo de códigos QR/Barcode mediante PDA industrial, cumpliendo normativas BPM, ISO 9001, D.S. 594, 148, 43 y 108.

### Contexto Operacional

| Aspecto | Detalle |
|---------|---------|
| **Ambiente** | Laboratorio con restricción de uso de teléfonos celulares |
| **Dispositivo principal** | PDA industrial con lector de códigos integrado |
| **Flujo de trabajo** | Escaneo de QR/Barcode previo a cada proceso productivo |
| **Elementos trazables** | Flores, insumos, reactivos, equipos, lotes de producción |

### Equipo de Desarrollo

- 1 Desarrollador Semi-Senior (arquitectura, integraciones, revisión de código)
- 1 Desarrollador Trainee (frontend, tareas mecánicas, testing)
- Asistencia de IA para generación de código y aceleración de desarrollo

---

## 2. Requerimientos Técnicos - Sistema PDA + Escaneo

### Dispositivo de Operación

| Característica | Especificación |
|----------------|----------------|
| **Modelo sugerido** | Zebra TC21/TC26, Honeywell CT40, Datalogic Memor |
| **Sistema operativo** | Android 10+ o Windows Mobile (según modelo) |
| **Lector integrado** | Códigos 1D (Barcode) y 2D (QR) |
| **Conectividad** | WiFi para sincronización con servidor central |

### Arquitectura del Sistema

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  PDA Industrial │────▶│   API REST      │────▶│  Base de Datos  │
│  (App Android)  │◀────│   (Backend)     │◀────│   PostgreSQL    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │
        │                       ▼
        │              ┌─────────────────┐
        │              │   Panel Web     │
        │              │  (Supervisión)  │
        └─────────────▶└─────────────────┘
```

### Componentes del Sistema

1. **Aplicación PDA (Android):** Interfaz optimizada para escaneo y registro rápido
2. **API REST:** Backend centralizado para procesamiento y persistencia
3. **Panel Web:** Supervisión, reportes y configuración (para PC de oficina)
4. **Generador de Códigos:** Impresión de etiquetas QR/Barcode

### Flujo de Trabajo con Escaneo

```
[Escanear elemento] → [Validar código] → [Mostrar info] → [Registrar acción] → [Siguiente paso]
```

### Códigos a Implementar

| Código | Elemento | Acciones |
|--------|----------|----------|
| `QR-MP-XXXX` | Materia Prima / Flores | Recepción, almacenamiento, uso |
| `QR-INS-XXXX` | Insumos | Recepción, stock, consumo |
| `QR-REA-XXXX` | Reactivos químicos | Trazabilidad, uso, vencimiento |
| `QR-EQU-XXXX` | Equipos | Identificación, mantenimiento, calibración |
| `QR-LOT-XXXX` | Lotes de producción | Seguimiento de proceso |
| `QR-RES-XXXX` | Residuos | Generación, almacenamiento, retiro |

---

## 3. Alcance Funcional - Módulos

### FASE 1 - Infraestructura Base + Módulos Core

#### Sprint 1.1 — Infraestructura y Arquitectura Base

**Objetivo:** Configurar entorno, base de datos, autenticación y aplicación base para PDA.

**1. Configuración del entorno y arquitectura**
- Setup de repositorio, estructura de proyecto, CI/CD básico
- Diseño e implementación de base de datos PostgreSQL
- Sistema de autenticación y gestión de usuarios/roles
- API REST base con documentación (Swagger/OpenAPI)

**2. Aplicación PDA Base + Dashboard**
- App Android base con integración de lector de códigos
- Módulo de login y sincronización con servidor
- Dashboard web: métricas y estadísticas consolidadas
- Sistema de generación e impresión de etiquetas QR/Barcode

#### Sprint 1.2 — Módulos de Inventario con Escaneo (Core del negocio)

**Objetivo:** Implementar módulos críticos con flujo de escaneo QR/Barcode integrado.

**3. Recepción de Flores / Materia Prima (Módulo 3)**
- Backend: CRUD, trazabilidad, códigos de lote
- PDA: Pantalla de escaneo para recepción y registro
- Web: Panel de consulta, tablas, búsqueda avanzada
- Generación de etiquetas QR para materia prima

**4. Control de Extractos / Línea Productiva (Módulo 2)**
- Backend: procesos RSO/BHO, fracciones, rendimientos
- PDA: Escaneo de inicio/fin de proceso, registro de lotes
- Web: Flujo de proceso, estados, trazabilidad visual
- Reportes de producción y rendimiento

**5. Gestión de Insumos (Módulo 4)**
- Backend: stock, movimientos, alertas de reposición
- PDA: Escaneo para consumo y ajustes de inventario
- Web: Inventario, kardex, proyecciones

---

### FASE 2 - Módulos de Adquisiciones y Laboratorio

#### Sprint 2.1 — Ciclo de Compras Completo

**Objetivo:** Implementar flujo completo de adquisiciones desde solicitud hasta recepción.

**6. Sistema de Solicitudes (Módulo 8)**
- Backend: workflow de aprobaciones, estados, notificaciones
- Frontend: formularios, seguimiento, historial

**7. Sistema de Compras (Módulo 6)**
- Backend: órdenes de compra, seguimiento, recepciones
- Frontend: gestión de OC, comparativas, reportes

**8. Gestión de Proveedores (Módulo 7)**
- Backend: registro, evaluación, documentación
- Frontend: ficha de proveedor, calificaciones

#### Sprint 2.2 — Módulos de Laboratorio con Escaneo

**Objetivo:** Control de reactivos y equipamiento con trazabilidad por escaneo.

**9. Reactivos Químicos (Módulo 5)**
- Backend: inventario, hojas de seguridad, vencimientos
- PDA: Escaneo para uso de reactivos, registro de consumo
- Web: Alertas, fichas técnicas, trazabilidad
- Integración con normativas de sustancias peligrosas

**10. Equipos y Mantenciones (Módulo 9)**
- Backend: inventario equipos, calibraciones, mantenciones
- PDA: Escaneo de equipo para registro de uso/mantención
- Web: Calendario, alertas, historial
- Gestión documental (manuales, certificados)

---

### FASE 3 - Módulos Operacionales y Compliance

#### Sprint 3.1 — Control Operacional

**Objetivo:** Módulos de operación diaria y registros de laboratorio.

**11. Control de Aseo e Higiene (Módulo 10)**
- Backend: áreas, registros, inventario productos limpieza
- Frontend: check-lists, dashboard sanitización
- Reportes para auditorías

**12. Bitácora de Laboratorio (Módulo 11)**
- Backend: registros cronológicos, firma digital
- Frontend: timeline, búsqueda, exportación

#### Sprint 3.2 — Gestión Ambiental con Escaneo y Cierre

**Objetivo:** Cumplimiento ambiental con trazabilidad y ajustes finales.

**13. Gestión de Residuos (Módulo 12)**
- Backend: clasificación RESPEL/no RESPEL, manifiestos
- PDA: Escaneo para registro de generación y retiro
- Web: Seguimiento, reportes D.S. 148
- Integración con empresas recolectoras

**14. Integraciones y Ajustes Finales**
- Notificaciones por correo/sistema
- Exportación de reportes (PDF, Excel)
- Pruebas de integración PDA + Web + API
- Documentación técnica y manual de usuario PDA

---

## 4. Stack Tecnológico

| Tecnología / Herramienta | Tipo | Comentario |
|--------------------------|------|------------|
| App PDA (Android nativo o PWA) | Código abierto | React Native, Flutter o PWA. Optimizada para lectores de códigos industriales. |
| PDA Industrial | Hardware cliente | Zebra, Honeywell, Datalogic u otro. **COSTO NO INCLUIDO** |
| Backend (Python/Django o Node.js) | Código abierto | Gratuito. Costos asociados solo al desarrollo e infraestructura. |
| Panel Web (React o Vue.js) | Código abierto | Gratuito. Solo costos de desarrollo e integración con backend. |
| Base de datos (PostgreSQL) | Código abierto | Sin costo de licencia. Solo costos de hosting/infraestructura. |
| Servidor / Infraestructura (AWS, GCP, Azure o VPS) | Propietario | Pago según uso de CPU/RAM/almacenamiento. Escalable según volumen de usuarios. |
| Autenticación (JWT, OAuth2) | Código abierto | Sin costo de licencia. Implementación segura con tokens y sesiones. |
| Generación de códigos QR/Barras | Código abierto | Librerías gratuitas para trazabilidad de lotes y productos. |
| Impresora de etiquetas | Hardware cliente | Zebra, Brother, Dymo u otra compatible. **COSTO NO INCLUIDO** |
| Exportación (PDF, Excel) | Código abierto | ReportLab, WeasyPrint, OpenPyXL para generación de reportes. |
| Notificaciones (Email) | Mixto | SMTP gratuito (limitado) o servicios pagos (SendGrid, Amazon SES). |
| Certificados SSL/TLS | Mixto | Let's Encrypt gratuito o certificados comerciales según requerimiento. |
| Asistencia IA (Claude/GPT) | Suscripción | Herramienta de desarrollo incluida. Acelera codificación y documentación. |
| Backup y recuperación | Incluido | Configuración de respaldos automáticos en la infraestructura seleccionada. |

---

## 5. Entregables por Fase

| Fase | Entregables | Resultado |
|------|-------------|-----------|
| **Fase 1** | App PDA funcional + Dashboard web + Módulos de inventario y producción | Cliente puede comenzar a operar con escaneo de MP, insumos y extractos |
| **Fase 2** | Módulos de compras + laboratorio integrados | Sistema completo de adquisiciones y control de reactivos/equipos |
| **Fase 3** | Módulos ambientales + QA final + Documentación | Sistema completo en producción con soporte |

---

## 6. Hardware Requerido (No incluido en cotización)

> **Nota:** El siguiente hardware debe ser adquirido por el cliente.

| Equipo | Modelo sugerido | Precio referencial |
|--------|-----------------|-------------------|
| PDA Industrial | Zebra TC21/TC26, Honeywell CT40 | ~$400-800 USD c/u |
| Impresora de etiquetas | Zebra ZD220/ZD420 | ~$200-400 USD |
| Etiquetas | Térmicas/sintéticas para códigos QR/Barcode | Variable |

---

## 7. Requerimientos de Infraestructura del Cliente

1. Conectividad WiFi en las instalaciones para sincronización de PDAs
2. Al menos 2 PDAs para pruebas durante desarrollo
3. Impresora de etiquetas compatible con ZPL o similar
4. PC con navegador moderno para Panel Web de supervisión

---

## 8. Cumplimiento Normativo

El sistema está diseñado para cumplir con:

- **BPM** - Buenas Prácticas de Manufactura
- **ISO 9001** - Sistema de Gestión de Calidad
- **D.S. 594** - Condiciones Sanitarias y Ambientales
- **D.S. 148** - Manejo de Residuos Peligrosos
- **D.S. 43** - Sustancias Peligrosas
- **D.S. 108** - Reglamento Cannabis

---

*Documento confidencial - Comunidad Virtual*
