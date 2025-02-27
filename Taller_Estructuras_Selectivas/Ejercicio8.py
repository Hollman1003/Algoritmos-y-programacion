ValueP = int(input("Ingrese el valor de P: "))
ValueQ = int(input("Ingrese el valor de Q: "))

ExpresionMatematica = (ValueP**3 + ValueQ**4 - 2 * ValueP**2) > 680

if ExpresionMatematica:
    print("P = " + str(ValueP) + " y Q = " + str(ValueQ) + " satisfacen la expresión")
else:
    print("P = " + str(ValueP) + " y Q = " + str(ValueQ) + " no satisfacen la expresión")
