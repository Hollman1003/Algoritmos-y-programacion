#Ejercicio 2


Diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}

Lista_Sin_Duplicados = []
for valor in Diccionario.values():
    if valor not in Lista_Sin_Duplicados:
        Lista_Sin_Duplicados.append(valor)

print(Lista_Sin_Duplicados)