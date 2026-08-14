from model.producto import Producto
from repository.producto_repository import (
    insertar_producto,
    obtener_productos,
    actualizar_producto,
    eliminar_producto
)


def guardar_producto(nombre, precio, stock):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    producto = Producto(
        nombre=nombre,
        precio=precio,
        stock=stock
    )

    insertar_producto(producto)


def listar_productos():
    return obtener_productos()


def editar_producto(id_producto, nombre, precio, stock):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor a 0")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo")

    producto = Producto(
        id_producto=id_producto,
        nombre=nombre,
        precio=precio,
        stock=stock
    )

    actualizar_producto(producto)


def borrar_producto(id_producto):
    eliminar_producto(id_producto)
