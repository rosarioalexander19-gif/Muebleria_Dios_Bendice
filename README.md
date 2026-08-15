# Youmelky Alexander Rosario – Base de Datos y Conexión

## Proyecto Final de Programación II

### Sistema de Gestión de Ventas – Mueblería Dios Bendice

---

## 1. Responsabilidad

Mi responsabilidad dentro del proyecto corresponde a la **Base de Datos y Conexión**.

Las tareas realizadas fueron:

- Creación de la base de datos `muebleria_dios_bendice`.
- Creación de las tablas y sus relaciones.
- Definición de claves primarias y foráneas.
- Uso de campos `AUTO_INCREMENT`.
- Creación y configuración de triggers para el control del inventario.
- Preparación del archivo `muebleria_dios_bendice.sql`.
- Desarrollo de `conexion.py` para conectar Python con MySQL.
- Pruebas de conexión a la base de datos.
- Documentación de la configuración necesaria para ejecutar la base de datos y la conexión.

---

## 2. Tecnologías utilizadas

- **Python**
- **Tkinter**
- **MySQL**
- **mysql-connector-python**
- **Git**
- **GitHub**
- **Visual Studio Code**

---

## 3. Base de datos

El proyecto utiliza la siguiente base de datos:

```sql
muebleria_dios_bendice
```

El archivo que contiene la estructura y los datos necesarios para restaurar la base de datos es:

```text
muebleria_dios_bendice.sql
```

### Tablas principales

La base de datos contiene las siguientes tablas:

- `clientes`
- `productos`
- `usuarios`
- `facturas`
- `detalle_factura`
- `cuentas_por_cobrar`

Estas tablas permiten gestionar clientes, productos, usuarios, ventas, detalles de las ventas y las cuentas pendientes generadas por las ventas a crédito.

---

## 4. Relaciones de la base de datos

La estructura general de las relaciones es:

```text
clientes
   │
   └── facturas
          │
          ├── detalle_factura
          │        │
          │        └── productos
          │
          └── cuentas_por_cobrar

usuarios
   │
   └── facturas
```

### Descripción

- Un **cliente** puede tener varias facturas.
- Un **usuario** puede registrar varias facturas.
- Una **factura** puede contener varios detalles de productos.
- Cada detalle de factura está relacionado con un producto.
- Una factura a crédito puede generar una cuenta por cobrar.

---

## 5. Claves primarias, foráneas y AUTO_INCREMENT

Las tablas utilizan claves primarias para identificar cada registro de manera única.

También se utilizan claves foráneas para mantener la integridad referencial entre las tablas.

Los identificadores principales utilizan `AUTO_INCREMENT`, permitiendo que MySQL genere automáticamente los valores de los IDs al insertar nuevos registros.

---

## 6. Triggers

Una de las responsabilidades principales de mi parte fue implementar los triggers relacionados con el inventario.

### Trigger `validar_stock`

Este trigger se ejecuta **antes de insertar** un registro en `detalle_factura`.

Su función es verificar que el producto tenga suficiente stock para realizar la venta.

Si la cantidad solicitada es mayor que el inventario disponible, la operación se detiene y MySQL genera un error indicando que el stock es insuficiente.

Esto evita registrar ventas de productos que no están disponibles.

### Trigger `actualizar_stock`

Este trigger se ejecuta **después de insertar** un registro en `detalle_factura`.

Su función es disminuir automáticamente el stock del producto según la cantidad vendida.

De esta forma, el inventario se actualiza automáticamente después de una venta válida.

### Flujo de los triggers

```text
Registrar producto en detalle_factura
              │
              ▼
       validar_stock
              │
       ┌──────┴──────┐
       │             │
    Suficiente     Insuficiente
       │             │
       ▼             ▼
 Registrar venta    Rechazar
       │
       ▼
 actualizar_stock
       │
       ▼
 Reducir inventario
```

---

## 7. Conexión Python + MySQL

La conexión entre la aplicación y MySQL se encuentra centralizada en:

```text
conexion.py
```

Se utiliza `mysql.connector` para establecer la comunicación con la base de datos.

La estructura de la conexión es similar a:

```python
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="TU_CONTRASEÑA",
        database="muebleria_dios_bendice"
    )
```

> **Importante:** `TU_CONTRASEÑA` representa la contraseña local de MySQL. La contraseña real no debe publicarse en GitHub.

Cada integrante debe configurar sus propias credenciales localmente.

---

## 8. Instalación del conector de MySQL

Para conectar Python con MySQL se debe instalar el paquete:

```bash
pip install mysql-connector-python
```

La conexión debe probarse antes de ejecutar los módulos que dependen de la base de datos.

---

## 9. Restauración de la base de datos

### Paso 1: Iniciar MySQL

Abrir MySQL Server, MySQL Workbench o el monitor de MySQL.

### Paso 2: Ejecutar el archivo SQL

Desde el monitor de MySQL se puede utilizar:

```sql
SOURCE C:/ruta/al/proyecto/muebleria_dios_bendice.sql;
```

La ruta debe sustituirse por la ubicación real del archivo en la computadora.

También se puede abrir el archivo desde MySQL Workbench y ejecutar su contenido.

### Paso 3: Verificar la base de datos

```sql
SHOW DATABASES;
```

Debe aparecer:

```text
muebleria_dios_bendice
```

### Paso 4: Seleccionar la base de datos

```sql
USE muebleria_dios_bendice;
```

### Paso 5: Verificar las tablas

```sql
SHOW TABLES;
```

Deben aparecer:

```text
clientes
cuentas_por_cobrar
detalle_factura
facturas
productos
usuarios
```

---

## 10. Estructura relacionada con mi responsabilidad

