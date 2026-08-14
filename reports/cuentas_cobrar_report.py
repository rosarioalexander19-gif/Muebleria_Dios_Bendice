from service.reporte_service import obtener_reporte_cuentas_por_cobrar


def generar_reporte_cuentas():
    cuentas = obtener_reporte_cuentas_por_cobrar()

    print("\n======= REPORTE DE CUENTAS POR COBRAR =======")

    if not cuentas:
        print("No hay cuentas por cobrar registradas.")
        return

    for cuenta in cuentas:
        print(
            f"Cuenta: {cuenta[0]} | "
            f"Factura: {cuenta[1]} | "
            f"Cliente: {cuenta[2]} {cuenta[3]} | "
            f"Vencimiento: {cuenta[4]} | "
            f"Monto: RD${cuenta[5]} | "
            f"Saldo: RD${cuenta[6]} | "
            f"Estado: {cuenta[7]}"
        )

    print("==============================================")


if __name__ == "__main__":
    generar_reporte_cuentas()
