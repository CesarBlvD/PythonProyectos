"""Declaracion
nombreLista=[elem1,elem2,elem3.....]
son similares a los array solo que aqui puedes guardar cualquier elemento
"""

Lista=["Cesar", "Jose", "Marta", "Antonio"] #Si se coloca un "*" se coloca la lista 3 veces
lista2=["Cesar", 5, True, 78.8]

lista3=Lista+lista2#Sumar listas(concatenar)
print(lista3[:])
print(lista2[:])
Lista.append("Sandra") #Agregar a la lista (al final)
Lista.insert(2,"Sandra") #Agregarla en un punto intermedio
Lista.extend(["Jesus", "Lucia", "Johana"]) #Agregar mas personas a la misma lista
Lista.remove("Jesus")#Eliminar elementos de la lista
Lista.pop() #Elimina el ultimo elemento de la lista
print(Lista.index("Sandra")) #Buscar posiciones de los elementos
print("Joses" in Lista) #Buscar si hay o no un dato
print(Lista[:]) #Para imprimir todos los datos
print(Lista[2]) #Un elemento en concreto
#print(Lista[7]) #Error de indice
print(Lista[-3]) #Cuenta del final para atras
print(Lista[1:3]) #Acceder a una porcion de la lista

