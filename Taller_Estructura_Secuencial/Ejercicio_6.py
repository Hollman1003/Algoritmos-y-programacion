# Ejercicio 6 ________________________________

# Ejercicio_6_PorcentajePersonas

Cantidad_Hombres = int(input("¿Cuántos hombres hay en el grupo? "))

Cantidad_Mujeres = int(input("¿Cuántas mujeres hay en el grupo? "))

Total_Personas = Cantidad_Hombres + Cantidad_Mujeres

Porcentaje_Hombres = (Cantidad_Hombres * 100) / Total_Personas
Porcentaje_Mujeres = (Cantidad_Mujeres * 100) / Total_Personas

print("El porcentaje de hombres en el grupo es:", Cantidad_Hombres, "%")
print("El porcentaje de mujeres en el grupo es:", Porcentaje_Mujeres, "%")