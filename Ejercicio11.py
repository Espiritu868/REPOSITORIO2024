import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("Hola Mundo")