from datetime import datetime, timedelta

from model.factura import Factura
from model.cuenta_cobrar import CuentaCobrar

from repository.factura_repository import insertar_factura
from repository.detalle_factura_repository import insertar_detalle
from repository.cuenta_cobrar_repository import insertar_cuenta


def calcular_subtotal(cantidad, precio):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que 0")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor que 0")

    return cantidad * precio


def calcular_total(detalles):
    if not detalles:
        raise ValueError("La factura debe tener al menos un producto")

    total = 0

    for detalle in detalles:
        total += detalle.subtotal

    return total


def guardar_factura(
    id_cliente,
    id_usuario,
    tipo_pago,
    plazo,
    detalles
):
    if id_cliente is None:
        raise ValueError("Debe seleccionar un cliente")

    if id_usuario is None:
        raise ValueError("Debe seleccionar un usuario")

    if not tipo_pago or not tipo_pago.strip():
        raise ValueError("Debe seleccionar un tipo de pago")

    if not detalles:
        raise ValueError("La factura debe tener al menos un producto")

    tipo_pago = tipo_pago.strip()

    # Validar el tipo de pago
    if tipo_pago.lower() not in ("contado", "credito"):
        raise ValueError(
            "El tipo de pago debe ser Contado o Credito"
        )

    # Validar el plazo cuando sea crédito
    if tipo_pago.lower() == "credito":

        if plazo is None:
            raise ValueError(
                "Debe indicar un plazo para una venta a crédito"
            )

        if plazo <= 0:
            raise ValueError(
                "El plazo debe ser mayor que 0 días"
            )

    # Las ventas de contado no necesitan plazo
    if tipo_pago.lower() == "contado":
        plazo = None

    total = calcular_total(detalles)

    factura = Factura(
        id_cliente=id_cliente,
        id_usuario=id_usuario,
        tipo_pago=tipo_pago,
        plazo=plazo,
        total=total
    )

    # Insertar factura
    id_factura = insertar_factura(factura)

    factura.id_factura = id_factura

    # Insertar detalles
    for detalle in detalles:
        detalle.id_factura = id_factura
        insertar_detalle(detalle)

    # Crear cuenta por cobrar si la venta es a crédito
    if tipo_pago.lower() == "credito":

        fecha_vencimiento = (
            datetime.now() + timedelta(days=plazo)
        ).date()

        cuenta = CuentaCobrar(
            id_factura=id_factura,
            fecha_vencimiento=fecha_vencimiento,
            monto=total,
            saldo=total,
            estado="Pendiente"
        )

        insertar_cuenta(cuenta)

    return factura
