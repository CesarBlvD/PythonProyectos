#Practica 1 en python

print("Vacaciones segun tu antiguedad y tu clave\n")

nombre = input("Ingresa tu nombre completo por favor: ")

clave = int(input("Hola "+nombre+" Ingresa la clave a la que perteneces: "))

anios = float(input("Por favor "+nombre+" Ingresa los años que llevas laborando:"))

if clave == 1:
    if anios == 1:
        print(nombre + " Te pertenecen 6 dias de vacaciones")
    elif anios >= 2 and anios <=6:
        print(nombre + " Te pertenecen 14 dias de vacaciones")
    elif anios >=7:
        print(nombre + " Te pertenecen 20 dias de vacaciones")
    else:
        print(nombre + " No tienes derecho a vacaciones")
elif clave == 2:
    if anios == 1:
        print(nombre + " Te pertenecen 7 dias de vacaciones")
    elif anios >= 2 and anios <=6:
        print(nombre + " Te pertenecen 15 dias de vacaciones")
    elif anios >=7:
        print(nombre + " Te pertenecen 22 dias de vacaciones")
    else:
        print(nombre + " No tienes derecho a vacaciones")
elif clave == 3:
    if anios == 1:
        print(nombre + " Te pertenecen 10 dias de vacaciones")
    elif anios >= 2 and anios <=6:
        print(nombre + " Te pertenecen 20 dias de vacaciones")
    elif anios >=7:
        print(nombre + " Te pertenecen 30 dias de vacaciones")
    else:
        print(nombre + " No tienes derecho a vacaciones")
else:
    print("La clave no existe")
