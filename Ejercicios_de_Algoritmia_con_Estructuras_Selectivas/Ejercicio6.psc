Algoritmo Ejercicio6
	Escribir "Ingrese un año"
	Leer Año
	si (Año % 4 = 0 y Año % 100 <> 0) o (Año % 400 = 0) Entonces
		Escribir "Es biciesto"
	sino
			Escribir "No es biciesto"
	FinSi
FinAlgoritmo 