# -*- coding: utf-8 -*-
"""E05: Tres comparaciones.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

a = [5]
b = [5]
c = a
print(a == b)
print(a is b)
print(b is c)
print(id(a) == id(c))
