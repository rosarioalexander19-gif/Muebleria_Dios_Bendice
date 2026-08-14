import tkinter as tk
from tkinter import messagebox


class LoginWindow:

    def __init__(self, usuario_service, abrir_menu):
        self.usuario_service = usuario_service
        self.abrir_menu = abrir_menu

        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("400x300")

        tk.Label(
            self.ventana,
            text="INICIO DE SESIÓN",
            font=("Arial", 18)
        ).pack(pady=20)

        tk.Label(
            self.ventana,
            text="Usuario:"
        ).pack()

        self.entrada_usuario = tk.Entry(self.ventana)
        self.entrada_usuario.pack(pady=5)

        tk.Label(
            self.ventana,
            text="Contraseña:"
        ).pack()

        self.entrada_password = tk.Entry(
            self.ventana,
            show="*"
        )
        self.entrada_password.pack(pady=5)

        tk.Button(
            self.ventana,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        ).pack(pady=20)

    def iniciar_sesion(self):

        usuario = self.entrada_usuario.get()
        password = self.entrada_password.get()

        resultado = self.usuario_service.iniciar_sesion(
            usuario,
            password
        )

        if resultado:

            messagebox.showinfo(
                "Éxito",
                "Inicio de sesión correcto."
            )

            self.ventana.destroy()

            self.abrir_menu()

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )

    def mostrar(self):
        self.ventana.mainloop()

