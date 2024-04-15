base = float(input("Introduce la base imponible de la factura: "))

def aplica_iva(base, iva=21):
    return base + base * iva / 100

total_con_iva = aplica_iva(base)
print("Total con IVA:", total_con_iva)
