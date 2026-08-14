import tkinter as tk
from tkinter import ttk, messagebox


class ClientesWindow:

    def __init__(self, cliente_service):

        self.cliente_service = cliente_service

        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("1000x600")

        tk.Label(
            self.ventana,
            text="GESTIÓN DE CLIENTES",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        formulario = tk.Frame(self.ventana)
        formulario.pack(pady=10)

        # Nombre
        tk.Label(formulario, text="Nombre:").grid(
            row=0, column=0, padx=5, pady=5
        )

        self.nombre = tk.Entry(formulario, width=30)
        self.nombre.grid(row=0, column=1)

        # Apellido
        tk.Label(formulario, text="Apellido:").grid(
            row=1, column=0, padx=5, pady=5
        )

        self.apellido = tk.Entry(formulario, width=30)
        self.apellido.grid(row=1, column=1)

        # Cédula
        tk.Label(formulario, text="Cédula:").grid(
            row=2, column=0, padx=5, pady=5
        )

        self.cedula = tk.Entry(formulario, width=30)
        self.cedula.grid(row=2, column=1)

        # Teléfono
        tk.Label(formulario, text="Teléfono:").grid(
            row=3, column=0, padx=5, pady=5
        )

        self.telefono = tk.Entry(formulario, width=30)
        self.telefono.grid(row=3, column=1)

        # Dirección
        tk.Label(formulario, text="Dirección:").grid(
            row=4, column=0, padx=5, pady=5
        )

        self.direccion = tk.Entry(formulario, width=30)
        self.direccion.grid(row=4, column=1)

        # Correo
        tk.Label(formulario, text="Correo:").grid(
            row=5, column=0, padx=5, pady=5
        )

        self.correo = tk.Entry(formulario, width=30)
        self.correo.grid(row=5, column=1)

        # Botones
        botones = tk.Frame(self.ventana)
        botones.pack(pady=10)

        tk.Button(
            botones,
            text="Crear",
            command=self.crear_cliente
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_cliente
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_cliente
        ).pack(side=tk.LEFT, padx=5)

        # Tabla
        columnas = (
            "id",
            "nombre",
            "apellido",
            "cedula",
            "telefono",
            "direccion",
            "correo"
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellido", text="Apellido")
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("direccion", text="Dirección")
        self.tabla.heading("correo", text="Correo")

        self.tabla.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        self.tabla.bind(
            "<ButtonRelease-1>",
            self.seleccionar_cliente
        )

        self.cargar_clientes()

    def cargar_clientes(self):

        for item in self.tabla.get_children():
            self.tabla.delete(item)

        clientes = self.cliente_service.obtener_clientes()

        for cliente in clientes:
            self.tabla.insert(
                "",
                tk.END,
                values=(
                    cliente.id_cliente,
                    cliente.nombre,
                    cliente.apellido,
                    cliente.cedula,
                    cliente.telefono,
                    cliente.direccion,
                    cliente.correo
                )
            )

    def crear_cliente(self):

        try:

            self.cliente_service.crear_cliente(
                self.nombre.get(),
                self.apellido.get(),
                self.cedula.get(),
                self.telefono.get(),
                self.direccion.get(),
                self.correo.get()
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente creado correctamente."
            )

            self.limpiar()
            self.cargar_clientes()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def seleccionar_cliente(self, evento):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        self.limpiar()

        self.nombre.insert(0, valores[1])
        self.apellido.insert(0, valores[2])
        self.cedula.insert(0, valores[3])
        self.telefono.insert(0, valores[4])
        self.direccion.insert(0, valores[5])
        self.correo.insert(0, valores[6])

        self.id_seleccionado = valores[0]

    def actualizar_cliente(self):

        if not hasattr(self, "id_seleccionado"):
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un cliente."
            )
            return

        cliente = self.cliente_service.obtener_cliente(
            self.id_seleccionado
        )

        cliente.nombre = self.nombre.get()
        cliente.apellido = self.apellido.get()
        cliente.cedula = self.cedula.get()
        cliente.telefono = self.telefono.get()
        cliente.direccion = self.direccion.get()
        cliente.correo = self.correo.get()

        self.cliente_service.actualizar_cliente(cliente)

        messagebox.showinfo(
            "Éxito",
            "Cliente actualizado correctamente."
        )

        self.limpiar()
        self.cargar_clientes()

    def eliminar_cliente(self):

        if not hasattr(self, "id_seleccionado"):
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un cliente."
            )
            return

        self.cliente_service.eliminar_cliente(
            self.id_seleccionado
        )

        messagebox.showinfo(
            "Éxito",
            "Cliente eliminado correctamente."
        )

        self.limpiar()
        self.cargar_clientes()

    def limpiar(self):

        self.nombre.delete(0, tk.END)
        self.apellido.delete(0, tk.END)
        self.cedula.delete(0, tk.END)
        self.telefono.delete(0, tk.END)
        self.direccion.delete(0, tk.END)
        self.correo.delete(0, tk.END)

        if hasattr(self, "id_seleccionado"):
            del self.id_seleccionado

    def mostrar(self):
        self.ventana.mainloop()
