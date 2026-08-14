class CuentaCobrar:
    def __init__(
        self,
        id_cuenta=None,
        id_factura=None,
        fecha_vencimiento=None,
        monto=0,
        saldo=0,
        estado="Pendiente"
    ):
        self.id_cuenta = id_cuenta
        self.id_factura = id_factura
        self.fecha_vencimiento = fecha_vencimiento
        self.monto = monto
        self.saldo = saldo
        self.estado = estado

    def __str__(self):
        return (
            f"Cuenta #{self.id_cuenta} - "
            f"Factura: {self.id_factura} - "
            f"Vencimiento: {self.fecha_vencimiento} - "
            f"Monto: RD${self.monto} - "
            f"Saldo: RD${self.saldo} - "
            f"Estado: {self.estado}"
        )
