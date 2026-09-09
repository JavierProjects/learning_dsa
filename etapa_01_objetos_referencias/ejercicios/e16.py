# -*- coding: utf-8 -*-
"""E16: Construcción con un ciclo.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

matrix = []
for _ in range(3):
    matrix.append([0] * 3)
matrix[0][0] = 1
print(matrix)
print(matrix[0] is matrix[1])
