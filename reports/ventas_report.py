from service.reporte_service import obtener_reporte_ventas


def generar_reporte_ventas():
    ventas = obtener_reporte_ventas()

    print("\n========== REPORTE DE VENTAS ==========")

    if not ventas:
        print("No hay ventas registradas.")
        return

    for venta in ventas:
        print(
            f"Factura: {venta[0]} | "
            f"Fecha: {venta[1]} | "
            f"Cliente: {venta[2]} {venta[3]} | "
            f"Tipo de pago: {venta[4]} | "
            f"Total: RD${venta[5]}"
        )

    print("========================================")


if __name__ == "__main__":
    generar_reporte_ventas()
