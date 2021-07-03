Diccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino unido":"Londres", "España":"Madrid"}
#Los diccionarios cuentan con una clave y un objeto, accediendo a la clave te entrega el objeto
Diccionario2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3} #Acepta cualquier valor
tupla=["España", "Francia", "Reino unido", "Alemania"]
Diccionario3={tupla[0]:"Madrir", tupla[1]:"Paris", tupla[2]:"Londres", tupla[3]:"Berlin"}
Diccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(Diccionario4)
print(Diccionario4["Anillos"])
print(Diccionario4.keys())
print(Diccionario4.values())
print(len(Diccionario4))
print(Diccionario3)
print(Diccionario2)
print(Diccionario["Francia"]) #Como accede al objeto y debera mostrar paris
Diccionario["Italia"]="Lisboa"#Agregar un elemneto
print(Diccionario) #Imprimir todo el diccionario
Diccionario["Italia"]="Roma"#Modificar un valor
del Diccionario["Reino unido"]#Como eleminar elementos
print(Diccionario)

