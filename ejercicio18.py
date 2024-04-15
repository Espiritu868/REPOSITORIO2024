#PROGRAMA PARA CALCULAR CAPITAL FINAL

import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicio del programa
while True: # Ciclo while para repetir el programa hasta que el usuario decida salir
    # Solicitar datos al usuario
    cantidad = float(input("Cantidad a invertir: "))
    interes = float(input("Interes porcentual anual: "))
    años = int(input("Años: "))
    
    # Calcular el capital final
    cf = str(round(cantidad * (interes / 100 + 1) ** años, 2))
    
    # Mostrar el resultado
    print(f"Capital final: {cf}")
    
    # Preguntar al usuario si desea realizar otra operación
    opcion = input("¿Desea realizar otra operación? (s/n): ")
    
    # Si el usuario no desea continuar, salir del programa
    if opcion.lower() == 'n':
        break
    
    # Limpiar la pantalla antes de volver a iniciar
    limpiar_pantalla()

# Mensaje de despedida
print("Gracias por utilizar el programa. ¡Hasta luego!")
