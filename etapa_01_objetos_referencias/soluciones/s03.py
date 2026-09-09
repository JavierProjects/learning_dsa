# -*- coding: utf-8 -*-
"""S03: Solución de la variante B.

Consulta después de intentar la práctica y justificar tu propuesta.
"""

matrix = [[0] * 3 for _ in range(3)]
copia = [fila.copy() for fila in matrix]
copia[0][0] = 1
print(matrix)
print(copia)
print(copia[0] is copia[1])
print(matrix[0] is copia[0])
