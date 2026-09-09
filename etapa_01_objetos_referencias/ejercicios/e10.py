# -*- coding: utf-8 -*-
"""E10: Actualizar y reiniciar un diccionario.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

def update_dict(d):
    d["key"] = "value"

def reset_dict(d):
    d = {}

my_dict = {}
update_dict(my_dict)
reset_dict(my_dict)
print(my_dict)
