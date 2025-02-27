DistanciaRecorrida = float(input("Ingrese la distancia recorrida en km: "))

if DistanciaRecorrida <= 300:
    CostoCliente = 50000
elif DistanciaRecorrida <= 1000:
    CostoCliente = 70000 + (DistanciaRecorrida - 300) * 30000
else:
    CostoCliente = 150000 + (DistanciaRecorrida - 1000) * 9000

print(f"El costo total a pagar es: {CostoCliente} COP")
