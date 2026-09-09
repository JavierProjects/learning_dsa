# -*- coding: utf-8 -*-
"""D05: Dos funciones sobre el mismo argumento.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

def add_item(lst):
    lst.append("X")

def reset_list(lst):
    lst = []

my_list = []
add_item(my_list)
reset_list(my_list)
print(my_list)
