name = input("Escribe tu nombre: ")
print(name.lower())
print(name.upper())
continuar = 's'

while continuar.lower() == 's':
    name = input("Escribe tu nombre: ")
    print(name.lower())
    print(name.upper())
    name = input("Escribe tu nombre: ")

    continuar = input("¿Quieres escribir otro nombre? (s/n): ")

print("Gracias por usar el programa.")
print(name.lower())
print(name.upper())
print(name.title())

continuar = input("¿Quieres escribir otro nombre? (s/n): ")

print("Gracias por usar el programa.")
