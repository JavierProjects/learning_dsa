# -*- coding: utf-8 -*-
"""S02: Solución de la variante B.

Consulta después de intentar la práctica y justificar tu propuesta.
"""

def agregar_final(datos):
    return datos + [99]

original = [1, 2]
resultado = agregar_final(original)
print(original)
print(resultado)
print(original is resultado)
