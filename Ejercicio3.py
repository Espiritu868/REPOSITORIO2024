import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicio del programa con un bucle que permite al usuario realizar operaciones múltiples o salir
while True:
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú

    # Mostramos el menú de opciones en la consola
    print("1. Realizar división")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")  # Solicitamos al usuario que elija una opción

    # Opción para realizar una división
    if opcion == "1":
        n1 = int(input("Por favor, defina el n1: "))  # Solicitamos el primer número al usuario
        n2 = int(input("Por favor, defina el n2: "))  # Solicitamos el segundo número al usuario

        # Verificamos que el divisor no sea cero antes de realizar la división
        if n2 == 0:
            print("Error: No se puede dividir entre cero.")  # Mensaje de error si el divisor es cero
        else:
            r = n1 / n2  # Realizamos la división
            if r.is_integer():  # Comprobamos si el resultado es un número entero
                r = int(r)  # Convertimos el resultado a entero
            print(f"El resultado de la división de {n1} / {n2} es: {r}")  # Mostramos el resultado
    # Opción para salir del programa
    elif opcion == "2":
        print("Saliendo del programa...")  # Mensaje de salida
        break  # Salimos del bucle y terminamos el programa
    else:
        print("Opción inválida, por favor intente de nuevo.")  # Mensaje de error si la opción no es válida

    input("Presione Enter para continuar...")  # Pausa antes de volver a mostrar el menú


