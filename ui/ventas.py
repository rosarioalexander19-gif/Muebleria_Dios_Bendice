import tkinter as tk
from tkinter import ttk, messagebox

from model.detalle_factura import DetalleFactura
from service.venta_service import (
    calcular_subtotal,
    guardar_factura
)


def abrir_ventana_ventas():

    ventana = tk.Tk()
    ventana.title("Ventas")
    ventana.geometry("850x650")

    # =========================
    # TÍTULO
    # =========================

    tk.Label(
        ventana,
        text="REGISTRO DE VENTAS",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    # =========================
    # DATOS DE LA FACTURA
    # =========================

    formulario_factura = tk.LabelFrame(
        ventana,
        text="Datos de la factura",
        padx=10,
        pady=10
    )

    formulario_factura.pack(
        fill="x",
        padx=15,
        pady=5
    )

    tk.Label(
        formulario_factura,
        text="ID Cliente:"
    ).grid(row=0, column=0, padx=5, pady=5)

    entry_cliente = tk.Entry(
        formulario_factura,
        width=20
    )
    entry_cliente.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(
        formulario_factura,
        text="ID Usuario:"
    ).grid(row=0, column=2, padx=5, pady=5)

    entry_usuario = tk.Entry(
        formulario_factura,
        width=20
    )
    entry_usuario.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(
        formulario_factura,
        text="Tipo de pago:"
    ).grid(row=1, column=0, padx=5, pady=5)

    combo_pago = ttk.Combobox(
        formulario_factura,
        values=("Contado", "Credito"),
        state="readonly",
        width=17
    )
    combo_pago.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(
        formulario_factura,
        text="Plazo (días):"
    ).grid(row=1, column=2, padx=5, pady=5)

    entry_plazo = tk.Entry(
        formulario_factura,
        width=20
    )
    entry_plazo.grid(row=1, column=3, padx=5, pady=5)

    # =========================
    # DATOS DEL PRODUCTO
    # =========================

    formulario_producto = tk.LabelFrame(
        ventana,
        text="Producto",
        padx=10,
        pady=10
    )

    formulario_producto.pack(
        fill="x",
        padx=15,
        pady=5
    )

    tk.Label(
        formulario_producto,
        text="ID Producto:"
    ).grid(row=0, column=0, padx=5, pady=5)

    entry_producto = tk.Entry(
        formulario_producto,
        width=20
    )
    entry_producto.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(
        formulario_producto,
        text="Cantidad:"
    ).grid(row=0, column=2, padx=5, pady=5)

    entry_cantidad = tk.Entry(
        formulario_producto,
        width=20
    )
    entry_cantidad.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(
        formulario_producto,
        text="Precio:"
    ).grid(row=1, column=0, padx=5, pady=5)

    entry_precio = tk.Entry(
        formulario_producto,
        width=20
    )
    entry_precio.grid(row=1, column=1, padx=5, pady=5)

    # =========================
    # TABLA DE PRODUCTOS
    # =========================

    tabla = ttk.Treeview(
        ventana,
        columns=(
            "producto",
            "cantidad",
            "precio",
            "subtotal"
        ),
        show="headings"
    )

    tabla.heading(
        "producto",
        text="ID Producto"
    )

    tabla.heading(
        "cantidad",
        text="Cantidad"
    )

    tabla.heading(
        "precio",
        text="Precio"
    )

    tabla.heading(
        "subtotal",
        text="Subtotal"
    )

    tabla.column(
        "producto",
        width=120,
        anchor="center"
    )

    tabla.column(
        "cantidad",
        width=120,
        anchor="center"
    )

    tabla.column(
        "precio",
        width=150,
        anchor="center"
    )

    tabla.column(
        "subtotal",
        width=150,
        anchor="center"
    )

    tabla.pack(
        fill="x",
        padx=15,
        pady=15
    )

    # Lista donde se almacenan los detalles
    detalles = []

    # =========================
    # TOTAL
    # =========================

    label_total = tk.Label(
        ventana,
        text="Total: RD$0.00",
        font=("Arial", 16, "bold")
    )

    label_total.pack(pady=5)

    # =========================
    # ACTUALIZAR TOTAL
    # =========================

    def actualizar_total():

        total = 0

        for detalle in detalles:
            total += detalle.subtotal

        label_total.config(
            text=f"Total: RD${total:.2f}"
        )

    # =========================
    # AGREGAR PRODUCTO
    # =========================

    def agregar_producto():

        try:

            id_producto = int(
                entry_producto.get()
            )

            cantidad = int(
                entry_cantidad.get()
            )

            precio = float(
                entry_precio.get()
            )

            subtotal = calcular_subtotal(
                cantidad,
                precio
            )

            detalle = DetalleFactura(
                id_producto=id_producto,
                cantidad=cantidad,
                precio=precio,
                subtotal=subtotal
            )

            detalles.append(detalle)

            tabla.insert(
                "",
                tk.END,
                values=(
                    id_producto,
                    cantidad,
                    f"RD${precio:.2f}",
                    f"RD${subtotal:.2f}"
                )
            )

            actualizar_total()

            entry_producto.delete(
                0,
                tk.END
            )

            entry_cantidad.delete(
                0,
                tk.END
            )

            entry_precio.delete(
                0,
                tk.END
            )

            messagebox.showinfo(
                "Producto agregado",
                "El producto fue agregado a la venta."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Ocurrió un error:\n{error}"
            )

    # =========================
    # REGISTRAR VENTA
    # =========================

    def registrar_venta():

        try:

            if not entry_cliente.get():
                raise ValueError(
                    "Debe indicar el ID del cliente."
                )

            if not entry_usuario.get():
                raise ValueError(
                    "Debe indicar el ID del usuario."
                )

            if not detalles:
                raise ValueError(
                    "Debe agregar al menos un producto."
                )

            id_cliente = int(
                entry_cliente.get()
            )

            id_usuario = int(
                entry_usuario.get()
            )

            tipo_pago = combo_pago.get()

            if not tipo_pago:
                raise ValueError(
                    "Debe seleccionar un tipo de pago."
                )

            plazo_texto = entry_plazo.get()

            if plazo_texto:
                plazo = int(plazo_texto)
            else:
                plazo = None

            factura = guardar_factura(
                id_cliente,
                id_usuario,
                tipo_pago,
                plazo,
                detalles
            )

            messagebox.showinfo(
                "Venta registrada",
                f"Venta registrada correctamente.\n\n"
                f"Factura #{factura.id_factura}\n"
                f"Total: RD${factura.total:.2f}"
            )

            detalles.clear()

            for fila in tabla.get_children():
                tabla.delete(fila)

            actualizar_total()

            entry_cliente.delete(
                0,
                tk.END
            )

            entry_usuario.delete(
                0,
                tk.END
            )

            combo_pago.set("")

            entry_plazo.delete(
                0,
                tk.END
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudo registrar la venta:\n{error}"
            )

    # =========================
    # BOTONES
    # =========================

    tk.Button(
        ventana,
        text="Agregar producto",
        width=20,
        command=agregar_producto
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Registrar venta",
        width=20,
        command=registrar_venta
    ).pack(pady=10)

    # =========================
    # INICIAR
    # =========================

    ventana.mainloop()


if __name__ == "__main__":
    abrir_ventana_ventas()
