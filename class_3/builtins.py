jugadores = [
    {"nombre": "Ana",    "victorias": 8, "puntos": 240, "tiempo_total": 1820},
    {"nombre": "Luis",   "victorias": 8, "puntos": 240, "tiempo_total": 1750},
    {"nombre": "María",  "victorias": 9, "puntos": 270, "tiempo_total": 2100},
    {"nombre": "Carlos", "victorias": 8, "puntos": 220, "tiempo_total": 1900},
    {"nombre": "Sofía",  "victorias": 9, "puntos": 270, "tiempo_total": 1980},
]

ranking = sorted(jugadores,
                 key=lambda jugador: (jugador["puntos"], -jugador["tiempo_total"]),
                 reverse=True)

print("\nRanking del torneo:")
for pos, j in enumerate(ranking, 1):
    print(f"  {pos}. {j['nombre']:8} | V:{j['victorias']} | Pts:{j['puntos']} | t:{j['tiempo_total']}s")


usuarios_raw = [
    "ANA TORRES",
    "luis GARCIA",
    "MARÍA LÓPEZ",
    "carlos RAMÍREZ",
]



