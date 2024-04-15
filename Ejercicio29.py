while True:
    nacimiento = input("Escribe la fecha en que naciste 'dd/mm/aaaa': ")
    if len(nacimiento) == 10 and nacimiento[2] == '/' and nacimiento[5] == '/':
        print('Dia:', nacimiento[:2])
        print('Mes:', nacimiento[3:5])
        print('Año:', nacimiento[6:])
        break
    else:
        print("Formato incorrecto, por favor ingresa la fecha en el formato 'dd/mm/aaaa'.")
