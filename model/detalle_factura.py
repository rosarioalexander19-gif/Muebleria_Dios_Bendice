class DetalleFactura:
    def __init__(
        self,
        id_detalle=None,
        id_factura=None,
        id_producto=None,
        cantidad=0,
        precio=0,
        subtotal=0
    ):
        self.id_detalle = id_detalle
        self.id_factura = id_factura
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal

    def __str__(self):
        return (
            f"Detalle #{self.id_detalle} - "
            f"Factura: {self.id_factura} - "
            f"Producto: {self.id_producto} - "
            f"Cantidad: {self.cantidad} - "
            f"Precio: RD${self.precio} - "
            f"Subtotal: RD${self.subtotal}"
        )
