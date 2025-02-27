A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))

NumeroCompleto = A * 1000 + B * 100 + C * 10 + D

NumeroRedondeado = round(NumeroCompleto, -2)

print(f"El número original es: {NumeroCompleto}")
print(f"El número redondeado es: {NumeroRedondeado}")
