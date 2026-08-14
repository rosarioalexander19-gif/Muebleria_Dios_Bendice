class Cliente:

    def __init__(
        self,
        id_cliente=None,
        nombre="",
        apellido="",
        cedula="",
        telefono="",
        direccion="",
        correo=""
    ):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (
            f"{self.id_cliente} - "
            f"{self.nombre} {self.apellido} - "
            f"{self.cedula} - "
            f"{self.telefono} - "
            f"{self.direccion} - "
            f"{self.correo}"
        )
