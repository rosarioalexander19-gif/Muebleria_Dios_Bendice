
class Usuario:
    def __init__(self, id_usuario=None, nombre="", usuario="", password=""):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.password = password

    def __str__(self):
        return f"{self.id_usuario} - {self.nombre} - {self.usuario}"


