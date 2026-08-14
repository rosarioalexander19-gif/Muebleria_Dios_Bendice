class Usuario:

    def __init__(
        self,
        id_usuario=None,
        nombre_usuario="",
        contrasena="",
        rol="",
        estado="Activo"
    ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol
        self.estado = estado

    def __str__(self):
        return (
            f"{self.id_usuario} - "
            f"{self.nombre_usuario} - "
            f"{self.rol} - "
            f"{self.estado}"
        )