Los archivos principales relacionados con mi trabajo son:

```text
muebleria_dios_bendice.sql
conexion.py
```

El proyecto completo además está organizado en capas:

```text
model/
repository/
service/
ui/
reports/
```

Esta organización permite separar los modelos de datos, el acceso a la base de datos, la lógica del sistema, la interfaz gráfica y los reportes.

---

## 11. Integración con el sistema de ventas

La base de datos fue diseñada para permitir que el sistema gestione:

- Clientes.
- Productos.
- Usuarios.
- Facturas.
- Detalles de facturas.
- Ventas al contado.
- Ventas a crédito.
- Cuentas por cobrar.
- Control de inventario.
- Reportes.

La información registrada desde la interfaz de Python es almacenada en MySQL mediante la conexión definida en `conexion.py`.

---

## 12. Ventas al contado y a crédito

La tabla `facturas` permite diferenciar el tipo de pago de la operación.

### Contado

Una venta al contado se registra utilizando:

```text
tipo_pago = Contado
```

### Crédito

Una venta a crédito se registra utilizando:

```text
tipo_pago = Credito
```

Las ventas a crédito se relacionan con `cuentas_por_cobrar` para llevar el control de las obligaciones pendientes.

El campo de plazo permite registrar el período correspondiente a la venta cuando aplica.

> Las modalidades específicas de pago deben corresponder a las opciones que estén implementadas en la versión final del sistema. No se considera una modalidad implementada únicamente por aparecer escrita en la documentación.

---

## 13. Cuentas por cobrar

La tabla:

```text
cuentas_por_cobrar
```

permite almacenar información de las ventas realizadas a crédito.

Entre los datos manejados se encuentran:

- Identificador de la cuenta.
- Factura relacionada.
- Fecha de vencimiento.
- Monto.
- Saldo.
- Estado.

Esto permite consultar las obligaciones pendientes de los clientes y generar información para los reportes correspondientes.

---

## 14. Reportes

El proyecto cuenta con módulos relacionados con reportes de:

- Ventas.
- Cuentas por cobrar.

La información utilizada para estos reportes se obtiene de la base de datos mediante las consultas correspondientes.

---

## 15. Prueba de la conexión

Una prueba básica de conexión debe comprobar que Python puede conectarse correctamente a:

```text
muebleria_dios_bendice
```

El objetivo es verificar:

1. Que MySQL Server esté iniciado.
2. Que la base de datos exista.
3. Que las credenciales sean correctas.
4. Que `mysql-connector-python` esté instalado.
5. Que Python pueda abrir la conexión sin errores.

---

## 16. Flujo completo de la base de datos durante una venta

```text
Usuario inicia sesión
        ↓
Menú principal
        ↓
Módulo de ventas
        ↓
Seleccionar cliente
        ↓
Seleccionar producto
        ↓
Indicar cantidad
        ↓
Validar stock
        ↓
Registrar factura
        ↓
Registrar detalle de factura
        ↓
Actualizar stock automáticamente
        ↓
Si es crédito
        ↓
Registrar cuenta por cobrar
```

---

## 17. Cumplimiento de mi parte frente al examen final

| Requisito | Estado |
|---|---|
| Crear base de datos | Cumplido |
| Crear tablas | Cumplido |
| Crear relaciones | Cumplido |
| Claves primarias | Cumplido |
| Claves foráneas | Cumplido |
| `AUTO_INCREMENT` | Cumplido |
| Triggers | Cumplido |
| Control de stock | Cumplido |
| Archivo SQL | Cumplido |
| Conexión Python–MySQL | Cumplido |
| `conexion.py` | Cumplido |
| Prueba de conexión | Cumplido |
| Soporte para ventas al contado | Cumplido |
| Soporte para ventas a crédito | Cumplido |
| Cuentas por cobrar | Cumplido |
| Reportes relacionados con la información de BD | Cumplido |

---

## 18. Recomendaciones para ejecutar correctamente el proyecto

Antes de iniciar el sistema:

1. Verificar que MySQL Server esté ejecutándose.
2. Confirmar que exista la base de datos `muebleria_dios_bendice`.
3. Verificar que las seis tablas estén creadas.
4. Confirmar que los triggers existan.
5. Instalar `mysql-connector-python`.
6. Configurar la contraseña local en `conexion.py` sin publicarla en GitHub.
7. Ejecutar el archivo principal del proyecto.

---

## 19. Git y GitHub

Para descargar el proyecto:

```bash
git clone https://github.com/rosarioalexander19-gif/Muebleria_Dios_Bendice.git
```

Entrar a la carpeta:

```bash
cd Muebleria_Dios_Bendice
```

Comprobar el estado del repositorio:

```bash
git status
```

Actualizar el proyecto:

```bash
git pull
```

Agregar cambios:

```bash
git add .
```

Crear un commit:

```bash
git commit -m "Actualización del proyecto"
```

Subir cambios:

```bash
git push
```

---

## 20. Conclusión

Mi participación en el proyecto se concentra en la construcción y funcionamiento de la **base de datos**, así como en la **conexión entre Python y MySQL**.

La base de datos `muebleria_dios_bendice` proporciona la estructura necesaria para administrar clientes, productos, usuarios, facturas, detalles de facturas y cuentas por cobrar.

Además, los triggers `validar_stock` y `actualizar_stock` permiten controlar automáticamente el inventario durante el proceso de ventas.

La conexión definida en `conexion.py` permite que la aplicación desarrollada en Python trabaje directamente con MySQL, integrando la base de datos con los módulos del sistema.

Esta implementación forma parte del proyecto final de **Programación II – Sistema de Gestión de Ventas: Mueblería Dios Bendice**.
