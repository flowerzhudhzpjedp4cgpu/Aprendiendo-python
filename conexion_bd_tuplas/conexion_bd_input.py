nombre = input('Teclear nombre?\n')
bienvenida = input(f'Bienvenido {nombre} ¿Tienes problemas con la BD?\n')
mayusc = bienvenida.upper()
minusc = bienvenida.lower()

if mayusc == "SI":
    print(type(mayusc))
    
    conexion_bd = (
        "127.0.0.1",
        "root",
        "qwerty",
        "nomina"
    )
    print("Conexión típica: ", type(conexion_bd), conexion_bd)
    print("nomina ->",conexion_bd.count("nomina"))
    
    conexion_completa = (
        conexion_bd,
        "3307",
        "10"
    )
    print(
        "\Conexión  con parámetros  adicionales:",
         type(conexion_completa),        
        "\n"
    )
    print("Tuplas index",conexion_completa.index(conexion_bd))
    for i in range(0, len(conexion_completa)):
        if i >= 0:
            print(i, conexion_completa[i])
            
    print("\n")
    
    print("IP de la BD:", conexion_completa[0][0])
    print("Usuario de la BD:", conexion_completa[0][1])
    print("Contraseña de la BD:", conexion_completa[0][2])
    print("Nombre de la BD:", conexion_completa[0][3])
    print("Puerto de conexión:", conexion_completa[1])
    print("Tiempo de espera en conexión:", conexion_completa[2])
    
    
elif minusc == "no":
    print(type(minusc))
else:
    print("ERROR...")


    
    


    

    
