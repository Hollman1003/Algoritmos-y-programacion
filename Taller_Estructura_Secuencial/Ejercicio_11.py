# Ejercicio 11  ________________________________

#Ejercicio_11_Sueldo_Trabajador

Nombre = ""
Horas_Normales = 0.0
Horas_Extras = 0.0
Pago_Hora = 0.0
Sueldo_Base = 0.0
Pago_Extras = 0.0
Asignaciones = 0.0
Deducciones = 0.0
Sueldo_Neto = 0.0
Numero_Hijos = 0


Nombre = input("Ingrese el nombre del empleado: ")
Horas_Normales = float(input("Ingrese el número total de horas normales laboradas: "))
Pago_Hora = float(input("Ingrese el pago por hora normal: "))
Horas_Extras = float(input("Ingrese el número de horas extras laboradas: "))
Numero_Hijos = int(input("Ingrese el número de hijos: "))


Sueldo_Base = Horas_Normales * Pago_Hora
Pago_Extras = Horas_Extras + (Pago_Hora * 1.25)
Asignaciones = Pago_Extras + 250000 + (173000 * Numero_Hijos) + 180000
Deducciones = (Sueldo_Base * 0.05) + (Sueldo_Base * 0.02) + (Sueldo_Base * 0.07)
Sueldo_Neto = Sueldo_Base + Asignaciones - Deducciones

print("Asignaciones:", Asignaciones)
print("Deducciones:", Deducciones)
print("Sueldo neto:", Sueldo_Neto)
