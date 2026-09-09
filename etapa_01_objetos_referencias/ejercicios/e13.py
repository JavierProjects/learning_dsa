# -*- coding: utf-8 -*-
"""E13: Sustituir una fila de la copia.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

original = [[1, 2], [3, 4]]
copia = original.copy()
copia[0] = [99, 2]
print(original)
print(copia)
print(original[1] is copia[1])
