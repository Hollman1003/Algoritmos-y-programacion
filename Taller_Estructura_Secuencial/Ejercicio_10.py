# Ejercicio 10  ________________________________

#Ejercicio_10_CambioDivisas
def cambio_divisas():
   
    Chelines = 0
    Dracmas = 0
    Pesetas = 0

    Chelines = float(input("Ingrese la cantidad en Chelines austriacos: "))
    EnPesetas = (Chelines * 956.871) / 100
    print(f"{Chelines} Chelines austríacos equivalen a {EnPesetas} pesetas.")


    Dracmas = float(input("Ingrese la cantidad en Dracmas griegos: "))
    EnPesetas = (Dracmas * 88.607) / 100
    EnFrancos = EnPesetas / 20.110
    print(f"{Dracmas} Dracmas griegos equivalen a {EnFrancos} francos franceses.")

    Pesetas = float(input("Ingrese la cantidad en pesetas: "))
    EnDolares = Pesetas / 122.499
    EnLiras = (Pesetas * 100) / 9.289
    print(f"{Pesetas} Pesetas equivalen a {EnDolares} dólares y {EnLiras} liras italianas.")

cambio_divisas()
