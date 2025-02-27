def determinar_anemia(EdadMeses, SexoUsuario, NivelHemoglobina):
    # Definir los rangos según la tabla
    if 0 <= EdadMeses <= 1:  # 0 meses - 1 mes
        rango_min, rango_max = 13, 26
    elif 1 < EdadMeses <= 6:  # Mayor de 1 mes y menor o igual de 6 meses
        rango_min, rango_max = 10, 18
    elif 6 < EdadMeses <= 12:  # Mayor de 6 meses y menor o igual de 12 meses
        rango_min, rango_max = 11, 15
    elif 12 < EdadMeses <= 60:  # Mayor de 1 año y menor o igual de 5 años (60 meses)
        rango_min, rango_max = 11.5, 15
    elif 60 < EdadMeses <= 120:  # Mayor de 5 años y menor o igual de 10 años (120 meses)
        rango_min, rango_max = 12.6, 15.5
    elif 120 < EdadMeses <= 180:  # Mayor de 10 años y menor o igual de 15 años (180 meses)
        rango_min, rango_max = 13, 15.5
    elif EdadMeses > 180:  # Mayores de 15 años
        if SexoUsuario.lower() == "mujer":
            rango_min, rango_max = 12, 16
        elif SexoUsuario.lower() == "hombre":
            rango_min, rango_max = 14, 18
        else:
            return "Error: Género no válido. Use 'hombre' o 'mujer'."
    else:
        return "Error: Edad no válida."

    if NivelHemoglobina < rango_min:
        return "Resultado: POSITIVO para anemia."
    else:
        return "Resultado: NEGATIVO para anemia."

EdadRecibida = int(input("Ingrese su edad en años: ")) / 12
SexoUsario = input("Ingrese el sexo (hombre/mujer): ").strip().lower()
NivelHemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

resultado = determinar_anemia(EdadRecibida, SexoUsario, NivelHemoglobina)
print(resultado)
