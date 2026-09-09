# -*- coding: utf-8 -*-
"""E18: Una copia profunda conserva un alias interno.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

import copy

fila = [0]
original = [fila, fila]
copia = copy.deepcopy(original)
copia[0][0] = 7
print(original)
print(copia)
print(copia[0] is copia[1])
print(copia[0] is fila)
