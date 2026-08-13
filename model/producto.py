class Producto:
    def __init__(self, id_producto=None, nombre="", categoria="", precio=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - RD${self.precio} - Stock: {self.stock}"
