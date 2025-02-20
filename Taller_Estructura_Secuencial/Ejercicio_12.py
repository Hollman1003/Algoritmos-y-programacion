# Ejercicio 12  ________________________________

#Ejercicio_12_Promedio_Alumno

examen_mate = float(input("Ingrese la nota del examen de Matemática: "))
tareas_mate1 = float(input("Ingrese la primera nota de tarea de Matemática: "))
tareas_mate2 = float(input("Ingrese la segunda nota de tarea de Matemática: "))
tareas_mate3 = float(input("Ingrese la tercera nota de tarea de Matemática: "))

promedio_mate = (examen_mate * 0.9) + (((tareas_mate1 + tareas_mate2 + tareas_mate3) / 3) * 0.1)

examen_fisica = float(input("Ingrese la nota del examen de Física: "))
tareas_fisica1 = float(input("Ingrese la primera nota de tarea de Física: "))
tareas_fisica2 = float(input("Ingrese la segunda nota de tarea de Física: "))

promedio_fisica = (examen_fisica * 0.8) + (((tareas_fisica1 + tareas_fisica2) / 2) * 0.2)

examen_quimica = float(input("Ingrese la nota del examen de Química: "))
tareas_quimica1 = float(input("Ingrese la primera nota de tarea de Química: "))
tareas_quimica2 = float(input("Ingrese la segunda nota de tarea de Química: "))
tareas_quimica3 = float(input("Ingrese la tercera nota de tarea de Química: "))

promedio_quimica = (examen_quimica * 0.85) + (((tareas_quimica1 + tareas_quimica2 + tareas_quimica3) / 3) * 0.15)

promedio_general = (promedio_mate + promedio_fisica + promedio_quimica) / 3

print("Promedio Matemática:", promedio_mate)
print("Promedio Física:", promedio_fisica)
print("Promedio Química:", promedio_quimica)
print("Promedio General:", promedio_general)