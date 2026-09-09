# -*- coding: utf-8 -*-
"""E06: Objetos vacíos.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

x = []
y = x
z = []
print(x == z)
print(x is y)
print(id(y) == id(z))
