# -*- coding: utf-8 -*-
"""E15: Una variable explícita.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

a = [0]
matrix = [a * 3] * 3
matrix[0][0] = 1
print(a)
print(matrix)
print(matrix[0] is matrix[2])
