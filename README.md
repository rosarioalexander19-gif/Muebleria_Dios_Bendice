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

####### DANIELA REYES HEREDIA###########

#Módulo de Login, Usuarios y Clientes.
Este módulo forma parte del proyecto y tiene como objetivo gestionar el acceso al sistema mediante un login, además de permitir la administración de usuarios y clientes.

Mi responsabilidad dentro del proyecto fue desarrollar:
* Login de usuarios.
* Registro de usuarios.
* Consulta de usuarios.
* Actualización de usuarios.
* Eliminación de usuarios.
* Registro de clientes.
* Consulta de clientes.
* Actualización de clientes.
* Eliminación de clientes.

# 1. Herramientas utilizadas
Para desarrollar este módulo utilicé las siguientes herramientas:
* Python
* MySQL
Tkinter

Python se utilizó para desarrollar la lógica del sistema y la interfaz gráfica.

Tkinter se utilizó para crear las ventanas del Login y la gestión de clientes.

MySQL se utilizó para almacenar la información de usuarios y clientes.

# 4. Creación del proyecto

Primero creé la carpeta principal del proyecto.

Dentro de ella organicé el código utilizando una arquitectura por capas.

La estructura correspondiente a mi parte quedó de la siguiente manera:

proyecto/
│
├── model/
│   ├── usuario.py
│   └── cliente.py
│
├── repository/
│   ├── usuario_repository.py
│   └── cliente_repository.py
│
├── service/
│   ├── usuario_service.py
│   └── cliente_service.py
│
└── ui/
    ├── login.py
    └── clientes.py

Esta organización permite separar las responsabilidades de cada parte del programa.

# 5. Capa Model

La carpeta `model` contiene las clases que representan los datos del sistema.

## usuario.py

En este archivo creé la clase `Usuario`.

La clase contiene los datos necesarios para identificar a un usuario:

* ID
* Nombre
* Usuario
* Contraseña

## cliente.py

En este archivo creé la clase `Cliente`.

Contiene:

* ID
* Nombre completo
* Cédula
* Teléfono
* Dirección

# 6. Creación de la base de datos

En MySQL creé las tablas necesarias para almacenar la información.
Después agregué un usuario para realizar las pruebas:
EJEMPL;
INSERT INTO usuarios
(nombre, usuario, password)
VALUES
('Daniela', 'daniela', '1234');
## Tabla clientes

También creé la tabla para almacenar los clientes:

Para realizar una prueba agregué un cliente:

# 7. Capa Repository

La carpeta `repository` contiene las operaciones que permiten comunicarse con la base de datos.

## usuario_repository.py

En este archivo desarrollé las operaciones relacionadas con los usuarios:

* Crear usuario.
* Obtener usuarios.
* Buscar usuario.
* Actualizar usuario.
* Eliminar usuario.

También se utiliza para consultar el usuario durante el proceso de Login.

## cliente_repository.py

En este archivo desarrollé las operaciones para los clientes:

* Crear cliente.
* Obtener clientes.
* Buscar cliente.
* Actualizar cliente.
* Eliminar cliente.

El Repository es la parte que realiza directamente las consultas SQL.

# 8. Capa Service

La carpeta `service` contiene la lógica del sistema.

## usuario_service.py

Aquí se realizan las validaciones de los usuarios y se utilizan las funciones del `UsuarioRepository`.

Por ejemplo, antes de crear un usuario se comprueba que:

* El nombre no esté vacío.
* El usuario no esté vacío.
* La contraseña no esté vacía.

También se utiliza para comprobar los datos del Login.

## cliente_service.py

En este archivo se encuentran las reglas relacionadas con los clientes.

Antes de registrar un cliente se comprueba que tenga:
* Nombre.
* Cédula.
* Teléfono.
* Dirección.

Después se envía la información al Repository para guardarla en MySQL.

# 9. Capa UI

La carpeta `ui` contiene las interfaces gráficas que utiliza el usuario.

## login.py

En este archivo desarrollé la ventana de inicio de sesión.

La ventana contiene:

INICIO DE SESIÓN

Usuario:   

Contraseña: 

[ Iniciar sesión ]

Cuando el usuario introduce sus datos, el Login utiliza el `UsuarioService` para comprobar si las credenciales son correctas.

Si son correctas, se permite el acceso al sistema.

Si son incorrectas, aparece un mensaje indicando que el usuario o contraseña no son correctos.

# 10. clientes.py

En este archivo desarrollé la interfaz para administrar los clientes.

La ventana permite realizar el CRUD completo.

El usuario puede:


### Leer

Mostrar los clientes registrados en una tabla utilizando `Treeview`.

La tabla muestra:

ID | Nombre | Cédula | Teléfono | Dirección

### Actualizar

Seleccionar un cliente de la tabla, modificar sus datos y guardar los cambios.

### Eliminar

Seleccionar un cliente y eliminarlo de la base de datos.

Cada capa tiene una responsabilidad diferente.

### Model

Representa los datos.

### Repository

Realiza las operaciones con la base de datos.

### Service

Contiene las validaciones y la lógica del sistema.

### UI

Es la interfaz gráfica que utiliza el usuario.

Esta separación permite que el código esté más organizado y sea más fácil de mantener.


La parte desarrollada permite controlar el acceso al sistema mediante un Login y administrar la información de usuarios y clientes.

Se implementó el CRUD completo para realizar las operaciones de crear, leer, actualizar y eliminar.

Además, el proyecto fue organizado utilizando las capas `Model`, `Repository`, `Service` y `UI`, lo que permite mantener el código organizado, separar responsabilidades y facilitar futuras modificaciones.

