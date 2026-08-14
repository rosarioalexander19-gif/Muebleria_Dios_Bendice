import tkinter as tk

from ui.clientes import ClientesWindow
from ui.productos import abrir_ventana_productos
from ui.ventas import abrir_ventana_ventas
from ui.reportes import abrir_ventana_reportes


class MenuWindow:

    def __init__(self, cliente_service):

        self.cliente_service = cliente_service

        self.ventana = tk.Tk()
        self.ventana.title("Mueblería Dios Bendice")
        self.ventana.geometry("500x450")

        tk.Label(
            self.ventana,
            text="MUEBLERÍA DIOS BENDICE",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Label(
            self.ventana,
            text="MENÚ PRINCIPAL",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Button(
            self.ventana,
            text="Clientes",
            width=25,
            command=self.abrir_clientes
        ).pack(pady=8)

        tk.Button(
            self.ventana,
            text="Productos",
            width=25,
            command=abrir_ventana_productos
        ).pack(pady=8)

        tk.Button(
            self.ventana,
            text="Ventas",
            width=25,
            command=abrir_ventana_ventas
        ).pack(pady=8)

        tk.Button(
            self.ventana,
            text="Reportes",
            width=25,
            command=abrir_ventana_reportes
        ).pack(pady=8)

        tk.Button(
            self.ventana,
            text="Salir",
            width=25,
            command=self.ventana.destroy
        ).pack(pady=20)

    def abrir_clientes(self):
        ventana = ClientesWindow(self.cliente_service)
        ventana.mostrar()

    def mostrar(self):
        self.ventana.mainloop()
