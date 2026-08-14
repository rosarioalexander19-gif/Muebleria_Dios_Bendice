from model.cliente import Cliente


class ClienteService:

    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository

    def crear_cliente(
        self,
        nombre,
        apellido,
        cedula,
        telefono,
        direccion,
        correo
    ):

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if not apellido:
            raise ValueError("El apellido es obligatorio.")

        if not cedula:
            raise ValueError("La cédula es obligatoria.")

        if not telefono:
            raise ValueError("El teléfono es obligatorio.")

        if not direccion:
            raise ValueError("La dirección es obligatoria.")

        if not correo:
            raise ValueError("El correo es obligatorio.")

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            telefono=telefono,
            direccion=direccion,
            correo=correo
        )

        return self.cliente_repository.crear(cliente)

    def obtener_clientes(self):
        return self.cliente_repository.obtener_todos()

    def obtener_cliente(self, id_cliente):
        return self.cliente_repository.buscar_por_id(id_cliente)

    def actualizar_cliente(self, cliente):
        self.cliente_repository.actualizar(cliente)

    def eliminar_cliente(self, id_cliente):
        self.cliente_repository.eliminar(id_cliente)
