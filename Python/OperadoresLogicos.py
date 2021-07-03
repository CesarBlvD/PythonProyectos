#Conjuncion

print("Conjuncion (and)")

num1 = int(input("Escribe un numero mayo a 2 y menor a 5:"))

if num1 > 2 and num1 <5:
    print("El numero ", num1, " Cumple con la condicion\n")
else:
    print("El numero ",num1, " NO CUMPLE CON LA CONDICION\n")

#Disyuncion
print("DISYUNCION (or)")

palabra = input("Para cumplir con la condicion escribe 'si' o 'yes':")
palabra = palabra.lower()

if palabra == "si" or palabra == "yes":
    print("La condicion SE HA CUMPLIDO\n")
else:
    print("La condicion NO SE HA CUMPLIDO")

#Negacion
print("NEgacion(NOT)")

num2 = int(input("Introduce un numero igual a 5: "))

if not num2 == 5:
    print("\nEl numero es diferente de 5 y SI CUMPLE LA CONDICION\n")
else:
    print("\nEl numero es igual a 5 y NO CUMPLE CON LA CONDICION")
