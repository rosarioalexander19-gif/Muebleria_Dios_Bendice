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

Esta implementación forma parte del proyecto final de **Programación II – Sistema de Gestión de Ventas: Mueblería Dios Bendice.

######DANIELA REYES HEREDIA ---Login, Usuario y clientes.
## Proyecto Final de Programación II

#####Gestión de Usuarios y Clientes

#Descripción

En esta parte del proyecto trabajé en la creación de los módulos de usuarios y clientes. La idea principal fue organizar el código en diferentes partes para que cada una tenga una función específica y sea más fácil de entender y mantener.

Para realizar esta parte utilicé Python, Tkinter y MySQL. Se trabajó con clases para representar los datos, repositorios para comunicarse con la base de datos, servicios para manejar las validaciones y las ventanas para que el usuario pueda interactuar con el sistema.

1. Modelo de Usuario

Primero se creó la clase "Usuario", que se utiliza para representar la información de cada usuario del sistema.

La clase contiene los siguientes datos:

- ID del usuario.
- Nombre de usuario.
- Contraseña.
- Rol.
- Estado.

También se agregó el método "__str__()" para poder mostrar la información del usuario de una forma más organizada.

2. Modelo de Cliente

También se creó la clase "Cliente", que contiene los datos necesarios para registrar a los clientes.

Los datos utilizados son:

- ID del cliente.
- Nombre.
- Apellido.
- Cédula.
- Teléfono.
- Dirección.
- Correo electrónico.

Al igual que en el modelo de usuario, se utilizó "__str__()" para representar la información del cliente.

3. Repositorio de Usuarios

Para trabajar con la base de datos se creó "UsuarioRepository".

Esta clase se encarga de realizar las operaciones principales con los usuarios:

- Crear usuarios.
- Mostrar todos los usuarios.
- Buscar un usuario por su nombre.
- Actualizar usuarios.
- Eliminar usuarios.

Para realizar estas operaciones se utilizan consultas SQL y una conexión con MySQL. Después de realizar cambios en la base de datos se utiliza "commit()" para guardar los cambios.

4. Repositorio de Clientes

También se creó "ClienteRepository", encargado de manejar los datos de los clientes en la base de datos.

Las operaciones principales son:

- Crear clientes.
- Obtener todos los clientes.
- Buscar un cliente por su ID.
- Actualizar clientes.
- Eliminar clientes.

De esta manera, las operaciones de la base de datos quedan separadas de las ventanas del programa.

5. Servicio de Usuarios

Se creó "UsuarioService" para manejar la lógica relacionada con los usuarios.

Antes de crear un usuario se verifica que el nombre de usuario y la contraseña no estén vacíos.

También se agregó la función de inicio de sesión. Para poder entrar al sistema se comprueba que:

1. El usuario exista.
2. El usuario se encuentre activo.
3. La contraseña coincida.

Si alguna de estas condiciones no se cumple, el inicio de sesión no permite continuar.

6. Servicio de Clientes

Para los clientes se creó "ClienteService".

En este servicio se realizan algunas validaciones antes de guardar un cliente. Se verifica que estén completos los datos principales:

- Nombre.
- Apellido.
- Cédula.
- Teléfono.
- Dirección.
- Correo.

Después de validar los datos, se crea el objeto "Cliente" y se envía al repositorio para guardarlo en la base de datos.

También permite consultar, actualizar y eliminar clientes.

7. Ventana de Inicio de Sesión

Se creó una ventana utilizando Tkinter para que los usuarios puedan iniciar sesión.

La ventana contiene:

- Campo para el usuario.
- Campo para la contraseña.
- Botón de inicio de sesión.

Cuando se presiona el botón, se comprueban los datos mediante "UsuarioService".

Si los datos son correctos, aparece un mensaje indicando que el inicio de sesión fue exitoso y se abre el menú principal.

Si los datos son incorrectos, se muestra un mensaje de error.

8. Ventana de Gestión de Clientes

También trabajé en la ventana de gestión de clientes utilizando Tkinter.

Esta ventana permite registrar y administrar los clientes desde una interfaz gráfica.

Los campos que se pueden llenar son:

- Nombre.
- Apellido.
- Cédula.
- Teléfono.
- Dirección.
- Correo.

Además, se agregaron los botones:

- Crear: permite registrar un nuevo cliente.
- Actualizar: permite modificar los datos de un cliente seleccionado.
- Eliminar: permite eliminar un cliente.

Los clientes registrados se muestran en una tabla utilizando "Treeview".

Al seleccionar un cliente de la tabla, sus datos se cargan automáticamente en los campos del formulario para poder modificarlos o eliminarlos.

9. Organización del código

La parte que trabajé quedó separada por responsabilidades. Los modelos contienen los datos, los repositorios trabajan con la base de datos, los servicios manejan la lógica y las ventanas se encargan de la interacción con el usuario.

Esta organización ayuda a que el proyecto sea más ordenado y facilita realizar cambios posteriormente sin tener que modificar todo el programa.

#Conclusión

Con esta parte del proyecto se logró implementar la gestión de usuarios y clientes, incluyendo el inicio de sesión, registro, consulta, actualización y eliminación de información.

