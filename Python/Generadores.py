"""
¿QUE SON?
-Estructuras que extraen valores de una funcion y se almacenan en objetos iterables(que se pueden recorrer)
-Estos valores se almacenan de uno en uno
-Cada vez que un gnerador almaccena un valor, esta permanece en un stado pausado hasta que se solicita el siguiente. Esta característica es conocida como "Suspension de estado"
"""

"""
UTILIDAD:
-son mas eficientes que las funciones tradicionales
-Muy utiles con listas de valores infinitos
-Bajo determinados escenarios, sera muy util que un generador devuelva los valores de uno en uno
"""

#----------------------------------------------------------
"""
#sintaxis
def ejemplo():
    numero=1
    yield numero
    """
#-------------------------------------------------------------
"""
#Ejemplo de una funcion de manera normal
def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))
"""
#---------------------------------------------------------------
"""
#ejemplo del uso de yield
def generaPares(limite):
    num=1

    while num<limite:

        yield num*2

        num=num+1
devuelvePares=generaPares(10)

for i in devuelvePares:
    print(i)
    """
#-----------------------------------------------------------------
"""
#ejemplo del uso de yield
def generaPares(limite):
    num=1

    while num<limite:

        yield num*2

        num=num+1
devuelvePares=generaPares(10)

print(next(devuelvePares))

print("Aqui podria ir mas codigo")

print(next(devuelvePares))

print("Aqui podria ir mas codigo")

print(next(devuelvePares))
"""
#------------------------------------------------------
#Uso de "yield from"
#utilidad simplificar el codigo de los generadores en el caso de utilizar bucles anidados

def devuelve_ciudades(*ciudades):#el asterisco indica que va a recibir un numero indeterminado de elementos ademas lo va a recibir en forma de tuplas
    for elementos in ciudades:
        #for subElemento in elementos:
            yield from elementos


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))