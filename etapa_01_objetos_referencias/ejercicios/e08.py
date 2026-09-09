# -*- coding: utf-8 -*-
"""E08: Vaciar y después reasignar.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

x = [1, 2]
y = x
y.clear()
y = [9]
print(x)
print(y)
print(x is y)
