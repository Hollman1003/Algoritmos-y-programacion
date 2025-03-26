# División de dos números enteros mediante restas sucesivas

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente = 0
residuo = dividendo

while residuo >= divisor:
    residuo -= divisor
    cociente += 1

print("Cociente:", cociente)
print("Residuo:", residuo)
