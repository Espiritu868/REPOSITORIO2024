import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print("Menú de opciones:")
    print("1. Menor de 4 años")
    print("2. Entre 4 y 18 años")
    print("3. Mayor de 18 años")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        edad = 3  # Menor de 4 años
    elif opcion == "2":
        edad = 4  # Entre 4 y 18 años
    elif opcion == "3":
        edad = 19  # Mayor de 18 años
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        continue

    if edad < 4: 
        print("Entrada Gratis")
    elif 4 <= edad <= 18: 
        print("Entrada: 5€")
    elif edad > 18: 
        print("Entrada: 10€")
    
    input("Presiona Enter para continuar...")
