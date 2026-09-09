# -*- coding: utf-8 -*-
"""D06: Una copia con elementos inmutables.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

original = [1, 2, "hola", True]
copia = original.copy()
copia[0] = 99
print(original)
print(copia)
print(original is copia)
