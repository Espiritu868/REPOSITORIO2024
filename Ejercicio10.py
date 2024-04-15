import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Función para mostrar el menú de opciones
def show_menu():
    print("Menu de Opciones:")
    print("1. Vegetariana")
    print("2. No Vegetariana")
    print("3. Salir")
    return input("Introduce el tipo de pizza que deseas (1/2/3): ")
# Función para pizza vegetariana
def vegetarian_pizza():
    print("Ingredientes pizzas vegetarianas: ")
    print("1.- Pimiento.")
    print("2.- Tofu.")
    ingrediente = input("Introduce el tipo de ingrediente que deseas (1/2): ")
    print("Pizza vegetariana con mozzarella, tomate y ", end= "")
    if ingrediente == "1": 
        print("Pimiento")
    else: 
        print("Tofu")
# Función para pizza no vegetariana
def non_vegetarian_pizza():
    print("Ingredientes de pizza No Vegetariana: ")
    print("1. Peperoni ")
    print("2. Jamón ")
    print("3. Salmón ")
    ingrediente = input("Introduce el ingrediente que deseas (1/2/3): ")
    print("Pizza no vegetariana con mozarella, tomate y ", end="")
    if ingrediente == "1":
        print("Peperoni")
    elif ingrediente == "2":
        print("Jamón")
    else: 
        print("Salmón")
# Ciclo while para repetir el menú hasta que el usuario decida salir
while True:
    clear_screen()
    opcion = show_menu()
    if opcion == "1":
        vegetarian_pizza()
    elif opcion == "2":
        non_vegetarian_pizza()
    elif opcion == "3":
        print("Gracias por usar el programa.")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
    input("Presiona Enter para continuar...") # Pausa antes de limpiar la pantalla
