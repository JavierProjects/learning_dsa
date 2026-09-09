# -*- coding: utf-8 -*-
"""S04: Una solución con copia profunda.

Consulta después de intentar la práctica y justificar tu propuesta.
"""

import copy

def preparar_equipo(equipo):
    nuevo = copy.deepcopy(equipo)
    nuevo["nombre"] = "Pruebas"
    nuevo["miembros"][0]["edad"] = 99
    return nuevo

ana = {"nombre": "Ana", "edad": 25}
original = {"nombre": "Desarrollo", "miembros": [ana]}
copia = preparar_equipo(original)
print(original["nombre"], ana["edad"])
print(copia["nombre"], copia["miembros"][0]["edad"])
print(original is copia)
print(original["miembros"] is copia["miembros"])
print(ana is copia["miembros"][0])
