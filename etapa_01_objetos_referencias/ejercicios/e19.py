# -*- coding: utf-8 -*-
"""E19: Copiar una lista que contiene una tupla.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

original = [([1], "A")]
copia = original.copy()
copia[0][0].append(2)
print(original)
print(copia)
print(original[0] is copia[0])
