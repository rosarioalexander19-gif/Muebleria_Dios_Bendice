from conexion import conectar

from repository.usuario_repository import UsuarioRepository
from repository.cliente_repository import ClienteRepository

from service.usuario_service import UsuarioService
from service.cliente_service import ClienteService

from ui.login import LoginWindow
from ui.menu import MenuWindow


def iniciar_sistema():

    print("MAIN.PY SE ESTA EJECUTANDO")

    conexion = conectar()

    usuario_repository = UsuarioRepository(conexion)
    cliente_repository = ClienteRepository(conexion)

    usuario_service = UsuarioService(usuario_repository)
    cliente_service = ClienteService(cliente_repository)

    def abrir_menu():
        menu = MenuWindow(cliente_service)
        menu.mostrar()

    login = LoginWindow(
        usuario_service,
        abrir_menu
    )

    login.mostrar()


if __name__ == "__main__":
    iniciar_sistema()
