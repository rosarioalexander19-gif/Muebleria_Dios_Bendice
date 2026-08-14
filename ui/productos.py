import tkinter as tk
from tkinter import ttk, messagebox

from service.producto_service import (
    guardar_producto,
    listar_productos,
    editar_producto,
    borrar_producto
)


def abrir_ventana_productos():

    ventana = tk.Tk()
    ventana.title("Productos")
    ventana.geometry("700x450")

    # -------------------------
    # TÍTULO
    # -------------------------

    tk.Label(
        ventana,
        text="GESTIÓN DE PRODUCTOS",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    # -------------------------
    # FORMULARIO
    # -------------------------

    formulario = tk.Frame(ventana)
    formulario.pack(pady=5)

    tk.Label(
        formulario,
        text="Código:"
    ).grid(row=0, column=0, padx=5, pady=5)

    entry_id = tk.Entry(
        formulario,
        width=30
    )
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(
        formulario,
        text="Nombre:"
    ).grid(row=1, column=0, padx=5, pady=5)

    entry_nombre = tk.Entry(
        formulario,
        width=30
    )
    entry_nombre.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(
        formulario,
        text="Precio:"
    ).grid(row=2, column=0, padx=5, pady=5)

    entry_precio = tk.Entry(
        formulario,
        width=30
    )
    entry_precio.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(
        formulario,
        text="Stock:"
    ).grid(row=3, column=0, padx=5, pady=5)

    entry_stock = tk.Entry(
        formulario,
        width=30
    )
    entry_stock.grid(row=3, column=1, padx=5, pady=5)

    # -------------------------
    # TABLA
    # -------------------------

    tabla = ttk.Treeview(
        ventana,
        columns=("id", "nombre", "precio", "stock"),
        show="headings"
    )

    tabla.heading(
        "id",
        text="ID"
    )

    tabla.heading(
        "nombre",
        text="Nombre"
    )

    tabla.heading(
        "precio",
        text="Precio"
    )

    tabla.heading(
        "stock",
        text="Stock"
    )

    tabla.column(
        "id",
        width=60,
        anchor="center"
    )

    tabla.column(
        "nombre",
        width=280
    )

    tabla.column(
        "precio",
        width=130,
        anchor="center"
    )

    tabla.column(
        "stock",
        width=100,
        anchor="center"
    )

    tabla.pack(
        fill=tk.BOTH,
        expand=True,
        padx=10,
        pady=10
    )

    # -------------------------
    # REFRESCAR TABLA
    # -------------------------

    def refrescar_tabla():

        for fila in tabla.get_children():
            tabla.delete(fila)

        productos = listar_productos()

        for producto in productos:

            tabla.insert(
                "",
                tk.END,
                values=(
                    producto.id_producto,
                    producto.nombre,
                    f"RD${producto.precio:.2f}",
                    producto.stock
                )
            )

    # -------------------------
    # SELECCIONAR PRODUCTO
    # -------------------------

    def seleccionar_producto(event):

        seleccion = tabla.selection()

        if not seleccion:
            return

        valores = tabla.item(
            seleccion[0],
            "values"
        )

        entry_id.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_stock.delete(0, tk.END)

        entry_id.insert(
            0,
            valores[0]
        )

        entry_nombre.insert(
            0,
            valores[1]
        )

        precio = valores[2].replace(
            "RD$",
            ""
        )

        entry_precio.insert(
            0,
            precio
        )

        entry_stock.insert(
            0,
            valores[3]
        )

    tabla.bind(
        "<ButtonRelease-1>",
        seleccionar_producto
    )

    # -------------------------
    # GUARDAR
    # -------------------------

    def guardar():

        try:

            guardar_producto(
                entry_nombre.get(),
                float(entry_precio.get()),
                int(entry_stock.get())
            )

            messagebox.showinfo(
                "Éxito",
                "Producto guardado correctamente."
            )

            limpiar()
            refrescar_tabla()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # -------------------------
    # EDITAR
    # -------------------------

    def editar():

        try:

            if not entry_id.get():
                raise ValueError(
                    "Seleccione un producto."
                )

            editar_producto(
                int(entry_id.get()),
                entry_nombre.get(),
                float(entry_precio.get()),
                int(entry_stock.get())
            )

            messagebox.showinfo(
                "Éxito",
                "Producto actualizado correctamente."
            )

            limpiar()
            refrescar_tabla()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # -------------------------
    # ELIMINAR
    # -------------------------

    def eliminar():

        try:

            if not entry_id.get():
                raise ValueError(
                    "Seleccione un producto."
                )

            confirmar = messagebox.askyesno(
                "Confirmar",
                "¿Está seguro de eliminar este producto?"
            )

            if not confirmar:
                return

            borrar_producto(
                int(entry_id.get())
            )

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado correctamente."
            )

            limpiar()
            refrescar_tabla()

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # -------------------------
    # LIMPIAR
    # -------------------------

    def limpiar():

        entry_id.delete(
            0,
            tk.END
        )

        entry_nombre.delete(
            0,
            tk.END
        )

        entry_precio.delete(
            0,
            tk.END
        )

        entry_stock.delete(
            0,
            tk.END
        )

    # -------------------------
    # BOTONES
    # -------------------------

    botones = tk.Frame(ventana)
    botones.pack(pady=5)

    tk.Button(
        botones,
        text="Guardar",
        width=12,
        command=guardar
    ).pack(
        side=tk.LEFT,
        padx=5
    )

    tk.Button(
        botones,
        text="Editar",
        width=12,
        command=editar
    ).pack(
        side=tk.LEFT,
        padx=5
    )

    tk.Button(
        botones,
        text="Eliminar",
        width=12,
        command=eliminar
    ).pack(
        side=tk.LEFT,
        padx=5
    )

    tk.Button(
        botones,
        text="Limpiar",
        width=12,
        command=limpiar
    ).pack(
        side=tk.LEFT,
        padx=5
    )

    # -------------------------
    # CARGAR PRODUCTOS
    # -------------------------

    refrescar_tabla()

    ventana.mainloop()


if __name__ == "__main__":
    abrir_ventana_productos()
