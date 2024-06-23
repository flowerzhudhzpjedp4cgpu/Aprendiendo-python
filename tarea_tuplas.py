#creando una tupla (no pueden modificar / inmutable)
tecnologias = ("Zope", "Plone", "Pyramid")

#este no es valido 
#tecnologias[0] = "Maquinola"

#iterar sobre una secuencia mientras cuidas el seguimiento
for i in range(0, len(tecnologias)):
    print(i, tecnologias[i])