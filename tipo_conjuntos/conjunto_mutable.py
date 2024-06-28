#Los objetos de tipo conjunto mutable y conjunto inmutable integra una serie de métodos
set_mutable1 = set([4,3,11,7,5,2,1,4])
set_mutable2 = set([11,5,9,2,4,8])
print(set_mutable1)

set_mutable1.add(22)#este método agraga un elemento a un conjunto mutable
print(set_mutable1)

set_mutable1.clear()#este método remueve todos los elementos dede este conjunto mutable
print(set_mutable1)

set_mutable = set([4.0, "Carro", True])
set_mutable1 = set_mutable.copy()#este método devuelve una copia superficial del tipo conjunto mutable o conjunto inmutable
if set_mutable == set_mutable1:
    print("copia superficial del tipo conjunto mutable o conjunto inmutable")

print(set_mutable1.difference(set_mutable2))#este método devuelve la diferencia entre dos conjunto mutable o conjunto inmutable.
print(set_mutable2.difference(set_mutable1))

proyecto1 = {"python","Zope","ZODB3","zope.pagetemplate"}
proyecto2 = {"python","Plone","plone.volto"}
print(proyecto1)
print(proyecto2)
proyecto1.difference_update(proyecto2)#este método actualiza un tipo conjunto mutable llamando al método difference_update() con la diferencia de los conjuntos
print(proyecto1)

paquetes = {"python", "zope", "plone", "django"}
print(paquetes)

paquetes.discard("django")#este método remueve un elemento desde un conjunto mutable si esta presente
print(paquetes)

#un conjunto mutable permanece sin cambios si el elemento pasado 
#como argumento al método discard() no existe.
paquetes.discard("php")
print(paquetes)