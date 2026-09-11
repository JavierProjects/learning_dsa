"""Variaciones y distractores de la web. Las salidas se verifican con Python.

El caso inicial de cada ejercicio siempre procede de contenido.py.
Las diez variaciones del PDF se conservan; la web añade otras diez para que
cada ejercicio tenga una segunda pestaña.
"""


VARIACIONES = {
    "e01": {
        "change": 'Reemplaza la segunda línea por `texto = texto.upper()` y muestra solo `texto`.',
        "replace": [('mayusculas = texto.upper()\nprint(texto)\nprint(mayusculas)', 'texto = texto.upper()\nprint(texto)')],
        "expected": "HOLA\n",
        "prompt": '¿Se modificó la cadena original o cambió la cadena que señala `texto`? ¿Las cadenas siguen siendo inmutables?',
        "answer": '`texto` pasa a señalar la cadena `HOLA`. La cadena original conserva su contenido. Cambiar la asignación no cambia la mutabilidad de `str`.',
    },
    "e02": {
        "change": 'En lugar de cambiar la edad, cambia `alumno["nombre"]` a `"Luis"`.',
        "replace": [('alumno["edad"] = 19', 'alumno["nombre"] = "Luis"')],
        "expected": "Luis\n18\n",
        "prompt": '¿Por qué la edad conserva su valor? ¿Cambió el diccionario o se modificó la cadena `"Ana"`?',
        "answer": 'Cambia la entrada `"nombre"` del diccionario y se conserva la entrada `"edad"`. La cadena `"Ana"` no se modifica: esa posición del diccionario pasa a señalar `"Luis"`.',
    },
    "e03": {
        "change": 'Cambia solo `b = a` por `b = [7]`. Mantén `c = b`.',
        "replace": [('b = a', 'b = [7]')],
        "expected": "[7]\n[7, 8]\n[7, 8]\n",
        "prompt": 'Describe qué nombres comparten una lista y cuántas listas se crearon.',
        "answer": '`a` señala una lista; `b` y `c` comparten otra. Se crearon dos listas. Solo la segunda recibe el `8`.',
    },
    "e04": {
        "change": 'Sustituye la última asignación por `b = b`.',
        "replace": [('b = b + 1', 'b = b')],
        "expected": "7\n7\n",
        "prompt": '¿La asignación `b = b` hace que `b` señale otro objeto? Explícalo con las tarjetas.',
        "answer": 'No. La etiqueta `b` vuelve a quedar en la misma tarjeta, la del `7`. Hay una asignación, pero no se cambia de objeto.',
    },
    "e05": {
        "change": 'Cambia únicamente `c = a` por `c = b`.',
        "replace": [('c = a', 'c = b')],
        "expected": "True\nFalse\nTrue\nFalse\n",
        "prompt": '¿Cuáles de las cuatro respuestas cambian respecto al caso inicial? ¿Por qué?',
        "answer": 'Cambian la tercera y la cuarta. Ahora `b` y `c` señalan la misma lista, y `a` señala otra.',
    },
    "e06": {
        "change": 'Cambia la creación de `z` por `z = y`.',
        "replace": [('z = []', 'z = y')],
        "expected": "True\nTrue\nTrue\n",
        "prompt": '¿Cuántas listas existen ahora? ¿Por qué coinciden los identificadores?',
        "answer": 'Hay una sola lista, señalada por `x`, `y` y `z`. Los identificadores coinciden porque todos esos nombres te llevan al mismo objeto.',
    },
    "e07": {
        "change": 'Cambia `y += [3]` por `y = y + [3]`.',
        "replace": [('y += [3]', 'y = y + [3]')],
        "expected": "[1, 2]\n[1, 2, 3]\nFalse\n",
        "prompt": 'Explica por qué ahora `x` y `y` señalan listas distintas. Después analiza `a = 10; b = a; b += 3`: ¿qué señala cada nombre?',
        "answer": '`+` crea otra lista y `y` pasa a señalarla. En el caso de los enteros, `a` sigue señalando el `10` y `b` pasa al `13`. El entero inicial conserva su valor.',
    },
    "e08": {
        "change": 'Cambia `y.clear()` por `y = []` y conserva el resto.',
        "replace": [('y.clear()', 'y = []')],
        "expected": "[1, 2]\n[9]\nFalse\n",
        "prompt": '¿Se llegó a vaciar la lista de `x`? Describe las dos asignaciones a `y`.',
        "answer": 'La lista de `x` conserva `[1, 2]`. Primero `y` pasa a señalar una lista vacía y luego otra con `[9]`. Ninguna de esas asignaciones modifica la lista inicial.',
    },
    "e09": {
        "change": 'Devuelve la lista resultante. Primero ignora el resultado y luego guárdalo en `numbers`.',
        "replace": [('lst = lst + [99]', 'return lst + [99]')],
        "append": 'numbers = modify(numbers)\nprint(numbers)\n',
        "expected": "[1, 2, 3]\n[1, 2, 3, 99]\n",
        "prompt": '¿Por qué las dos llamadas producen efectos distintos sobre lo que señala `numbers`?',
        "answer": 'La primera llamada devuelve una lista que no guardamos. La segunda también devuelve otra lista, pero ahora la asignamos a `numbers`. La función no modifica la lista recibida.',
    },
    "e10": {
        "change": 'En `reset_dict()`, reemplaza `d = {}` por `d.clear()`.',
        "replace": [('    d = {}', '    d.clear()')],
        "expected": "{}\n",
        "prompt": '¿Qué hace que ahora el cambio sea visible mediante `my_dict`?',
        "answer": '`d.clear()` vacía el diccionario compartido. El parámetro `d` y la variable `my_dict` siguen señalando ese mismo objeto.',
    },
    "e11": {
        "change": 'Reemplaza `alias = original` por `alias = copia`.',
        "replace": [('alias = original', 'alias = copia')],
        "expected": "[10, 20]\n[99, 20, 30]\n",
        "prompt": '¿Qué lista recibe los dos cambios? ¿Qué nombres la comparten?',
        "answer": '`copia` y `alias` señalan la misma lista nueva, que recibe el `30` y el `99`. La lista de `original` conserva sus valores.',
    },
    "e12": {
        "change": 'Cambia `b = a[:]` por `b = a`.',
        "replace": [('b = a[:]', 'b = a')],
        "expected": "True\nTrue\n[]\n[]\n",
        "prompt": '¿Por qué ahora vaciar la lista mediante `b` cambia lo que vemos mediante `a`?',
        "answer": 'La asignación no crea otra lista. Los dos nombres comparten la misma, y `b.clear()` la vacía.',
    },
    "e13": {
        "change": 'Reemplaza la primera fila por otra lista con el mismo contenido: `[1, 2]`. Compara las primeras filas.',
        "replace": [('copia[0] = [99, 2]', 'copia[0] = [1, 2]'), ('original[1] is copia[1]', 'original[0] is copia[0]')],
        "expected": "[[1, 2], [3, 4]]\n[[1, 2], [3, 4]]\nFalse\n",
        "prompt": '¿Por qué las impresiones coinciden, pero las primeras filas tienen identidades distintas?',
        "answer": 'La nueva primera fila contiene los mismos números, pero es otra lista. Igual contenido no significa mismo objeto. La segunda fila sí permanece compartida.',
    },
    "e14": {
        "change": 'Reemplaza `copia[0][0] = 99` por `copia.append([5, 6])`.',
        "replace": [('copia[0][0] = 99', 'copia.append([5, 6])')],
        "expected": "[[1, 2], [3, 4]]\n[[1, 2], [3, 4], [5, 6]]\nTrue\n",
        "prompt": '¿Qué lista cambia? ¿Por qué la primera fila sigue compartida?',
        "answer": 'Cambia la lista exterior de `copia`: recibe otra fila. Sus dos primeras posiciones conservan las referencias copiadas de `original`.',
    },
    "e15": {
        "change": 'Construye las filas con `matrix = [(a * 3).copy() for _ in range(3)]`.',
        "replace": [('matrix = [a * 3] * 3', 'matrix = [(a * 3).copy() for _ in range(3)]')],
        "expected": "[0]\n[[1, 0, 0], [0, 0, 0], [0, 0, 0]]\nFalse\n",
        "prompt": '¿Hace falta `.copy()` aquí? Si `a = [0]`, ¿cuántas filas y columnas tendría `[a.copy(), a.copy(), a.copy()]`?',
        "answer": 'No hace falta: `a * 3` ya crea una fila nueva en cada vuelta. Copiar tres veces la lista `a = [0]` produciría 3 filas y 1 columna.',
    },
    "e16": {
        "change": 'Crea una sola fila antes del ciclo y agrégala en cada vuelta.',
        "replace": [('matrix = []\nfor _ in range(3):\n    matrix.append([0] * 3)', 'matrix = []\nfila = [0] * 3\nfor _ in range(3):\n    matrix.append(fila)')],
        "expected": "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\nTrue\n",
        "prompt": '¿Por qué usar un ciclo no garantiza por sí solo tener filas independientes?',
        "answer": 'El ciclo añade tres referencias a la misma fila. Para tener filas independientes, la creación de la lista debe ocurrir dentro de cada vuelta.',
    },
    "e17": {
        "change": 'Usa `original.copy()` en lugar de `copy.deepcopy(original)`.',
        "replace": [('copy.deepcopy(original)', 'original.copy()')],
        "expected": "[8, 9, 10]\n[8, 9, 10]\n",
        "prompt": '¿Qué se copió y qué sigue compartido?',
        "answer": 'Se copió el diccionario exterior. Su lista `"notas"` sigue compartida, así que el cambio se ve desde ambos diccionarios.',
    },
    "e18": {
        "change": 'Usa `copia = [elemento.copy() for elemento in original]`.',
        "replace": [('copy.deepcopy(original)', '[elemento.copy() for elemento in original]')],
        "expected": "[[0], [0]]\n[[7], [0]]\nFalse\nFalse\n",
        "prompt": '¿Por qué esta construcción separa las filas entre sí, además de separarlas de la original?',
        "answer": 'Cada vuelta ejecuta `.copy()` y crea otra lista. Las dos posiciones de `copia` terminan señalando filas distintas y ninguna es la fila original.',
    },
    "e19": {
        "change": 'Importa `copy` y realiza una copia profunda de `original`.',
        "prepend": 'import copy\n\n',
        "replace": [('original.copy()', 'copy.deepcopy(original)')],
        "expected": "[([1], 'A')]\n[([1, 2], 'A')]\nFalse\n",
        "prompt": '¿Por qué se necesita también otra tupla en esta copia, aunque las tuplas sean inmutables?',
        "answer": 'La tupla original señala la lista original. Para que la copia señale una lista interior distinta, se necesita otra tupla que la contenga. Cambia solo la lista de la copia.',
    },
    "e20": {
        "change": 'Importa `copy` y reemplaza la copia superficial por `copy.deepcopy(carro1)`.',
        "prepend": 'import copy\n\n',
        "replace": [('carro1.copy()', 'copy.deepcopy(carro1)')],
        "expected": "Toyota\n200\nFalse\n",
        "prompt": '¿Qué objetos quedan separados y por qué el motor original conserva sus caballos?',
        "answer": 'Se copian el diccionario del carro y el del motor. Cada carro tiene ahora su propio motor: cambiar los caballos de uno no modifica el otro.',
    },
}

