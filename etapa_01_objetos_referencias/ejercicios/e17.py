# -*- coding: utf-8 -*-
"""E17: Una lista dentro de un diccionario.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

import copy

original = {"notas": [8, 9]}
copia = copy.deepcopy(original)
copia["notas"].append(10)
print(original["notas"])
print(copia["notas"])
