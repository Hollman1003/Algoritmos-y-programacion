DenominacionesBilletes = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

Cantidad = int(input("Ingrese la cantidad en COP: "))

Cantidad = (Cantidad // 50) * 50

DesgloseBilletes = []

for Billete in DenominacionesBilletes:
    if (Cantidad >= Billete):
        CantidadBilletes = Cantidad // Billete
        Cantidad %= Billete
        DesgloseBilletes.extend([Billete] * CantidadBilletes)

print(",".join(map(str, DesgloseBilletes)))