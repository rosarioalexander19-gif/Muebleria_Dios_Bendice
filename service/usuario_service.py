from model.usuario import Usuario


class UsuarioService:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def crear_usuario(self, nombre_usuario, contrasena, rol="Usuario"):

        if not nombre_usuario:
            raise ValueError("El nombre de usuario es obligatorio.")

        if not contrasena:
            raise ValueError("La contraseña es obligatoria.")

        nuevo_usuario = self.usuario_repository.crear(
            Usuario(
                nombre_usuario=nombre_usuario,
                contrasena=contrasena,
                rol=rol
            )
        )

        return nuevo_usuario

    def obtener_usuarios(self):
        return self.usuario_repository.obtener_todos()

    def iniciar_sesion(self, nombre_usuario, contrasena):

        usuario_encontrado = (
            self.usuario_repository.buscar_por_usuario(nombre_usuario)
        )

        if usuario_encontrado is None:
            return False

        if usuario_encontrado.estado != "Activo":
            return False

        return usuario_encontrado.contrasena == contrasena

    def actualizar_usuario(self, usuario):
        self.usuario_repository.actualizar(usuario)

    def eliminar_usuario(self, id_usuario):
        self.usuario_repository.eliminar(id_usuario)
