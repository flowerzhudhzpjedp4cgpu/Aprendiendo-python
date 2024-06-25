#define una relación uno a uno entre claves y valores.
diccionario = {#el diccionario pueden ser creados colocando una lista separada por coma de pares
    "clave1" : 234,
    "clave2" : True,
    "clave3" : "Valor 1",
    "clave4" : [1,2,3,4],#class 'list'
}

print(diccionario, type(diccionario))
#acceder a los valores del diccionario usando cada su clave
print(diccionario["clave1"])
print(diccionario["clave2"])
print(diccionario["clave3"])
print(diccionario["clave4"])
#almacenar los diversos tipos de datos integrados en Python
#usando la función Type()
print(type(diccionario["clave1"]))
print(type(diccionario["clave2"]))
print(type(diccionario["clave3"]))
print(type(diccionario["clave4"]))

#operaciones
#acceder a valor de  clave
versiones = {"python": 3.11, "zope": 5.2, "plone": 6.0, "django": 4.2}
versiones2 = {"python": 3.11, "zope": 5.2, "plone": None}
versiones2["plone"]
versiones2["plone"] = 6.0#asignar valor a clave - mutable
print(versiones["zope"])
print(versiones2["plone"])#su clave

#Iteración in - operador integrado in
versiones3 = dict(python=None, zope=None, plone=None, django=None)
print(versiones3)

key = input("Teclear key:")

if key in versiones3:#True
    
    modificar = input("Lo deseas modificar:")
    
    mayusc = modificar.upper()
    minusc = modificar.lower()
    
    if mayusc == "SI":    
        value = input("Teclear value?")
        versiones3[key] = value
        print(versiones3)
        versiones3.clear()
        #este método devuelve una copia superficial del tipo de diccionario
        versiones2 = versiones3.copy()
        versiones3 == versiones2 #true
        #este método crea un nuevo diccionario con claves a partir de un tipo de dato secuencia. 
        #el valor de value por defecto es el tipo None
        secuencia = ("python", "zope", "plone")#tipo de dato secuencia
        versiones = dict.fromkeys(secuencia)
        print("Nuevo Diccionario : %s" %str(versiones))
        
    elif minusc == "no":
        print("OK.")
        
    else: 
        print("Error...")

else:#False
    print("Error...")