# -*- coding: utf-8 -*-
"""D09: Separar también las filas.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

import copy

original = [[1, 2], [3, 4]]
profunda = copy.deepcopy(original)
profunda[0][0] = 99
print(original)
print(profunda)
print(original[0] is profunda[0])
