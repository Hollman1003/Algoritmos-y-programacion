CapitalInvercion = float(input("Ingrese el monto de la inversión en COP: "))
TasaInteres = float(input("Ingrese la tasa de interés anual (en %): "))
TiempoAños = int(input("Ingrese el tiempo de inversión en años: "))

TasaInteresToDecimal = TasaInteres / 100

Intereses = CapitalInvercion * TasaInteresToDecimal * TiempoAños

if Intereses > 100000:
    CapitalTotal = CapitalInvercion + Intereses
    print(f"\nLos intereses generados son: ${Intereses} COP")
    print("Se reinvierten los intereses.")
    print(f"Monto final en la cuenta: ${CapitalTotal} COP")
else:
    print(f"\nLos intereses generados son: ${Intereses} COP")
    print("Los intereses no son suficientes para reinversión.")
    print(f"Monto total en la cuenta: ${CapitalInvercion} COP")
