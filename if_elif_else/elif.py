#El valor es ingresado en la variable '''numero'''
numero = int(input("\nIngresa un número entero, por favor: "))
#convierte el valor ingresado a número enteros
#lee el valor ingresado por la entrada estándar

if numero < 0:
    numero = 0
    print("El número ingresado es negativo cambiado a cero.\n")
elif numero == 0:
    print("El número ingresado es 0. \n")
elif numero == 1:
    print("El número ingresado es 1. \n")
else:
    print("El número ingresado es mayor que uno")