# -*- coding: utf-8 -*-
"""D07: Dos exteriores y una lista interior.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

a = [1, 2]
b = [a, a]
c = b.copy()
c[0][0] = 99
print(a)
print(b)
print(c)
print(b is c)