El uso de Python, Tkinter y MySQL permitió conectar la interfaz gráfica con la lógica del programa y la base de datos. También aprendí a separar las diferentes funciones del sistema para que el código sea más fácil de organizar y mantener.

# Gestión de Productos

## 1. Descripción

La gestión de productos permite registrar, consultar, modificar y eliminar los productos de la mueblería.

Esta parte del sistema fue desarrollada utilizando Python, Tkinter y MySQL. El módulo permite que el usuario pueda administrar la información de los productos mediante una interfaz gráfica sencilla.

Cada producto contiene un código o ID, nombre, precio y cantidad disponible en stock.

---

## 2. Funcionalidades

El módulo de productos permite realizar las siguientes operaciones:

- Registrar productos nuevos.
- Consultar los productos registrados.
- Editar la información de un producto.
- Eliminar productos.
- Mostrar los productos en una tabla.
- Validar los datos introducidos por el usuario.
- Limpiar los campos del formulario.

---

## 3. Datos de los productos

Cada producto maneja los siguientes datos:

| Campo | Descripción |
|---|---|
| ID | Identificador único del producto |
| Nombre | Nombre del producto |
| Precio | Precio del producto |
| Stock | Cantidad disponible del producto |

---

## 4. Organización del código

La funcionalidad de productos está organizada por responsabilidades para mantener el código ordenado y facilitar su mantenimiento.

### Modelo

El archivo `producto.py` contiene la clase `Producto`.

La clase representa un producto y almacena:

- ID del producto.
- Nombre.
- Precio.
- Stock.

También cuenta con un método que permite mostrar la información del producto.

---

### Repositorio

El repositorio se encarga de realizar las operaciones directamente con la base de datos.

Las operaciones principales son:

- Insertar productos.
- Obtener productos.
- Actualizar productos.
- Eliminar productos.

Para guardar un producto se utiliza una sentencia `INSERT`.

Para consultar los productos se utiliza una sentencia `SELECT`.

Para modificar un producto se utiliza una sentencia `UPDATE`.

Para eliminar un producto se utiliza una sentencia `DELETE`.

---

### Servicio

El servicio contiene la lógica y las validaciones necesarias antes de realizar las operaciones en la base de datos.

Las principales funciones son:

- `guardar_producto()`
- `listar_productos()`
- `editar_producto()`
- `borrar_producto()`

Antes de guardar o editar un producto se realizan las siguientes validaciones:

- El nombre no puede estar vacío.
- El precio debe ser mayor que 0.
- El stock no puede ser negativo.

Estas validaciones ayudan a evitar que se introduzcan datos incorrectos en el sistema.

---

## 5. Interfaz gráfica

La interfaz gráfica fue desarrollada utilizando Tkinter.

La ventana tiene como título:

**GESTIÓN DE PRODUCTOS**

El formulario permite introducir los siguientes datos:

- Código.
- Nombre.
- Precio.
- Stock.

Los productos registrados se muestran en una tabla utilizando `Treeview`.

La tabla muestra las columnas:

- ID.
- Nombre.
- Precio.
- Stock.

---

## 6. Botones de la interfaz

La interfaz cuenta con cuatro botones principales:

### Guardar

Permite registrar un nuevo producto en la base de datos.

### Editar

Permite modificar la información de un producto seleccionado.

### Eliminar

Permite eliminar un producto después de confirmar la operación.

### Limpiar

Permite borrar la información de los campos del formulario.

---

## 7. Selección de productos

Cuando el usuario selecciona un producto desde la tabla, sus datos se cargan automáticamente en los campos del formulario.

Esto permite consultar la información y posteriormente editarla o eliminarla.

---

## 8. Conexión con la base de datos

El módulo utiliza una conexión con la base de datos para almacenar y consultar la información de los productos.

Las operaciones realizadas desde la interfaz gráfica son enviadas al servicio, posteriormente al repositorio y finalmente a la base de datos.

El flujo de trabajo es:

**Interfaz gráfica → Servicio → Repositorio → Base de datos**

Para consultar información, el proceso funciona de manera inversa:

**Base de datos → Repositorio → Servicio → Interfaz gráfica**

---

## 9. Flujo para registrar un producto

El proceso para registrar un producto funciona de la siguiente manera:

1. El usuario introduce el nombre, precio y stock.
2. Presiona el botón **Guardar**.
3. El servicio valida los datos.
4. Si los datos son correctos, se crea el objeto `Producto`.
5. El repositorio inserta el producto en la base de datos.
6. Se muestra un mensaje indicando que el producto fue guardado correctamente.
7. La tabla se actualiza para mostrar el nuevo producto.

---

## 10. Flujo para editar un producto

Para editar un producto:

1. El usuario selecciona un producto de la tabla.
2. Los datos se cargan en el formulario.
3. El usuario modifica la información necesaria.
4. Presiona el botón **Editar**.
5. El sistema valida los datos.
6. Se actualiza la información en la base de datos.
7. La tabla se actualiza automáticamente.

---

## 11. Flujo para eliminar un producto

