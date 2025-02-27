print("Calculadora Especifica")

ValuesText = input("Ingrese los datos A, B, C y D separado por espacios:")

(A,B,C,D) = ValuesText.split(" ")

ValueA = int(A)
ValueB = int(B)
ValueC = int(C)
ValueD = int(D)

def ValueEqualToZero(FirstValue, SecondValue):
    return (FirstValue - SecondValue)**2 # (A-C)^2

def ValueNotEqualToZero(FirstValue, SecondValue, ThirdValue):
    return (FirstValue - SecondValue)**3 / ThirdValue # (A-B)^3 / D

if (ValueD == 0):
    print(f"El resultado de la funcion `(A-C)^2` es: {ValueEqualToZero(ValueA, ValueC)}")
else:
    print(f"El resultado de la funcion `(A-B)^3 / D` es: {ValueNotEqualToZero(ValueA, ValueB, ValueD)}")
