def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
# Solicitamos la edad del usuario y la almacenamos como un entero
edad = int(input("Por favor, digite su edad: "))
# Solicitamos el salario mensual del usuario y lo almacenamos como un número flotante para permitir decimales
ingreso = float(input("Por favor, ingrese su salario mensual (€): "))

# Verificamos que la edad y el ingreso sean valores válidos (mayores a 0)
if edad <= 0 or ingreso < 0:
    print("Por favor, ingrese valores válidos.")  # Mensaje de error si los valores no son válidos
elif edad > 16 and ingreso >= 1000:  # Condición para tener derecho a tributar ajustada a los requisitos
    print("Usted tiene derecho a tributar.")  # Mensaje si cumple con las condiciones para tributar
else: 
    print("Lo sentimos, pero no tiene derecho a tributar.")  # Mensaje si no cumple con las condiciones para tributar