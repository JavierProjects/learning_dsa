# -*- coding: utf-8 -*-
"""E20: Dos carros comparten motor.

Lee la consigna y escribe tu predicción en la guía antes de ejecutar.
"""

motor = {"caballos": 200}
carro1 = {"marca": "Toyota", "motor": motor}
carro2 = carro1.copy()
carro2["marca"] = "Honda"
carro2["motor"]["caballos"] = 300
print(carro1["marca"])
print(carro1["motor"]["caballos"])
print(carro1["motor"] is carro2["motor"])
