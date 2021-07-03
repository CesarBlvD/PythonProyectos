print("CONVERSOR!!!")
print("============ \n\n")
print("Menu de opciones\n")
print("Presiona 1 para convertir de numero a palbara")
print("Presiona dos para convertir de palabra a numero\n")

opcion = int(input("¿Cual es la opcion deseada?: "))

if opcion == 1:
    print("\nVamos a convertir de numero a palabra")

    opcion1= int(input("¿Cual es el numero que deseas convertir a palabra?: "))

    if opcion1 == 1:
        print("el numero es UNO")

    elif opcion1 == 2:
        print("el numero es DOS")

    elif opcion1 == 3:
        print("el numero es TRES")

    elif opcion1 == 4:
        print("el numero es CUATRO")

    elif opcion1 == 5:
        print("el numero es cinco")
    else:
        print("Ese numero no esta registrado")

elif opcion == 2:
    print("\nVamos a convertir de palabra a numero")

    opcion2 = input("¿Cual es la palabra que deseas convertir a numero?")
    opcion2 = opcion2.lower()

    if opcion2 == "uno":
        print("el numero es 1")

    elif opcion2 == "dos":
        print("el numero es 2")

    elif opcion2 == "tres":
        print("el numero es 3")

    elif opcion2 == "cuatro":
        print("el numero es 4")

    elif opcion2 == "cinco":
        print("el numero es 5")
    else:
        print("Ese numero no existe en la base de datos")
        
else:
    print("\nOpcion no disponible")

print("Fin de codigo")

