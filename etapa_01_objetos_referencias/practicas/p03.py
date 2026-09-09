# -*- coding: utf-8 -*-
"""P03: Programa inicial.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

matrix = [[0] * 3] * 3
copia = matrix.copy()
copia[0][0] = 1
print(matrix)
print(copia)
print(matrix is copia)
print(matrix[0] is copia[0])
