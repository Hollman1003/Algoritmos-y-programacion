def calcular_pagos(ValorCompra):
    if ValorCompra > 5000000:
        InversionEmpresa = ValorCompra * 0.55
        BancoPrestamo = ValorCompra * 0.30
        CreditoFabricante = ValorCompra * 0.15
    else:
        InversionEmpresa = ValorCompra * 0.70
        BancoPrestamo = 0
        CreditoFabricante = ValorCompra * 0.30

    Intereses = CreditoFabricante * 0.20
    TotalCredito = CreditoFabricante + Intereses

    print(f"Valor total de la compra: ${ValorCompra} COP")
    print(f"Inversión de la empresa: ${InversionEmpresa} COP")
    print(f"Préstamo del banco: ${BancoPrestamo} COP")
    print(f"Crédito del fabricante: ${CreditoFabricante} COP")
    print(f"Intereses a pagar: ${Intereses} COP")
    print(f"Total de crédito a pagar: ${TotalCredito} COP")

# Ejemplo de uso:
ValorCompra = float(input("Ingrese el valor total de la compra en COP: "))
calcular_pagos(ValorCompra)