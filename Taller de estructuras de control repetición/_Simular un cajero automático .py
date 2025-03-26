# Simular un cajero automático 
def Cajero_Automatico():
    Saldo = 0  

    while True:
        print("Cajero Automático")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")
        
        
        Opción = input("Seleccione una opción (1-4): ")

        if Opción == '1':
            Cantidad = float(input("Ingrese la cantidad a depositar: "))
            Saldo += Cantidad
            print(f"Has depositado ${Cantidad:.2f}. Su nuevo saldo es ${Saldo:.2f}.")

        elif Opción == '2':
            Cantidad = float(input("Ingrese la cantidad a retirar: "))
            if Cantidad > Saldo:
                print("No tiene suficiente saldo para realizar esta operación.")
            else:
                Saldo -= Cantidad
                print(f"Has retirado ${Cantidad:.2f}. Su nuevo saldo es ${Saldo:.2f}.")

        elif Opción == '3':
            print(f"Su saldo actual es ${Saldo:.2f}.")

        elif Opción == '4':
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

Cajero_Automatico()