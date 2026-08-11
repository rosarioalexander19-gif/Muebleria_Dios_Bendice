import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YAR075510",
        database="muebleria_dios_bendice"
    )

    if conexion.is_connected():
        print("CONEXION EXITOSA A MYSQL")
        print("Base de datos: muebleria_dios_bendice")

except mysql.connector.Error as error:
    print("ERROR DE CONEXION:", error)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexion cerrada.")