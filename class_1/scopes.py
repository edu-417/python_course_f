TASA_IVA = 0.18   # constante global (convención: MAYÚSCULAS)
 
def calcular_precio_final(precio_base):

    impuesto = precio_base * TASA_IVA   # lee global — OK
    total    = precio_base + impuesto

    return total

print(calcular_precio_final(15))


