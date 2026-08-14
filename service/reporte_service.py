from conexion import conectar


def obtener_reporte_ventas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            f.id_factura,
            f.fecha,
            c.nombre,
            c.apellido,
            f.tipo_pago,
            f.total
        FROM facturas f
        INNER JOIN clientes c
            ON f.id_cliente = c.id_cliente
        ORDER BY f.fecha DESC
    """)

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados


def obtener_reporte_cuentas_por_cobrar():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            cc.id_cuenta,
            cc.id_factura,
            c.nombre,
            c.apellido,
            cc.fecha_vencimiento,
            cc.monto,
            cc.saldo,
            cc.estado
        FROM cuentas_por_cobrar cc
        INNER JOIN facturas f
            ON cc.id_factura = f.id_factura
        INNER JOIN clientes c
            ON f.id_cliente = c.id_cliente
        ORDER BY cc.fecha_vencimiento ASC
    """)

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return resultados

