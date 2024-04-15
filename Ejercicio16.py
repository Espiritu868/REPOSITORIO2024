#CALCULADORA DE MASA CORPORAL

peso = float(input("Peso (kg):"))
estatura = float(input("Estatura (mt):"))
imc = round(float(peso) /float(estatura)**2,2)
print(f"Tu indice de masa corporal es: {imc}")