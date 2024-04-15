import os
# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
# Función para calcular el tipo impositivo
def calcular_impositivo(renta):
    if renta < 10000: 
        return 5
    elif renta < 20000: 
        return 15
    elif renta < 35000: 
        return 20
    elif renta < 60000: 
        return 30
    else: 
        return 45

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Renta menor a 10000")
    print("2. Renta mayor o igual a 10000 y menor a 20000")
    print("3. Renta mayor o igual a 20000 y menor a 35000")
    print("4. Renta mayor o igual a 35000 y menor a 60000")
    print("5. Renta mayor a 60000")
    print("6. Salir")
    return int(input("Seleccione una opción: "))

# Función principal
def main():
    continuar = True
    while continuar:
        limpiar_pantalla()
        opcion = mostrar_menu()
        if opcion == 6:
            continuar = False
        elif 1 <= opcion <= 5:
            rentas = [5000, 15000, 25000, 45000, 70000]  # Valores aproximados para cada opción
            renta = rentas[opcion - 1]
            impo = calcular_impositivo(renta)
            print(f"El tipo impositivo que le corresponde es: {impo}%")
        else:
            print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para continuar...")

# Ejecución del programa
if __name__ == "__main__":
    main()
