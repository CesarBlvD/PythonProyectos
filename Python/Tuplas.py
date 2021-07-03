#Sintaxis de las tuplas
"""NombreTupla=(elem1, elem2, elem3....)   parentesis tupla corchetes lista

"""
#Ejemplo=("Hola", 10, 11)

tupla=("Hola", 10, 1, 1234)
nombre, dia, mes, ano = tupla  #asignar las variables a la tupla
print (nombre)
print (ano)
lista=list(tupla) #Convertir una tupla en una lista
print(tupla[:])
print(tupla.count(10)) #cuantas veces hay un dato en la tupla
print(len(tupla)) #La longitud de la tupla 


#Convertir la lista en una tupla
"""lista1=[10, 21, "hola"]
tupla2=tuple(lista1)
print(tupla2)
"""