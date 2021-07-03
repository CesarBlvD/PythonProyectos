print("Introducir dos numeros para comparar\n")

num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))

print("\nLos numeros a comparar son: ", num1, "Y", num2, "\n")

if num1==num2:
    print("El numero 1 es igual al numero 2")
elif num1>num2:
    print("El numero 1 es mayor que el numero 2")
elif num1<num2:
    print("El numero 1 es menor que el nuemro 2")
elif num1 != num2:
    print("El numero es diferente al numero 2")
