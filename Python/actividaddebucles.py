"""
#Pedir un email y validarlo
x=3
print("Solo tienes 3 intentos para introducir una direccion de correo valida")
while x>0:
    miEmail=input("introduce tu direccion de email: ")
    miEmail.lower()
    print("Te quedan ", x," Intentos")
    contadorArroba=0
    contadorPunto=0
    for i in miEmail: #Verifica caracter por caracter cesarhdez2401@gmail.com
        if (i == "@"):
            contadorArroba=contadorArroba+1
        if(i=="."):
            contadorPunto=contadorPunto+1
    if (contadorArroba>=2): 
        print("El email tiene mas de un arroba, ingrese otro diferente")
        x=x-1
        if (x==0):
            print("Demasiados intentos cerrando terminal...")
    elif(contadorPunto>=2):
        print("El email tiene mas de un putno, ingrese otro diferente")
        x=x-1
        if (x==0):
            print("Demasiados intentos cerrando terminal...")
    elif(contadorPunto==0):
        print("Le falta un punto a tu direccion de correo electronico")
        x=x-1
        if (x==0):
            print("Demasiados intentos cerrando terminal...")
    elif(contadorArroba==0):
        print("Le falta un arroba a tu direccion de correo electronico")
        x=x-1
        if (x==0):
            print("Demasiados intentos cerrando terminal...")
    else:
        print("El email es correcto")
        x=0
    """
#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo

#Comparacion de numeros pares e impares
numero1=(input("Ingrese un numero "))
for i in numero1:
    if(i >="a"):
        print("Ingresaste una letra")
    else:
        entero1=int(numero1)
        numero2=(input("Ingrese un numero mayor que el anterior "))
        for i in numero2:
            if(i >="a"):
                print("Ingresaste una letra")
            else:
                entero2=int(numero2)
                if (entero1<=entero2):
                    for i in range(entero1, entero2+1):
                        if ((entero1%2)==0):
                            print("El numero ",entero1,"Es par")
                            entero1=entero1+1
                        else:
                            print("El numero ",entero1," Es impar")
                            entero1=entero1+1
                else:
                    print("El primer numero tiene que ser menor o igual que el segundo")


