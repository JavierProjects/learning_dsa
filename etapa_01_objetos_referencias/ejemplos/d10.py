# -*- coding: utf-8 -*-
"""D10: Una tupla y su lista interior.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

datos = ([1, 2], "grupo A")
alias = datos
datos[0].append(3)
print(datos)
print(alias is datos)
