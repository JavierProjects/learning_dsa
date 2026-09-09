# -*- coding: utf-8 -*-
"""E11: Una copia y un alias.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

original = [10, 20]
copia = original.copy()
alias = original
copia.append(30)
alias[0] = 99
print(original)
print(copia)
