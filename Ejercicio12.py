import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
nombre = str(input("Cual es tu nombre?:" ))
print(f"Hola, {nombre}")