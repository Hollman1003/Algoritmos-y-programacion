# Ejercicio 4

estudiantes = {}
max_estudiantes = 10 

for i in range(1, max_estudiantes + 1):
    print(f"\nEstudiante {i}")
    nombre = input("Nombre del estudiante: ")
    
    while True:
        try:
            nota = float(input("Nota del estudiante (0-10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Introduce un número válido para la nota.")
    
    estudiantes[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }

aprobados = []
suspendidos = []
suma_notas = 0

for estudiante in estudiantes.values():
    nota = float(estudiante["nota"])
    suma_notas += nota
    if nota >= 5:
        aprobados.append(estudiante["nombre"])
    else:
        suspendidos.append(estudiante["nombre"])

print("\nEstudiantes aprobados:")
for nombre in aprobados:
    print(f"- {nombre}")

print("\nEstudiantes suspendidos:")
for nombre in suspendidos:
    print(f"- {nombre}")

media = suma_notas / len(estudiantes)
print(f"\nNota media de la clase: {media:.2f}")