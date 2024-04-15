import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bonificacion = 2400
inaceptable = 0 
aceptable = 0.4 
meritorio = 0.6 

while True:
    clear_screen()
    print("Menú de opciones:")
    print("1. Inaceptable")
    print("2. Aceptable")
    print("3. Meritorio")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        puntos = inaceptable
    elif opcion == "2":
        puntos = aceptable
    elif opcion == "3":
        puntos = meritorio
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        continue

    if puntos == inaceptable: 
        nivel = "inaceptable" 
    elif puntos == aceptable: 
        nivel = "aceptable"
    elif puntos >= 0.6: 
        nivel = "meritorio" 
    else: 
        nivel = ""

    if nivel == "":
        print("Esta puntuación no es válida.")
    else: 
        print("Tu nivel de rendimiento es %s" % nivel)
        print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))
    
    input("Presiona Enter para continuar...")

            