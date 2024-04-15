
continuar = True
while continuar:
    correo = input("Introduce tu correo electronico: (Ejemplo: holasoycorreo@gmail.com)")
    print("Otro correo electronico similar al tuyo es:", correo[0:-9], "ceu.es")
    respuesta = input("¿Deseas introducir otro correo? (s/n): ")
    if respuesta.lower() != 's':
        continuar = False
