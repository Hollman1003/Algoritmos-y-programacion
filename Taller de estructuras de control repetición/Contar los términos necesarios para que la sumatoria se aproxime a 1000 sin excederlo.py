# Contar los términos necesarios para que la sumatoria se aproxime a 1000 sin excederlo
suma = 0
k = 1
while suma + k <= 1000:
    suma += k
    k += 1

print("Número de términos necesarios:", k - 1)