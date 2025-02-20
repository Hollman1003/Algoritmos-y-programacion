# Ejercicio 7 ________________________________

#Ejercicio_7_Conversion_Metros_Pies_Pulgadas

Metros = float(input("Ingrese la cantidad en metros: "))

Pulgadas = Metros * 39.27
Pies = int(Pulgadas // 12)  
PulgadasRestantes = Pulgadas - (Pies * 12)

print(f"La cantidad en metros equivale a: {Pies} pies y {PulgadasRestantes:.2f} pulgadas.")
