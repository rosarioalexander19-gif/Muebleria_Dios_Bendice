from model.usuario import Usuario


class UsuarioRepository:

    def __init__(self, conexion):
        self.conexion = conexion

    def crear(self, usuario):
        cursor = self.conexion.cursor()

        sql = """
            INSERT INTO usuarios
            (nombre_usuario, `contrase├▒a`, rol, estado)
            VALUES (%s, %s, %s, %s)
        """

        valores = (
            usuario.nombre_usuario,
            usuario.contrasena,
            usuario.rol,
            usuario.estado
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
                id_usuario=fila[0],
                nombre_usuario=fila[1],
                contrasena=fila[2],
                rol=fila[3],
                estado=fila[4]
            )

            usuarios.append(usuario)

        return usuarios

    def buscar_por_usuario(self, nombre_usuario):
        cursor = self.conexion.cursor()

        sql = """
            SELECT * FROM usuarios
            WHERE nombre_usuario = %s
        """

        cursor.execute(sql, (nombre_usuario,))

        fila = cursor.fetchone()

        cursor.close()

        if fila:
            return Usuario(
                id_usuario=fila[0],
                nombre_usuario=fila[1],
                contrasena=fila[2],
                rol=fila[3],
                estado=fila[4]
            )

        return None

    def actualizar(self, usuario):
        cursor = self.conexion.cursor()

        sql = """
            UPDATE usuarios
            SET nombre_usuario = %s,
                `contrase├▒a` = %s,
                rol = %s,
                estado = %s
            WHERE id_usuario = %s
        """

        valores = (
            usuario.nombre_usuario,
            usuario.contrasena,
            usuario.rol,
            usuario.estado,
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
