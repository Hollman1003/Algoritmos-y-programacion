from math import sqrt

VariableA = float(input("Ingrese el coeficiente A: "))
VariableB = float(input("Ingrese el coeficiente B: "))
VariableC = float(input("Ingrese el coeficiente C: "))

if VariableA == 0:
    print("A no puede ser 0")
    
else:
    Formula = VariableB**2 - 4 * VariableA * VariableC

    if Formula > 0:
        X1 = (-VariableB + sqrt(Formula)) / (2 * VariableA)
        X2 = (-VariableB - sqrt(Formula)) / (2 * VariableA)
        print(f"Las soluciones son: X1 = {X1}, X2 = {X2}")

    elif Formula == 0:
        X1 = -VariableB / (2 * VariableA)
        print(f"Existe una única solución: X = {X1}")

    else:
        print("No tiene solución en los números reales.")