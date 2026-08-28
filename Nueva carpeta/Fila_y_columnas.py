for aula in range(1,5):
    suma=0
    print(f"--AULA--{aula}")
    for estudiante in range (1,6):
        nota = float(input("Ingrese la nota del estudiante:"))
        suma=suma+nota
        promedio=suma/5
    print(f"El promedio del aula {aula} es: {promedio}")
