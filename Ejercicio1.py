import os

# Función que limpia la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función que determina si es mayor de edad
def es_mayor_de_edad(anio):
    return anio <= 21

# Inicio del programa
while True:
    limpiar_pantalla()
    print("1. Ingresar edad\n2. Ingresar número de identidad\n3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        edad = int(input("Ingrese su edad: "))
        mensaje = "mayor" if es_mayor_de_edad(edad) else "menor"
        print(f"Usted es {mensaje} de edad.")
    elif opcion == "2":
        num_id = input("Ingrese su número de identidad: ")
        anio_nacimiento = int(num_id[:2])
        mensaje = "mayor" if es_mayor_de_edad(anio_nacimiento) else "menor"
        print(f"Usted es {mensaje} de edad.")
    elif opcion == "3" or opcion.lower() == "salir":
        break
    else:
        print("Opción inválida.")
    
    input("Presione Enter para continuar...")

