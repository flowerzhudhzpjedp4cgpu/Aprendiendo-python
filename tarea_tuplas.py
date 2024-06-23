#creando una tupla (no pueden modificar / inmutable)
tecnologias = ("Zope", "Plone", "Pyramid")
valores = ("Python", True, "Zope", 5)

#este no es valido 
#tecnologias[0] = "Maquinola"

#iterar sobre una secuencia mientras cuidas el seguimiento
for i in range(0, len(tecnologias)):#función range, len
    print(i, tecnologias[i])
    
for contador, tecnologia in enumerate(tecnologias, start=1):#la palabra reservada enumerate
    print(contador, tecnologia)
    
print(valores.index(True))#recibe un elemento como argumento, y devuelve el índices