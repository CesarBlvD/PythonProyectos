salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))
#salario_presidente=str(salario_presidente)

salario_director=int(input("Introduce el salario del Director: "))
print("Salario presidente: " + str(salario_presidente))

salario_jefeArea=int(input("Introduce el salario del Jefe de area: "))
print("Salario presidente: " + str(salario_presidente))

salario_administrativo=int(input("Introduce el salario del Administrativo: "))
print("Salario presidente: " + str(salario_presidente))

if salario_administrativo<salario_jefeArea<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo esta mal")