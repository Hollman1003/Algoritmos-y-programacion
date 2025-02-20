# Ejercicio 5________________________________


print("Ingrese las calificaciones de los parciales: ")
Nota_1 = float(input("Calificación del primer parcial: "))
Nota_2 = float(input("Calificación del segundo parcial: "))
Nota_3 = float(input("Calificación del tercer parcial: "))

ExamenFinal = float(input("Envie la calificacion de examen final: "))

TrabajoFinal = float(input("Envie la calificacion del trabajo final: "))

PromedioNotas = (Nota_1 + Nota_2 + Nota_3) / 3
PromedioParciales = PromedioNotas * 0.55
PromedioExamenFinal = ExamenFinal * 0.30
PromedioTrabajoFinal = TrabajoFinal * 0.15


PromedioFinal = PromedioParciales + PromedioExamenFinal + PromedioTrabajoFinal

print("Sus calificaciones en la finales son:", PromedioFinal)