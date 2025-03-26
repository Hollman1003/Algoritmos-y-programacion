# Suma de todos los números pares comprendidos entre 97 y 1003
suma = 0

for num in range(97, 1004):  
    if num % 2 == 0:
        suma += num  # Sumar el número a la variable suma

print("La suma de los números pares entre 97 y 1003 es:", suma)

    