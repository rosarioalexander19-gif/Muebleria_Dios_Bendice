from model.cliente import Cliente


class ClienteRepository:

    def __init__(self, conexion):
        self.conexion = conexion

    def crear(self, cliente):
        cursor = self.conexion.cursor()

        sql = """
            INSERT INTO clientes
            (nombre, apellido, cedula, telefono, direccion, correo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            cliente.nombre,
            cliente.apellido,
            cliente.cedula,
            cliente.telefono,
            cliente.direccion,
            cliente.correo
        )

        cursor.execute(sql, valores)
        self.conexion.commit()

        cliente.id_cliente = cursor.lastrowid

        cursor.close()

        return cliente

    def obtener_todos(self):
        cursor = self.conexion.cursor()

        cursor.execute("SELECT * FROM clientes")

        filas = cursor.fetchall()

        cursor.close()

        clientes = []

        for fila in filas:
            cliente = Cliente(
                id_cliente=fila[0],
                nombre=fila[1],
                apellido=fila[2],
                cedula=fila[3],
                telefono=fila[4],
                direccion=fila[5],
                correo=fila[6]
            )

            clientes.append(cliente)

        return clientes

    def buscar_por_id(self, id_cliente):
        cursor = self.conexion.cursor()

        sql = """
            SELECT * FROM clientes
            WHERE id_cliente = %s
        """

        cursor.execute(sql, (id_cliente,))

        fila = cursor.fetchone()

        cursor.close()

        if fila:
            return Cliente(
                id_cliente=fila[0],
                nombre=fila[1],
                apellido=fila[2],
                cedula=fila[3],
                telefono=fila[4],
                direccion=fila[5],
                correo=fila[6]
            )

        return None

    def actualizar(self, cliente):
        cursor = self.conexion.cursor()

        sql = """
            UPDATE clientes
            SET nombre = %s,
                apellido = %s,
                cedula = %s,
                telefono = %s,
                direccion = %s,
                correo = %s
            WHERE id_cliente = %s
        """

        valores = (
            cliente.nombre,
            cliente.apellido,
            cliente.cedula,
            cliente.telefono,
            cliente.direccion,
            cliente.correo,
            cliente.id_cliente
        )

        cursor.execute(sql, valores)

        self.conexion.commit()

        cursor.close()

    def eliminar(self, id_cliente):
        cursor = self.conexion.cursor()

        sql = """
            DELETE FROM clientes
            WHERE id_cliente = %s
        """

        cursor.execute(sql, (id_cliente,))

        self.conexion.commit()

        cursor.close()
