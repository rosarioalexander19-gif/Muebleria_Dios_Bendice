class Factura:
    def __init__(
        self,
        id_factura=None,
        id_cliente=None,
        id_usuario=None,
        fecha=None,
        tipo_pago="",
        plazo=None,
        total=0
    ):
        self.id_factura = id_factura
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.tipo_pago = tipo_pago
        self.plazo = plazo
        self.total = total

    def __str__(self):
        return (
            f"Factura #{self.id_factura} - "
            f"Cliente: {self.id_cliente} - "
            f"Usuario: {self.id_usuario} - "
            f"Fecha: {self.fecha} - "
            f"Tipo de pago: {self.tipo_pago} - "
            f"Total: RD${self.total}"
        )
