
class UsuarioService:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def crear_usuario(self, nombre, usuario, password):

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if not usuario:
            raise ValueError("El usuario es obligatorio.")

        if not password:
            raise ValueError("La contraseña es obligatoria.")

        nuevo_usuario = self.usuario_repository.crear(
            Usuario(
                nombre=nombre,
                usuario=usuario,
                password=password
            )
        )

        return nuevo_usuario

    def obtener_usuarios(self):
        return self.usuario_repository.obtener_todos()

    def iniciar_sesion(self, usuario, password):

        usuario_encontrado = (
            self.usuario_repository.buscar_por_usuario(usuario)
        )

        if usuario_encontrado is None:
            return False

        return usuario_encontrado.password == password

    def actualizar_usuario(self, usuario):
        self.usuario_repository.actualizar(usuario)

    def eliminar_usuario(self, id_usuario):
        self.usuario_repository.eliminar(id_usuario)

