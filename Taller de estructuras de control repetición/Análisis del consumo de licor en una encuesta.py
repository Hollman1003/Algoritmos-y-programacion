# Análisis del consumo de licor en una encuesta

# Inicializar contadores y variables
consumen_licor = 0
mujeres_menores = 0
hombres_sin_aguardiente = 0
edad_total_cerveza = 0
cerveza_contador = 0
whisky_contador = 0
total_encuestados = 0

while True:
    # Solicitar datos
    consume = input("¿Consume licor? (Sí/No): ").strip().lower()
    if consume == "si":
        consumen_licor += 1
        licor = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
    else:
        licor = 0  # No consume licor
    
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M/F): ").strip().upper()
    total_encuestados += 1
    
    # Contar mujeres menores de edad
    if sexo == "F" and edad < 18:
        mujeres_menores += 1
    
    # Contar hombres que no consumen aguardiente y tienen entre 20 y 25 años
    if sexo == "M" and (licor != 1) and (20 <= edad <= 25):
        hombres_sin_aguardiente += 1
    
    # Acumular datos para cerveza
    if licor == 3:
        edad_total_cerveza += edad
        cerveza_contador += 1
    
    # Contar consumidores de whisky
    if licor == 5:
        whisky_contador += 1
    
    # Preguntar si desea continuar
    continuar = input("¿Desea continuar con la encuesta? (Sí/No): ").strip().lower()
    if continuar != "si":
        break

# Calcular estadísticas
promedio_edad_cerveza = edad_total_cerveza / cerveza_contador if cerveza_contador > 0 else 0
porcentaje_whisky = (whisky_contador / total_encuestados) * 100 if total_encuestados > 0 else 0

# Mostrar resultados
print("Total de personas que consumen licor:", consumen_licor)
print("Total de mujeres menores de edad:", mujeres_menores)
print("Total de hombres (20-25 años) que no consumen aguardiente:", hombres_sin_aguardiente)
print("Promedio de edad de quienes consumen cerveza:", promedio_edad_cerveza)
print("Porcentaje de personas que consumen whisky respecto al total encuestado:", porcentaje_whisky, "%")