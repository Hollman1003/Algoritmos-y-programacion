TemperaturaRegistrada = float(input("Ingrese la temperatura en grados Fahrenheit: "))

if TemperaturaRegistrada > 85:
    DeporteSeleccioando = "Natación"
elif (70 <= TemperaturaRegistrada <= 85):
    DeporteSeleccioando = "Tenis"
elif (32 <= TemperaturaRegistrada <= 70):
    DeporteSeleccioando = "Golf"
elif (10 < TemperaturaRegistrada <= 32):
    DeporteSeleccioando = "Esquí"
elif (TemperaturaRegistrada > 10):
    DeporteSeleccioando = "Marcha"

print(f"Temperatura ingresada: {str(TemperaturaRegistrada)} °F")
print(f"Deporte recomendado: {DeporteSeleccioando}")
