import tkinter as tk
from tkinter import ttk, messagebox

from service.reporte_service import (
    obtener_reporte_ventas,
    obtener_reporte_cuentas_por_cobrar
)


def abrir_ventana_reportes():
    ventana = tk.Tk()
    ventana.title("Reportes")
    ventana.geometry("950x550")

    tk.Label(
        ventana,
        text="Reportes de la Mueblería",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # -------------------------
    # REPORTE DE VENTAS
    # -------------------------

    tk.Label(
        ventana,
        text="Reporte de Ventas",
        font=("Arial", 12, "bold")
    ).pack()

    tabla_ventas = ttk.Treeview(
        ventana,
        columns=(
            "factura",
            "fecha",
            "nombre",
            "apellido",
            "pago",
            "total"
        ),
        show="headings"
    )

    columnas_ventas = {
        "factura": "Factura",
        "fecha": "Fecha",
        "nombre": "Nombre",
        "apellido": "Apellido",
        "pago": "Tipo de Pago",
        "total": "Total"
    }

    for columna, titulo in columnas_ventas.items():
        tabla_ventas.heading(columna, text=titulo)

    tabla_ventas.pack(
        fill="x",
        padx=10,
        pady=10
    )

    # -------------------------
    # REPORTE CUENTAS POR COBRAR
    # -------------------------

    tk.Label(
        ventana,
        text="Cuentas por Cobrar",
        font=("Arial", 12, "bold")
    ).pack()

    tabla_cuentas = ttk.Treeview(
        ventana,
        columns=(
            "cuenta",
            "factura",
            "nombre",
            "apellido",
            "vencimiento",
            "monto",
            "saldo",
            "estado"
        ),
        show="headings"
    )

    columnas_cuentas = {
        "cuenta": "Cuenta",
        "factura": "Factura",
        "nombre": "Nombre",
        "apellido": "Apellido",
        "vencimiento": "Vencimiento",
        "monto": "Monto",
        "saldo": "Saldo",
        "estado": "Estado"
    }

    for columna, titulo in columnas_cuentas.items():
        tabla_cuentas.heading(columna, text=titulo)

    tabla_cuentas.pack(
        fill="x",
        padx=10,
        pady=10
    )

    # -------------------------
    # FUNCIONES
    # -------------------------

    def cargar_ventas():
        try:
            for fila in tabla_ventas.get_children():
                tabla_ventas.delete(fila)

            resultados = obtener_reporte_ventas()

            for venta in resultados:
                tabla_ventas.insert(
                    "",
                    "end",
                    values=venta
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo cargar el reporte de ventas:\n{e}"
            )

    def cargar_cuentas():
        try:
            for fila in tabla_cuentas.get_children():
                tabla_cuentas.delete(fila)

            resultados = obtener_reporte_cuentas_por_cobrar()

            for cuenta in resultados:
                tabla_cuentas.insert(
                    "",
                    "end",
                    values=cuenta
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo cargar el reporte de cuentas:\n{e}"
            )

    def cargar_reportes():
        cargar_ventas()
        cargar_cuentas()

    # -------------------------
    # BOTÓN
    # -------------------------

    tk.Button(
        ventana,
        text="Actualizar Reportes",
        command=cargar_reportes
    ).pack(pady=10)

    cargar_reportes()

    ventana.mainloop()


if __name__ == "__main__":
    abrir_ventana_reportes()
