conexion_bd = (#tuplas inmutables
    "127.0.0.1",#elemento 0
    "root",#elemento 1
    "qwerty",#elemento 2
    "nomina",#elemento 3
)
print("\n")
print("Conexión típica:", type(conexion_bd), conexion_bd )

conexion_completa = (
    conexion_bd,
    "3307",
    "10"
)
print(
    "\nConexión con parámetros adicionales:",
    type(conexion_completa),
    "\n"
)
for i in range(0, len(conexion_completa)):#funciòn range, len
        if i >= 0:
         print(i, conexion_completa[i])
         
print("\n")

print("IP de la BD:", conexion_completa[0][0])
print("Usuario de la BD:", conexion_completa[0][1])
print("Contraseña de la BD:", conexion_completa[0][2])
print("Nombre de la BD:", conexion_completa[0][3])
print("Puerto de conexión:", conexion_completa[1])
print("Tiempo de espera en conexion:", conexion_completa[2])

print("\n")


