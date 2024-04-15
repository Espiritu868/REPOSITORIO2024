#PROGRAMA PARA CALCULAR PESO TOTAL DE PAQUETE
import os

# Inicia ciclo while para repetir el proceso
while True:
    # Solicita la cantidad de payasos y muñecas vendidos
    payaso = int(input("Digite la cantidad de payasos vendidos: "))
    muñeca = int(input("Digite la cantidad de muñecas vendidas: "))
    
    # Calcula el peso total de los payasos y muñecas
    ppayaso = payaso * 112
    pmuñeca = muñeca * 75 
    total = ppayaso + pmuñeca 
    
    # Muestra el peso total del paquete
    print(f"El peso total del paquete será de: {total}")
    
    # Pregunta al usuario si desea calcular otro paquete
    continuar = input("¿Desea calcular otro paquete? (s/n): ")
    
    # Si la respuesta no es 's', termina el ciclo
    if continuar.lower() != 's':
        break
    
    # Limpia la pantalla para una nueva entrada de datos
    os.system('cls' if os.name == 'nt' else 'clear')
