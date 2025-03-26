#Encontrar la mayor altura entre un grupo de estudiantes.
N_Estudiantes = int(input("Ingrese el número de estudiantes: "))

max_altura = 0


for Estudiante in range(N_Estudiantes):
    altura = float(input(f"Ingrese la altura del estudiante {Estudiante+1}: "))
    if altura > max_altura:
        max_altura = altura

print("La mayor altura es:", max_altura)
