"""def nombre_funcion(Puede tener parametros):
    -instrucciones de la funcion
    -return(opcional)
"""
#Ejecutarlo es: nombre_funcion(parametros)

#Funcion Basica

def mensaje():  #Declaracion
    print("Hola mundo")
    print("Probando las funciones")  #Cuerpo de la funcion

mensaje()  #Llamada de funcion

#Funcion con parametros

def suma(num1, num2):
    
    resultado = num1+num2
    return resultado  #print(suma())

print(suma(5,7))

print(suma(2,3))

print(suma(35,358))

almacenar_resultado=suma(5,8)
print(almacenar_resultado)