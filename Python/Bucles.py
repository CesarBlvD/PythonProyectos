#While
#------------------------------------
"""
x=1
while x<3:
    print(x)
    x=x+1
print("Fin")

"Ejemplo2"

x=1
y=10
m="Hola"
while x<=10:
    print(f"Cesar{1}")
    x+=1
"""
#-------------------------------------------------------
"""
import math
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0
while numero<0:
    print("No se puede hayar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido demasiados intentos, El programa ha finalizado")
        break;
    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos+=1
if intentos<2:
    solucion=math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {solucion}")
"""
#-------------------------------------------------------
#Continue pass y else
"""
for letra in "Python":
    if letra == "h":
        continue #Evita presentar la h como si la brincara
    print("Viendo la letra: "+ letra)
#Conteo de string
nombre="Pildoras Informaticas"

contador=0
for i in nombre:

    if i==" ":
        continue #El codigo unicamente nos dira letras sin el espacio
    contador+=1

print(contador)

#Instruccion pass se evita el codigo o se lo brinca como si fuera un comentario
email=input("Introduce tu email, por favor ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:   #Se puede usar en for tambien
    arroba=False
print(arroba)
"""

#-------------------------------------------------------
#For 
# A i se le asigna un dato segun sean arreglos, tuplas o numeros
"""
for i in ["Primavera","Verano","Otoño","Invierno"]: #i="Primavera" luego ejecuta "Hola" y asi con los demas datos
    print("Hola")
    print(i)
"""
#-------------------------------------------------------
"""
#Imprimir todo en una linea
for i in ["pildoras", "informaticas", 3]:
    print("Hola", end=" ") #uso de end para evitar salto de linea palabras medias entre hola
"""
#imprimir hola por cada caracter
#-----------------------------------------------------------
"""
email=False
miEmail=input("introduce tu direccion de email: ")
for i in miEmail: #Verifica caracter por caracter
    if (i == "@"):
        email=True
if (email==True): #Colocar true puede ser opcional if email:
    print("Email es correcto")
else:
    print("Email es incorrecto")
""" 
#------------------------------------------------------------
"""
contador=0
email=False
miEmail=input("introduce tu direccion de email: ")
for i in miEmail: #Verifica caracter por caracter
    if (i == "@" or i=="."):
        contador=contador+1

if (contador==2): 
    print("Email es correcto")
else:
    print("Email es incorrecto")
    """
#------------------------------------------------------
"""
for i in range(5):
    print("hola")
"""
"""
#------------------------------------------------------
#Primer valor(5,0,0) llega la repeticion hasta la 5
#segundo valor(5,9,0) segundo valor pone un limite de 5 hasta 9
#Tercero valor (5,9,2) indica de cuanto va ir subiendo la variable)
for i in range(5):
    print(f"valor de la variable {i}") #una manera de concatenar la variable
    #print("Valor de la variable", i)
    len("Juan") #devuelve el numero de caracteres de un string
"""
#---------------------------------------------------------
"""
valido= False

email=input("Introduce tu email: ")

for i in range(len(email)): #Recorrido de 4 
    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")
"""
#-----------------------------------------------------------