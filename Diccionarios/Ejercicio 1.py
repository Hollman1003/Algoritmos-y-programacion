#Ejercicio 1

Lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
Diccionario = {}
for i in Lista:
    Diccionario.update({i:Lista.count(i)})
    print (Diccionario)