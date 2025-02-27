LecturaAnterior = int(input("Ingrese la lectura anterior (Kwh): "))
LecturaActual = int(input("Ingrese la lectura actual (Kwh): "))

ConsumoGeneral = LecturaActual - LecturaAnterior
if ConsumoGeneral < 0:
    print("La lectura actual debe ser mayor o igual a la lectura anterior.")
else:
    if ConsumoGeneral <= 100:
        CostoKwh = 4600
    elif ConsumoGeneral <= 300:
        CostoKwh = 80000
    elif ConsumoGeneral <= 500:
        CostoKwh = 100000
    else:
        CostoKwh = 120000
    ValorPagar = ConsumoGeneral * CostoKwh

print(f"El consumo fue de: {ConsumoGeneral}") 
print(f"El valor total a pagar es: {ValorPagar}")
