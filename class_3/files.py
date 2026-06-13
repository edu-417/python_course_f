archivo_txt = "notas.txt"
 
file = open(archivo_txt, "w", encoding="utf-8")
file.write("Primera nota: Python es genial.\n")
file.write("Segunda nota: Los archivos son útiles.\n")
file.write("Tercera nota: Practicar es la clave.\n")
file.close()

print("Archivo '{archivo_txt}' creado en modo 'w'.")


file = open(archivo_txt, "r", encoding="utf-8")
content = file.read()          # Lee TODO el archivo como un string
file.close()

print(content)

file = open(archivo_txt, "r", encoding="utf-8")
lines = file.readlines()        # Devuelve una LISTA de strings
file.close()
 
print("Líneas con readlines():")
for i, line in enumerate(lines, start=1):
    print(f"  Línea {i}: {line.strip()}")



with open(archivo_txt, "r", encoding="utf-8") as file:
    lines = file.readlines()        # Devuelve una LISTA de strings
    print("Líneas con readlines():")
    for i, line in enumerate(lines, start=1):
        print(f"  Línea {i}: {line.strip()}")