#tipos de dato compuestos

#creando una lista (se puede modificar)
lista = ["Yung Lion","Soy Cristian", True, 1.85]

#creando una tupla (no pueden modificar)
tupla = ("Yung Lion","Soy Cristian", True, 1.85)

#esto es válido 
lista[3] = "Maquinola"

#este no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a los elementos por indice, no almacena datos duplicados)
conjunto = {"Yung Lion", "Soy Cristian", True, 1.85, "Yung Lion" } # + "Soy Cristian"

#print(conjunto[3]) -> no puede acceder al 

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Yung Lion",
    'canal' : "Soy Cristian",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "Soy Cristian"   
}
print(lista[3])
print(diccionario['altura'] + 2)