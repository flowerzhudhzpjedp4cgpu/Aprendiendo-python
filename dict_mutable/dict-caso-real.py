secuencia = (
    "nombres",
    "apellidos",
    "cedula",
    "fecha_nacimiento",
    "lugar_nacimiento",
    "nacionalidad",
    "estado_civil"          
)

versiones = dict.fromkeys(secuencia)

print("\n\n Inscripción de Curso:")
print("====================")
print("\n Datos de participante")
print("---------------------------")
print("Keys : %s" % str(versiones))

#operaciones con tipo diccionario con funciones propias
print("\nClaves de diccionario:",versiones.keys())
print("\nValores de diccionario:",versiones.values())
print("\nElementos de diccionario:",versiones.items())
print("\n")

try:#bloque de código a comprobar
    cedula = int(input('Teclear cedula de identidad:'))#entrada de entero
    
    nombre = input('Teclear nombre:')#entrada  de cadena
    apellido = input('Teclear apellido:')#entrada de cadena
    fecha_nacimiento = input('Teclear fecha de nacimiento:')#entrada de cadena

    versiones["cedula"] = cedula#asignar valor a clave - mutable
    versiones["nombres"] = nombre
    versiones["apellidos"] = apellido
    versiones["fecha_nacimiento"] = fecha_nacimiento

    print("\n")

    #operador integrado in
    for key, value in iter(versiones.items()):
        print(f"Clave: {key}, posee el valor: {value}")
    print("\n")
    print("Cédula de identidad: ", versiones["cedula"])
    print("Nombre completo: ", versiones["nombres"] + " con apellido " + versiones["apellidos"])

    import datetime, locale, os

    print(
    "Fecha de nacimiento:",
    datetime.datetime.strftime(
        datetime.datetime.strptime(versiones["fecha_nacimiento"], "%d/%m/%Y"),
        "%d de %B de %Y",
    )
    )
except:#bloque para captura de error
    print('error, debe ser números')
    
