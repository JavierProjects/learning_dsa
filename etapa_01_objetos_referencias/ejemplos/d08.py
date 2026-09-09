# -*- coding: utf-8 -*-
"""D08: Una fila compartida tres veces.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)
print(matrix[0] is matrix[1])
