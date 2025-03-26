# Función para verificar si un número es perfecto

def Numero_Perfecto(Numero):
    Suma = 0  

   
    for i in range(1, Numero):
        if Numero % i == 0:  
            Suma += i  


    if Suma == Numero:
        print(f"{Numero} es un número perfecto.")
    else:
        print(f"{Numero} no es un número perfecto.")


try:
    Numero = int(input("Introduce un número entero positivo: "))
    if Numero > 0:
        Numero_Perfecto(Numero)
    else:
        print("Por favor, introduce un número entero positivo.")
except Valorinvalido:
    print("Entrada no válida. Asegúrate de introducir un número entero.")