RAZONAMIENTOS = {
    "e01": '¿Se modificó la cadena que señala `texto`? Explica.',
    "e02": '¿Qué objeto cambió? Clasifica `int`, `str`, `list`, `tuple`, `dict` y `set` según su mutabilidad.',
    "e03": 'Describe las referencias de `a`, `b` y `c`. ¿Cuántas listas se crearon?',
    "e04": 'Describe qué señalan `a` y `b` al final. ¿Se modificó el entero `7`?',
    "e05": 'Describe las dos listas e indica qué nombres señalan el mismo objeto.',
    "e06": '¿Podemos exigir un número específico como respuesta a `id(x)` en cualquier ejecución? Explica.',
    "e07": '¿Qué diferencia hay con D04, donde se utiliza `y = y + [4]`?',
    "e08": 'Describe las referencias después de `y.clear()` y al final. ¿Qué línea modifica la lista y cuál reasigna `y`?',
    "e09": 'Describe las listas durante la llamada. ¿Qué cambiaría si la función usara `lst.append(99)`?',
    "e10": 'Identifica la mutación y la reasignación de `d`. Propón una línea para vaciar el diccionario recibido.',
    "e11": 'Describe las dos listas e indica qué nombres comparten una.',
    "e12": '¿Por qué vaciar la lista de `b` no vacía la de `a`?',
    "e13": '¿Qué referencia se reemplazó? ¿Sigue compartida alguna fila?',
    "e14": 'Describe ambos niveles. ¿Por qué E13 y E14 afectan de forma distinta a `original`?',
    "e15": '¿La lista de `a` y la fila creada por `a * 3` son el mismo objeto? Explica.',
    "e16": '¿Cuántas filas distintas hay? Escribe la construcción con una comprensión de listas.',
    "e17": '¿Qué objetos mutables necesitas copiar para que este cambio no afecte al original?',
    "e18": '¿Las filas de `copia` son independientes de la original? ¿Son independientes entre sí? Explica.',
    "e19": 'Describe los tres niveles. ¿Qué objeto cambia y cuáles siguen compartidos?',
    "e20": '¿Por qué la marca y el motor se comportan de forma distinta? Propón cómo conservar el motor de `carro1`.',
}

