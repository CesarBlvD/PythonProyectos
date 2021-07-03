print("Programa de evaluacion de notas de alumnos")
nota_alumno=int(input("Ingresa un numero del 1 al 10: "))

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(nota_alumno))