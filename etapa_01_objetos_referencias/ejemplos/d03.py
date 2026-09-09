# -*- coding: utf-8 -*-
"""D03: Iguales no significa compartidas.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

a = [1, 2]
b = a
c = [1, 2]
print(a == c)
print(a is c)
print(a is b)
print(id(a) == id(b))
