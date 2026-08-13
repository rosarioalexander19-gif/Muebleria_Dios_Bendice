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
    ventana.geometry("500x450")

    tk.Label(ventana, text="Código:").pack()
    entry_id = tk.Entry(ventana)
    entry_id.pack()

    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Categoría:").pack()
    entry_categoria = tk.Entry(ventana)
    entry_categoria.pack()

    tk.Label(ventana, text="Precio:").pack()
    entry_precio = tk.Entry(ventana)
    entry_precio.pack()

    tk.Label(ventana, text="Stock:").pack()
    entry_stock = tk.Entry(ventana)
    entry_stock.pack()

    tabla = ttk.Treeview(ventana, columns=("id", "nombre", "categoria", "precio", "stock"), show="headings")
    for col in ("id", "nombre", "categoria", "precio", "stock"):
        tabla.heading(col, text=col)
    tabla.pack(pady=10)

    def refrescar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        for p in listar_productos():
            tabla.insert("", "end", values=p)

    def guardar():
        try:
            guardar_producto(
                entry_nombre.get(),
                entry_categoria.get(),
                float(entry_precio.get()),
                int(entry_stock.get())
            )
            messagebox.showinfo("Éxito", "Producto guardado")
            refrescar_tabla()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def editar():
        try:
            editar_producto(
                int(entry_id.get()),
                entry_nombre.get(),
                entry_categoria.get(),
                float(entry_precio.get()),
                int(entry_stock.get())
            )
            messagebox.showinfo("Éxito", "Producto actualizado")
            refrescar_tabla()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar():
        try:
            borrar_producto(int(entry_id.get()))
            messagebox.showinfo("Éxito", "Producto eliminado")
            refrescar_tabla()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Guardar", command=guardar).pack(side="left", padx=10, pady=10)
    tk.Button(ventana, text="Editar", command=editar).pack(side="left", padx=10, pady=10)
    tk.Button(ventana, text="Eliminar", command=eliminar).pack(side="left", padx=10, pady=10)

    refrescar_tabla()
    ventana.mainloop()

if __name__ == "__main__":
    abrir_ventana_productos()
