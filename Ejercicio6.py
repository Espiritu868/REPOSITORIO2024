import os

# Definimos una función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicializamos una variable para controlar el ciclo while
continuar = True

# Iniciamos el ciclo while
while continuar:
    # Limpiamos la consola cada vez que iniciamos el ciclo
    limpiar_consola()
    
    # Pedimos el nombre del alumno
    name = str(input("Nombre del Alumno: "))
    
    # Mostramos el menú para que el usuario elija el sexo
    print("Seleccione el sexo del alumno:")
    print("1. Hombre (H)")
    print("2. Mujer (M)")
    opcion = int(input("Opción: "))
    
    # Asignamos el valor de sexo de acuerdo a la opción seleccionada
    if opcion == 1:
        sex = "H"
    elif opcion == 2:
        sex = "M"
    else:
        print("Opción inválida. Intente de nuevo.")
        continue
    
    # Comprobamos si el alumno pertenece al grupo A o B
    if (sex == "M" and name.lower() < "m") or (sex == "H" and name.lower() > "n"): 
        grupo = "A"
    else: 
        grupo = "B"
    
    # Mostramos el grupo al que pertenece el alumno
    print("El grupo del alumno es: " + grupo)
    
    # Preguntamos si se desea continuar o salir del programa
    salir = input("¿Desea ingresar otro alumno? (S/N): ")
    if salir.lower() == "n":
        continuar = False

# Fin del programa
print("Programa finalizado.")