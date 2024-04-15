import re

def obtener_numero_telefono():
    while True:
        telefono = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx (por ejemplo, +34-123456789-12): ")
        # Uso de expresiones regulares para validar y extraer el número de teléfono
        patron = r"\+\d{2}-\d{9}-\d{2}"
        if re.fullmatch(patron, telefono):
            # Extraer solo el número de teléfono sin código de país ni últimos dos dígitos
            numero = re.search(r"(?<=-)\d{9}(?=-)", telefono).group()
            return numero
        else:
            print("Formato de número de teléfono incorrecto. Por favor, intenta de nuevo.")

numero_telefono = obtener_numero_telefono()
print("El número de teléfono es:", numero_telefono)
