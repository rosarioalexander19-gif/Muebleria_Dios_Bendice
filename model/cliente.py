
class Cliente:
    def __init__(
        self,
        id_cliente=None,
        nombre_completo="",
        cedula="",
        telefono="",
        direccion=""
    ):
        self.id_cliente = id_cliente
        self.nombre_completo = nombre_completo
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return (
            f"{self.id_cliente} - "
            f"{self.nombre_completo} - "
            f"{self.cedula} - "
            f"{self.telefono} - "
            f"{self.direccion}"
        )


