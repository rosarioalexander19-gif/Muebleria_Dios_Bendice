# Youmelky Alexander Rosario –

## Base de Datos y Conexión

### Proyecto Final de Programación II

**Sistema de Gestión de Ventas – Mueblería Dios Bendice**

---

## 1. Responsabilidad

Mi responsabilidad en el proyecto corresponde a la **creación de la base de datos y la conexión entre Python y MySQL**.

Mis principales tareas fueron:

* Crear la base de datos.
* Crear las tablas y relaciones.
* Definir claves primarias y foráneas.
* Crear los triggers.
* Preparar el archivo `base_de_datos.sql`.
* Crear `conexion.py`.
* Conectar Python con MySQL.
* Configurar la conexión en Visual Studio Code.
* Integrar mi trabajo al repositorio de GitHub.

---

## 2. Base de datos

La base de datos creada se llama:

```text
muebleria_dios_bendice
```

Para crearla:

```sql
CREATE DATABASE muebleria_dios_bendice;
```

Para utilizarla:

```sql
USE muebleria_dios_bendice;
```

Las principales tablas creadas son:

```text
clientes
productos
usuarios
facturas
detalle_factura
```

Para comprobar las tablas:

```sql
SHOW TABLES;
```

También se utilizaron **claves primarias, claves foráneas y relaciones** para conectar las diferentes tablas.

---

## 3. Triggers

Se crearon triggers para automatizar procesos de la base de datos.

Uno de sus usos principales es actualizar automáticamente el stock de los productos después de registrar una venta.

Para comprobar los triggers:

```sql
SHOW TRIGGERS;
```

---

## 4. Archivo de base de datos

Se creó el archivo:

```text
base_de_datos.sql
```

Este archivo contiene la estructura necesaria para crear la base de datos, tablas, relaciones, triggers y datos iniciales.

Para utilizarlo en otra computadora:

```sql
SOURCE base_de_datos.sql;
```

De esta manera, los demás integrantes pueden crear una copia de la misma estructura de la base de datos.

---

## 5. Conexión Python + MySQL

Para conectar Python con MySQL se instaló:

```bash
pip install mysql-connector-python
```

Se creó el archivo:

```text
conexion.py
```

Con una conexión de este tipo:

```python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TU_CONTRASEÑA",
    database="muebleria_dios_bendice"
)

print("Conexión exitosa")
```

La conexión permite la comunicación:

```text
Python
   ↓
mysql-connector-python
   ↓
MySQL Server
   ↓
muebleria_dios_bendice
```

Cada integrante debe utilizar su propia contraseña de MySQL.

---

## 6. Visual Studio Code y GitHub

El proyecto fue desarrollado utilizando **Visual Studio Code** y se utilizó **Git/GitHub** para compartir el código entre los integrantes.

Comandos principales utilizados:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

Para obtener los cambios del equipo:

```bash
git pull
Para obtener el proyecto por primera vez:
bash
git clone URL_DEL_REPOSITORIO

## 7. Resultado

La parte desarrollada permite que el sistema tenga una base de datos funcional y que Python pueda comunicarse con MySQL.

Además, mediante `base_de_datos.sql` y GitHub, los demás integrantes pueden configurar el proyecto en sus propias computadoras utilizando la misma estructura de base de datos.

**Youmelky Alexander Rosario**

**Responsabilidad:** Base de Datos y Conexión.
