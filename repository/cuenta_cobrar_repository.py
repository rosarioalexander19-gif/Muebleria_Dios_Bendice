from conexion import conectar


def insertar_cuenta(cuenta):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO cuentas_por_cobrar
        (id_factura, fecha_vencimiento, monto, saldo, estado)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            cuenta.id_factura,
            cuenta.fecha_vencimiento,
            cuenta.monto,
            cuenta.saldo,
            cuenta.estado
        )
    )

    conexion.commit()
    cursor.close()
    conexion.close()


def obtener_cuentas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM cuentas_por_cobrar")
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


def obtener_cuenta_por_factura(id_factura):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM cuentas_por_cobrar WHERE id_factura=%s",
        (id_factura,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


def actualizar_cuenta(cuenta):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE cuentas_por_cobrar
        SET id_factura=%s,
            fecha_vencimiento=%s,
            monto=%s,
            saldo=%s,
            estado=%s
        WHERE id_cuenta=%s
        """,
        (
            cuenta.id_factura,
            cuenta.fecha_vencimiento,
            cuenta.monto,
            cuenta.saldo,
            cuenta.estado,
            cuenta.id_cuenta
        )
    )

    conexion.commit()
    cursor.close()
    conexion.close()


def eliminar_cuenta(id_cuenta):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM cuentas_por_cobrar WHERE id_cuenta=%s",
        (id_cuenta,)
    )

    conexion.commit()
    cursor.close()
    conexion.close()

