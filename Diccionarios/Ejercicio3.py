#Ejercicio 3

usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        nombre = usuarios[usuario]["nombre"]
        apellido = usuarios[usuario]["apellido"]
        print(f"Bienvenido, {nombre} {apellido}!")
        break
    else:
        print("Usuario o contraseña incorrectos.")
        intentos += 1

if intentos == max_intentos:
    print("Has superado el número máximo de intentos.")