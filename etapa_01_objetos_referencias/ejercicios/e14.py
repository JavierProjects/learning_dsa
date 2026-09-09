# -*- coding: utf-8 -*-
"""E14: Modificar una fila compartida.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

original = [[1, 2], [3, 4]]
copia = original.copy()
copia[0][0] = 99
print(original)
print(copia)
print(original[0] is copia[0])
