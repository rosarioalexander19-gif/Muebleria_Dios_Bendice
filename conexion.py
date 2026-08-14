import mysql.connector


def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu contraseña",
        database="muebleria_dios_bendice"
    )

    return conexion
