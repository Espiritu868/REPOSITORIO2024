# Inicio del programa
while True:
    # Menú de opciones
    print("\nMenú de opciones:")
    print("1. Verificar si un número es par o impar")
    print("2. Verificar si un número es entero o decimal")
    print("3. Salir")
    
    # Elección del usuario
    opcion = input("Elija una opción (1-3): ")
    
    # Opción 1: Verificar paridad
    if opcion == "1":
        n = float(input("Ingrese un número entero: "))
        print("El número es par." if n.is_integer() and n % 2 == 0 else "El número es impar.")
    
    # Opción 2: Verificar tipo de número
    elif opcion == "2":
        n = float(input("Ingrese un número: "))
        print("El número es entero." if n.is_integer() else "El número es decimal.")
    
    # Opción 3: Salir del programa
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    # Opción inválida
    else:
        print("Opción no válida, intente de nuevo.")