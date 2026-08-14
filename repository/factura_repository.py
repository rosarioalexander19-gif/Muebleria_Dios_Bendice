from conexion import conectar


def insertar_factura(factura):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO facturas
        (id_cliente, id_usuario, tipo_pago, plazo, total)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            factura.id_cliente,
            factura.id_usuario,
            factura.tipo_pago,
            factura.plazo,
            factura.total
        )
    )

    conexion.commit()
    id_factura = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_factura


def obtener_facturas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM facturas")
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


def actualizar_factura(factura):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE facturas
        SET id_cliente=%s,
            id_usuario=%s,
            tipo_pago=%s,
            plazo=%s,
            total=%s
        WHERE id_factura=%s
        """,
        (
            factura.id_cliente,
            factura.id_usuario,
            factura.tipo_pago,
            factura.plazo,
            factura.total,
            factura.id_factura
        )
    )

    conexion.commit()
    cursor.close()
    conexion.close()


def eliminar_factura(id_factura):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM facturas WHERE id_factura=%s",
        (id_factura,)
    )

    conexion.commit()
    cursor.close()
    conexion.close()
