"""
#Un programa que evualue si un alumno tiene derecho a una beca

print("Programa de becas año 2021")

distancia_escuela=int(input("Introduce la distancia de la escuela en Km "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario anual bruto "))
print(salario_familiar)

#Probando operadores and y or en una sentencia if
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
"""
#Probando in
from typing import AsyncContextManager


print("Asignaturas optativas año 2021")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion= input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() #Cambiar las letras a minusculas

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura.upper()) #Cambiar letras a minusculas
else:
    print("La asignatura escogida no esta contemplada")