Para eliminar un producto:

1. El usuario selecciona un producto.
2. Presiona el botón **Eliminar**.
3. El sistema solicita confirmación.
4. Si el usuario confirma, se elimina el producto.
5. La tabla se actualiza y deja de mostrar el producto eliminado.

---

## 12. Tecnologías utilizadas

Para desarrollar este módulo se utilizaron:

- **Python** como lenguaje de programación.
- **Tkinter** para crear la interfaz gráfica.
- **MySQL** para almacenar la información.
- **GitHub** para almacenar y gestionar el código del proyecto.

---

## 13. Conclusión

El módulo de gestión de productos permite administrar de manera sencilla la información de los productos de la mueblería.

La separación entre modelo, repositorio, servicio e interfaz gráfica permite mantener el código organizado y facilita realizar modificaciones posteriormente.

Con esta funcionalidad, el usuario puede registrar, consultar, editar y eliminar productos, manteniendo actualizada la información del inventario.


--Participación de Claritza Esther Barry Brown--
Módulo de Ventas, Facturación, Cuentas por Cobrar y Reportes

Mi participación en el proyecto estuvo enfocada principalmente en el desarrollo y funcionamiento del proceso de ventas, incluyendo la creación de facturas, el registro de los productos vendidos y el manejo de las ventas realizadas a crédito.

Se desarrolló la interfaz gráfica correspondiente al módulo de Ventas, utilizando Python y Tkinter. Esta interfaz permite introducir los datos necesarios para realizar una venta, como el ID del cliente, el ID del usuario, el tipo de pago, el plazo cuando la venta es a crédito, el ID del producto, la cantidad y el precio.

También se implementó el proceso para agregar productos a una venta, calculando automáticamente el subtotal correspondiente a cada producto mediante la cantidad y el precio. Los productos agregados son mostrados en una tabla dentro de la interfaz, permitiendo visualizar la información antes de registrar definitivamente la venta.

Otra parte importante fue la implementación del cálculo del total de la factura. El sistema toma los subtotales de todos los productos agregados y calcula automáticamente el monto total de la venta. Además, se agregaron validaciones para evitar cantidades o precios menores o iguales a cero y para impedir que se registre una factura sin productos.

En cuanto a la facturación, se trabajó en el proceso de creación de una factura asociada a un cliente y a un usuario. Al registrar la venta, la información se almacena en la base de datos MySQL y se genera el número correspondiente de factura. También se registran los detalles de los productos incluidos en dicha factura.

Se implementó además el manejo de ventas a crédito. Cuando el usuario selecciona el tipo de pago "Crédito", el sistema solicita un plazo en días y utiliza esta información para calcular la fecha de vencimiento. Posteriormente, se crea automáticamente un registro en la tabla de cuentas por cobrar, incluyendo el monto de la venta, el saldo pendiente y el estado de la cuenta.

Para garantizar el correcto funcionamiento del proceso, se realizaron pruebas de integración entre la interfaz gráfica desarrollada en Python y la base de datos MySQL. Se verificó el registro de clientes, productos, facturas, detalles de facturas y cuentas por cobrar, así como la consulta posterior de la información mediante los reportes.

También se participó en el desarrollo del módulo de Reportes, encargado de mostrar información relacionada con las ventas realizadas y las cuentas por cobrar. El reporte de ventas permite visualizar datos como el número de factura, fecha, cliente, tipo de pago y total de la venta. El reporte de cuentas por cobrar permite consultar las cuentas generadas por ventas a crédito, mostrando información como factura, cliente, fecha de vencimiento, monto, saldo y estado.

Archivos y módulos trabajados

Interfaz gráfica:

ui/ventas.py
ui/reportes.py

Servicios:

service/venta_service.py
service/reporte_service.py

Repositorios:

repository/factura_repository.py
repository/detalle_factura_repository.py
repository/cuenta_cobrar_repository.py

Modelos relacionados:

model/factura.py
model/detalle_factura.py
model/cuenta_cobrar.py

Reportes:

reports/ventas_report.py
reports/cuentas_cobrar_report.py
Funcionalidades desarrolladas y comprobadas
Registro de ventas.
Agregar productos a una factura.
Cálculo automático de subtotales.
Cálculo automático del total de la venta.
Validación de cantidades y precios.
Selección del tipo de pago.
Registro de ventas de contado.
Registro de ventas a crédito.
Validación del plazo de crédito.
Cálculo de la fecha de vencimiento.
Creación automática de cuentas por cobrar.
Registro de facturas en MySQL.
Registro de detalles de las facturas.
Consulta de ventas mediante reportes.
Consulta de cuentas por cobrar mediante reportes.
Pruebas de conexión y funcionamiento entre Python, Tkinter y MySQL.
Resultado

El desarrollo de estos módulos permitió integrar el proceso de venta completo dentro del sistema de la Mueblería Dios Bendice, desde la selección del cliente y los productos hasta la generación de la factura, el manejo de créditos y la consulta de los resultados mediante reportes. Las funcionalidades fueron probadas utilizando datos de prueba y verificando que la información se almacenara correctamente en la base de datos MySQL.
