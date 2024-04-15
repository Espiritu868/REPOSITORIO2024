name = input("Escribe tu nombre: ")
n = input("Escribe un numero entero: ")

while not n.isdigit():
    print("Error: Debes escribir un número entero.")
    n = input("Escribe un numero entero: ")

n = int(n)
print((name + "\n") * n)