# Distractores cercanos a las confusiones que se trabajan en cada ejercicio.
DISTRACTORES = {
    "e01": ['hola', 'HOLA', 'None', '"hola"'],
    "e02": ['Ana', 'Luis', '"Ana"', '18', '19', '20'],
    "e03": ['[7]', '[7, 8]', '[8]', '[[7], 8]'],
    "e04": ['7', '8', '14', 'None'],
    "e05": [], "e06": [],
    "e07": ['[1, 2]', '[1, 2, 3]', '[3]', 'None'],
    "e08": ['[]', '[9]', '[1, 2]', '[1, 2, 9]'],
    "e09": ['[1, 2, 3]', '[1, 2, 3, 99]', '[99]', 'None'],
    "e10": ["{'key': 'value'}", '{}', 'None', "{'key': None}"],
    "e11": ['[10, 20]', '[99, 20]', '[10, 20, 30]', '[99, 20, 30]'],
    "e12": ["['A', 'B']", '[]', 'None', "['A']"],
    "e13": ['[[1, 2], [3, 4]]', '[[99, 2], [3, 4]]', '[[99], [3, 4]]', '[99, 2]'],
    "e14": ['[[1, 2], [3, 4]]', '[[99, 2], [3, 4]]', '[[1, 2], [3, 4], [5, 6]]', '[[5, 6]]'],
    "e15": ['[0]', '[1]', '[[1, 0, 0], [1, 0, 0], [1, 0, 0]]', '[[1, 0, 0], [0, 0, 0], [0, 0, 0]]', '[[0, 0, 0], [0, 0, 0], [0, 0, 0]]'],
    "e16": ['[[1, 0, 0], [1, 0, 0], [1, 0, 0]]', '[[1, 0, 0], [0, 0, 0], [0, 0, 0]]', '[[0, 0, 0], [0, 0, 0], [0, 0, 0]]', '[[1], [0], [0]]'],
    "e17": ['[8, 9]', '[8, 9, 10]', '[10]', 'None'],
    "e18": ['[[0], [0]]', '[[7], [7]]', '[[7], [0]]', '[[0], [7]]'],
    "e19": ["[([1], 'A')]", "[([1, 2], 'A')]", "[([2], 'A')]", 'None'],
    "e20": ['Toyota', 'Honda', '"Toyota"', '200', '300', 'None'],
}


def cases_for(exercise):
    ident = exercise['id']
    config = VARIACIONES[ident]
    code = exercise['code']
    for old, new in config.get('replace', []):
        if old not in code:
            raise ValueError(f'La variación de {ident} ya no coincide con el caso inicial: {old!r}')
        code = code.replace(old, new, 1)
    code = config.get('prepend', '') + code + config.get('append', '')
    return [
        {'key': 'inicial', 'label': 'Caso inicial', 'code': exercise['code'],
         'expected': exercise['expected'], 'prompt': RAZONAMIENTOS[ident],
         'answer': exercise['explanation'], 'change': ''},
        {'key': 'variacion', 'label': 'Variación', 'code': code,
         'expected': config['expected'],
         'prompt': config['prompt'], 'answer': config['answer'], 'change': config['change']},
    ]
