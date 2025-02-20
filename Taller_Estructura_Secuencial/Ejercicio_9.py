# Ejercicio 9  ________________________________
#Ejercicio_9_CalculoSalarioNeto

HorasTrabajadas = float(input("Ingrese el número de horas trabajadas: "))
PrecioHora = float(input("Ingrese el precio por hora: "))

SueldoBase = HorasTrabajadas * PrecioHora

Descuento = SueldoBase * 0.20

SalarioNeto = SueldoBase - Descuento

print("El salario neto es:", SalarioNeto)

