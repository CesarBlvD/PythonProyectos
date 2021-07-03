def divide():
#hola
    try:
        op1=(float(input("Introduce el primer numero: ")))

        op2=(float(input("Introduce el primer numero: ")))

        print("La division es: " + str(op1/op2))

        print("Calculo finalizado")
    except ValueError:

        print("El Valor introducido es erroneo")

    except ZeroDivisionError:

        print("No se puede divir entre 0")
    #except: detectar cualquier tipo de erro

        #print("Ha ocurrido un error")
    finally: #En el finally se ejecuta siempre
        print("Calculo finalizado")

divide()