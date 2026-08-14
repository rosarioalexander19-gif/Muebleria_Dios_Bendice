from conexion import conectar


def insertar_detalle(detalle):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO detalle_factura
        (id_factura, id_producto, cantidad, precio, subtotal)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            detalle.id_factura,
            detalle.id_producto,
            detalle.cantidad,
            detalle.precio,
            detalle.subtotal
        )
    )

    conexion.commit()
    cursor.close()
    conexion.close()


def obtener_detalles():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM detalle_factura")
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


def obtener_detalles_por_factura(id_factura):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM detalle_factura WHERE id_factura=%s",
        (id_factura,)
    )

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


def actualizar_detalle(detalle):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE detalle_factura
        SET id_factura=%s,
            id_producto=%s,
            cantidad=%s,
            precio=%s,
            subtotal=%s
        WHERE id_detalle=%s
        """,
        (
            detalle.id_factura,
            detalle.id_producto,
            detalle.cantidad,
            detalle.precio,
            detalle.subtotal,
            detalle.id_detalle
        )
    )

    conexion.commit()
    cursor.close()
    conexion.close()


def eliminar_detalle(id_detalle):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM detalle_factura WHERE id_detalle=%s",
        (id_detalle,)
    )

    conexion.commit()
    cursor.close()
    conexion.close()
