from model.producto import Producto
from conexion import conectar


def insertar_producto(producto):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO productos
        (nombre, precio, stock)
        VALUES (%s, %s, %s)
    """

    valores = (
        producto.nombre,
        producto.precio,
        producto.stock
    )

    cursor.execute(sql, valores)

    conexion.commit()

    producto.id_producto = cursor.lastrowid

    cursor.close()
    conexion.close()

    return producto


def obtener_productos():

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        SELECT id_producto, nombre, precio, stock
        FROM productos
    """

    cursor.execute(sql)

    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    productos = []

    for fila in filas:

        producto = Producto(
            id_producto=fila[0],
            nombre=fila[1],
            precio=fila[2],
            stock=fila[3]
        )

        productos.append(producto)

    return productos


def actualizar_producto(producto):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        UPDATE productos
        SET nombre = %s,
            precio = %s,
            stock = %s
        WHERE id_producto = %s
    """

    valores = (
        producto.nombre,
        producto.precio,
        producto.stock,
        producto.id_producto
    )

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_producto(id_producto):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        DELETE FROM productos
        WHERE id_producto = %s
    """

    cursor.execute(sql, (id_producto,))

    conexion.commit()

    cursor.close()
    conexion.close()
