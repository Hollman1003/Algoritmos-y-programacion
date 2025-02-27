NopmbreCliente = input("Ingrese el nombre del cliente: ")
ValorCompra = float(input("Ingrese el valor de la compra en COP: "))

if ValorCompra < 50000:
    Descuento = 0
elif ValorCompra <= 100000:
    Descuento = 0.05
elif ValorCompra <= 700000:
    Descuento = 0.11
elif ValorCompra <= 1500000:
    Descuento = 0.18
else:
    Descuento = 0.25

ValorDescuento = ValorCompra * Descuento
TotalCompra = ValorCompra - ValorDescuento

print("\n--- Factura de Compra ---")
print("Cliente: " + NopmbreCliente)
print(f"Monto de la compra: $ {ValorCompra} COP")
print(f"Descuento aplicado: {str(int(Descuento * 100))} %")
print(f"Valor del descuento: $ {ValorDescuento} COP")
print(f"Monto a pagar: $ {TotalCompra} COP")
