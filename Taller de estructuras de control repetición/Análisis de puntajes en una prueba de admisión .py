# Análisis de puntajes en una prueba de admisión 
def main():
    estudiantes = []
    puntajes = []
    
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        
        try:
            puntaje = float(input(f"Ingrese el puntaje de {nombre}: "))
            estudiantes.append((nombre, puntaje))
            puntajes.append(puntaje)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el puntaje.")
    
    if not estudiantes:
        print("No se ingresaron datos de estudiantes.")
        return
    

    max_puntaje = max(puntajes)
    min_puntaje = min(puntajes)
    promedio = sum(puntajes) / len(puntajes)
    
    estudiante_max = [nombre for nombre, puntaje in estudiantes if puntaje == max_puntaje]
    estudiante_min = [nombre for nombre, puntaje in estudiantes if puntaje == min_puntaje]
    
    inferiores = sum(1 for p in puntajes if p < promedio) / len(puntajes) * 100
    superiores = sum(1 for p in puntajes if p > promedio) / len(puntajes) * 100
    
  
    print("\nResultados del análisis:")
    print(f"Estudiante(s) con el puntaje más alto ({max_puntaje}): {', '.join(estudiante_max)}")
    print(f"Estudiante(s) con el puntaje más bajo ({min_puntaje}): {', '.join(estudiante_min)}")
    print(f"Puntaje máximo obtenido: {max_puntaje}")
    print(f"Puntaje mínimo obtenido: {min_puntaje}")
    print(f"Promedio de todos los puntajes: {promedio:.2f}")
    print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {inferiores:.2f}%")
    print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {superiores:.2f}%")

if __name__ == "__main__":
    main()