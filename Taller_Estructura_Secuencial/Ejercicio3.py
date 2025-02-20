# Ejercicio 3________________________________

Salario_Base = float(input("Indique su salario base: "))

Primera_Venta = float(input("Cuánto fue su primera venta: "))
Segunda_Venta = float(input("Cuánto fue su segunda venta: "))
Tercera_Venta = float(input("Cuánto fue su tercera venta: "))


Ventas_Totales = Primera_Venta + Segunda_Venta + Tercera_Venta

Comision_Total = Ventas_Totales * 10 / 100

Pago_Total = Salario_Base + Comision_Total


print("Su salario con comisiones da un total de:",Pago_Total )