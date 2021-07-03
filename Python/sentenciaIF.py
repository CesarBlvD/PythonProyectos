print("Sistema para calcular el promedio del alumno ")
nombre = input("Por favor ingresa tu numbre: ")
materia1= float(input(nombre + " Ingresa la calificacion de Fisica: "))
materia2= float(input(nombre + " Ingresa la calificacion de Matematicas: "))
materia3= float(input(nombre + " Ingresa la calificacion de quimica: "))
suma = materia1 + materia2 + materia3
total = suma/3
print(nombre + " El promedio total de las materias es: ", total)
print(nombre + " El promedio total de las materias es: ", round(total,2))
if total>=6.0:
    print("APROBASTE EL CURSO " + nombre)
    print("Probando el if")
else:
    print("REPROBASTE EL CURSO " + nombre)
    print("Probando el else")
