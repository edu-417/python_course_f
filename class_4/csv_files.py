import csv

csv_file = "estudiantes.csv"

headers = ["nombre", "edad", "nota", "aprobado"]

rows = [
    ["Ana García",    22, 18.5, True],
    ["Bruno López",   19, 12.0, False],
    ["Carla Mendez",  21, 16.0, True],
    ["Diego Torres",  23, 14.5, True],
    ["Elena Ríos",    20,  9.0, False],
]

with open(csv_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

    print(f"Archivo '{csv_file}' creado con csv.writer.")


with open(csv_file, "r", newline="", encoding="utf-8") as file:

    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:
        nombre, edad, nota, aprobado = row
        print(f"{nombre:<20} {edad:>5} {nota:>6} {aprobado:>10}")