
from model.usuario import Usuario


class UsuarioRepository:

    def __init__(self, conexion):
        self.conexion = conexion

    def crear(self, usuario):
        cursor = self.conexion.cursor()

        sql = """
            INSERT INTO usuarios
            (nombre, usuario, password)
            VALUES (%s, %s, %s)
        """

        valores = (
            usuario.nombre,
            usuario.usuario,
            usuario.password
        )

        cursor.execute(sql, valores)
        self.conexion.commit()

        usuario.id_usuario = cursor.lastrowid

        cursor.close()

        return usuario

    def obtener_todos(self):
        cursor = self.conexion.cursor()

        sql = "SELECT * FROM usuarios"

        cursor.execute(sql)

        filas = cursor.fetchall()

        cursor.close()

        usuarios = []

        for fila in filas:
            usuario = Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3]
            )

            usuarios.append(usuario)

        return usuarios

    def buscar_por_usuario(self, nombre_usuario):
        cursor = self.conexion.cursor()

        sql = """
            SELECT * FROM usuarios
            WHERE usuario = %s
        """

        cursor.execute(sql, (nombre_usuario,))

        fila = cursor.fetchone()

        cursor.close()

        if fila:
            return Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3]
            )

        return None

    def actualizar(self, usuario):
        cursor = self.conexion.cursor()

        sql = """
            UPDATE usuarios
            SET nombre = %s,
                usuario = %s,
                password = %s
            WHERE id_usuario = %s
        """

        valores = (
            usuario.nombre,
            usuario.usuario,
            usuario.password,
            usuario.id_usuario
        )

        cursor.execute(sql, valores)

        self.conexion.commit()

        cursor.close()

    def eliminar(self, id_usuario):
        cursor = self.conexion.cursor()

        sql = """
            DELETE FROM usuarios
            WHERE id_usuario = %s
        """

        cursor.execute(sql, (id_usuario,))

        self.conexion.commit()

        cursor.close()


