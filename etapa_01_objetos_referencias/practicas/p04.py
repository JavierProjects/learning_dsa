# -*- coding: utf-8 -*-
"""P04: Programa inicial.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

def preparar_equipo(equipo):
    nuevo = equipo.copy()
    nuevo["nombre"] = "Pruebas"
    nuevo["miembros"][0]["edad"] = 99
    return nuevo

ana = {"nombre": "Ana", "edad": 25}
original = {"nombre": "Desarrollo", "miembros": [ana]}
copia = preparar_equipo(original)
print(original["nombre"], ana["edad"])
print(copia["nombre"], copia["miembros"][0]["edad"])
