# -*- coding: utf-8 -*-
"""E12: Copiar mediante un corte.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

a = ["A", "B"]
b = a[:]
print(a == b)
print(a is b)
b.clear()
print(a)
print(b)
