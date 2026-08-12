
from model.cliente import Cliente


class ClienteRepository:

    def __init__(self, conexion):
        self.conexion = conexion

    def crear(self, cliente):
        cursor = self.conexion.cursor()

        sql = """
            INSERT INTO clientes
            (nombre_completo, cedula, telefono, direccion)
            VALUES (%s, %s, %s, %s)
        """

        valores = (
            cliente.nombre_completo,
            cliente.cedula,
            cliente.telefono,
            cliente.direccion
        )

        cursor.execute(sql, valores)

        self.conexion.commit()

        cliente.id_cliente = cursor.lastrowid

        cursor.close()

        return cliente

    def obtener_todos(self):
        cursor = self.conexion.cursor()

        sql = "SELECT * FROM clientes"

        cursor.execute(sql)

        filas = cursor.fetchall()

        cursor.close()

        clientes = []

        for fila in filas:
            cliente = Cliente(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4]
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
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4]
            )

        return None

    def actualizar(self, cliente):
        cursor = self.conexion.cursor()

        sql = """
            UPDATE clientes
            SET nombre_completo = %s,
                cedula = %s,
                telefono = %s,
                direccion = %s
            WHERE id_cliente = %s
        """

        valores = (
            cliente.nombre_completo,
            cliente.cedula,
            cliente.telefono,
            cliente.direccion,
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


