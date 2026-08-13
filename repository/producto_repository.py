from repository.conexion import conectar

def insertar_producto(producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO producto (nombre, categoria, precio, stock) VALUES (%s, %s, %s, %s)",
        (producto.nombre, producto.categoria, producto.precio, producto.stock)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def actualizar_producto(producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE producto SET nombre=%s, categoria=%s, precio=%s, stock=%s WHERE id_producto=%s",
        (producto.nombre, producto.categoria, producto.precio, producto.stock, producto.id_producto)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto=%s", (id_producto,))
    conexion.commit()
    cursor.close()
    conexion.close()
