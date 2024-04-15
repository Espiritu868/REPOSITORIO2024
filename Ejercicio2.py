import getpass
import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Contraseña correcta
Password = "hola"

# Inicio del programa
# NOTA, SI QUIERE SALIR DEL PROGRAMA SIN ESCRIBIR LA CONTRASEÑA, ESCRIBA LA FRASE "NECESITO SALIR DEL PROGRAMA" EN MAYUSCULAS
while True:
    # Limpia la pantalla antes de solicitar la contraseña
    limpiar_pantalla()
    
    # Solicitamos la contraseña sin mostrarla en pantalla
    PUser = getpass.getpass("Por favor, introduzca su contraseña: ")

    # Comparamos la contraseña ingresada con la correcta
    if PUser.lower() == Password:
        print("Su contraseña es correcta.")
        input("Presione una tecla para cerrar el programa.")
        break
    elif PUser.lower() == "necesito salir del programa":
        print("Saliendo del programa...")
        break
    else:
        print("Contraseña incorrecta, intentelo de nuevo.")
        input("Presione Enter para continuar...")

# Nota: getpass no muestra los caracteres en la terminal, incluidos los '*', por razones de seguridad.




