import mysql.connector


def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YAR075510",
        database="muebleria_dios_bendice"
    )

    return conexion