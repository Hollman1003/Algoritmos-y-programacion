SueldoTexto = input("Envie el sueldo del trabajador: ")

SueldoNumerico = int(SueldoTexto)

if (SueldoNumerico < 900000):
    Aumento = SueldoNumerico * 0.15
elif (SueldoNumerico >= 900000):
    Aumento = SueldoNumerico * 0.12

NuevoSueldo = SueldoNumerico + Aumento

print("El nuevo sueldo del trabajador es: ", NuevoSueldo)