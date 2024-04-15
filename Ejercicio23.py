
while True:
    nombre = input("Introduce tu nombre: ")
    if nombre:
        print(nombre.upper() + " tiene " + str(len(nombre)) + " letras.")
        break
    else:
        print("Por favor, introduce un nombre válido.")