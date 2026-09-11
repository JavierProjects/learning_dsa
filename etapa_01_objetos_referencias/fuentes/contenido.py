"""Fuente editable de la guía y de los programas. Python 3.10 o posterior.

El generador utiliza el mismo código en el PDF y en los archivos .py.
Las salidas esperadas se escriben explícitamente y se verifican por ejecución.
"""

from textwrap import dedent


def programa(identificador, titulo, codigo, salida, explicacion, preguntas=None):
    return {
        "id": identificador,
        "title": titulo,
        "code": dedent(codigo).strip() + "\n",
        "expected": dedent(salida).strip() + "\n",
        "explanation": explicacion,
        "questions": preguntas or [],
    }


UNIDADES = [
    {
        "number": "1.1", "title": "Objetos, tipos y mutabilidad",
        "goal": "Reconocer qué objetos pueden cambiar y qué ocurre cuando una variable señala otro objeto.",
        "question": "Si los enteros no pueden cambiar, ¿por qué funciona `n = n + 1`?",
        "concepts": [
            "En Python trabajamos con objetos. Cada uno tiene un tipo, un valor y una identidad. En `x = 5`, el objeto es de tipo `int` y su valor es `5`. Su identidad permite reconocer ese objeto concreto, aunque otros tengan el mismo valor.",
            "Un objeto mutable puede cambiar su contenido; uno inmutable lo conserva. Una variable es un nombre que señala un objeto. Por eso `n = n + 1` funciona: `n` pasa a señalar el entero resultante. El entero anterior conserva su valor.",
        ],
        "table": {
            "headers": ["Mutables", "Inmutables"],
            "rows": [["`list`, `dict`, `set`", "`int`, `float`, `bool`, `str`, `tuple`"],
                     ["Consulta adicional: `bytearray`", "Consulta: `complex`, `bytes`, `range`, `frozenset`"]],
        },
        "example": programa("d01", "Una lista cambia; un entero se sustituye", '''
            numero = 10
            numero = numero + 1
            datos = [10]
            datos[0] = 11
            print(numero)
            print(datos)
        ''', '''
            11
            [11]
        ''', "La suma da `11` y `numero` pasa a señalar ese entero. El entero `10` conserva su valor. En la lista, `datos[0] = 11` reemplaza su primer elemento: cambia la misma lista, no el entero que estaba allí."),
        "diagram": "mutabilidad",
        "pitfall": "Que una variable muestre otro valor no demuestra que el objeto anterior haya cambiado. Por ejemplo, `upper()` obtiene una cadena en mayúsculas sin modificar la cadena original.",
        "exercises": [
            programa("e01", "Una operación sobre una cadena", '''
                texto = "hola"
                mayusculas = texto.upper()
                print(texto)
                print(mayusculas)
            ''', '''
                hola
                HOLA
            ''', "`texto.upper()` obtiene la cadena en mayúsculas. La cadena original conserva `hola`, y `texto` sigue señalándola. La variable `mayusculas` señala el resultado: `HOLA`.", ["Escribe las dos líneas de salida.", "¿Se modificó la cadena que señala `texto`? Explica."]),
            programa("e02", "Modificar un diccionario", '''
                alumno = {"nombre": "Ana", "edad": 18}
                alumno["edad"] = 19
                print(alumno["nombre"])
                print(alumno["edad"])
            ''', '''
                Ana
                19
            ''', "Cambia el diccionario de `alumno`, en la entrada `\"edad\"`. El entero `18` no se transforma en `19`. Los tipos `int`, `str` y `tuple` son inmutables; `list`, `dict` y `set` son mutables.", ["Escribe la salida e identifica qué objeto cambió.", "Clasifica `int`, `str`, `list`, `tuple`, `dict` y `set` según su mutabilidad."]),
        ],
        "variation": "En E01, reemplaza la segunda línea por `texto = texto.upper()` y muestra solo `texto`. ¿Las cadenas dejarían de ser inmutables?",
        "variation_answer": "Se imprimiría `HOLA`. Las cadenas siguen siendo inmutables: ahora `texto` señala la cadena resultante, y la original conserva su contenido.",
        "checkpoint": "Puedo explicar la diferencia entre cambiar un objeto y hacer que una variable señale otro.",
    },
    {
        "number": "1.2", "title": "Variables, asignación y referencias",
        "goal": "Dibujar las referencias y reconocer cuándo varios nombres señalan el mismo objeto.",
        "question": "Cuando escribes `y = x`, ¿creas otra lista o das otro nombre a la misma lista?",
        "concepts": [
            "Piensa en una variable como una etiqueta y en un objeto como una tarjeta. La referencia es la flecha que une ambos. Con `x = [1, 2, 3]` creamos una lista y la señalamos con `x`. Con `y = x`, también `y` señala esa lista.",
            "La asignación no hace una copia. Si dos nombres señalan el mismo objeto, los llamamos alias. Cuando modificas la lista usando uno, ves el cambio también desde el otro: ambos te llevan a la misma lista.",
        ],
        "example": programa("d02", "Dos nombres, una lista", '''
            x = [1, 2, 3]
            y = x
            y.append(4)
            print(x)
            print(y)
        ''', '''
            [1, 2, 3, 4]
            [1, 2, 3, 4]
        ''', "`x` y `y` señalan la misma lista. Al ejecutar `y.append(4)`, esa lista cambia. Las dos impresiones muestran el cambio porque consultan el mismo objeto."),
        "diagram": "alias",
        "pitfall": "Dos nombres no significan dos objetos. Cuenta las cajas de objetos y sigue las flechas. Los folios A y B de los dibujos son simbólicos; no son direcciones reales.",
        "exercises": [
            programa("e03", "Una tercera referencia", '''
                a = [7]
                b = a
                c = b
                c.append(8)
                print(a)
                print(b)
                print(c)
            ''', '''
                [7, 8]
                [7, 8]
                [7, 8]
            ''', "Se crea una sola lista. Los nombres `a`, `b` y `c` la señalan. La instrucción `c.append(8)` la modifica; las asignaciones anteriores no hicieron copias.", ["Predice la salida y dibuja los tres nombres.", "¿Cuántas listas se crearon?"]),
            programa("e04", "La misma asignación con enteros", '''
                a = 7
                b = a
                b = b + 1
                print(a)
                print(b)
            ''', '''
                7
                8
            ''', "Después de `b = a`, ambos nombres señalan el entero `7`. La suma hace que `b` pase a señalar el `8`. La variable `a` sigue señalando el `7`, que conserva su valor.", ["Escribe la salida y dibuja las referencias al final.", "¿Se modificó el entero `7`?"]),
        ],
        "variation": "En E03, cambia únicamente `b = a` por `b = [7]`. Conserva `c = b`. ¿Qué se imprimirá y cuántas listas habrá?",
        "variation_answer": "Se imprimen `[7]`, `[7, 8]` y `[7, 8]`. La variable `a` señala una lista; `b` y `c` comparten la segunda, creada con `[7]`.",
        "checkpoint": "Puedo contar los objetos sin confundirlos con los nombres que los señalan.",
    },
    {
        "number": "1.3", "title": "Identidad e igualdad",
        "goal": "Predecir si dos nombres señalan el mismo objeto, sin memorizar números de identificación.",
        "question": "¿Dos listas que imprimen lo mismo tienen que ser la misma lista?",
        "concepts": [
            "La identidad distingue a un objeto concreto. En la analogía, es el folio de la tarjeta; la flecha representa la referencia. Para nuestras listas, `==` compara el contenido e `is` comprueba si se trata del mismo objeto. Dos listas pueden ser iguales y tener identidades distintas.",
            "La función `id(objeto)` devuelve un número que identifica al objeto mientras existe. En CPython es su dirección de memoria; en otras implementaciones no tiene que serlo. Compararemos si los identificadores coinciden entre objetos que existen al mismo tiempo.",
        ],
        "example": programa("d03", "Iguales no significa compartidas", '''
            a = [1, 2]
            b = a
            c = [1, 2]
            print(a == c)
            print(a is c)
            print(a is b)
            print(id(a) == id(b))
        ''', '''
            True
            False
            True
            True
        ''', "`a` y `b` comparten una lista. La variable `c` señala otra con el mismo contenido. Por eso `a == c` da `True`, pero `a is c` da `False`. Los identificadores de `a` y `b` coinciden porque señalan el mismo objeto."),
        "diagram": "identidad",
        "pitfall": "Usa `==` para comparar valores. Con números y cadenas, Python puede reutilizar objetos: no saques reglas generales a partir de `is` entre literales. Cuando un objeto deja de existir, su identificador puede reutilizarse.",
        "exercises": [
            programa("e05", "Tres comparaciones", '''
                a = [5]
                b = [5]
                c = a
                print(a == b)
                print(a is b)
                print(b is c)
                print(id(a) == id(c))
            ''', '''
                True
                False
                False
                True
            ''', "`a` y `c` comparten una lista; `b` señala otra. Las dos listas contienen `5`, pero son objetos distintos. La última comparación da `True` porque `a` y `c` señalan el mismo objeto.", ["Predice cada `True` o `False`; no escribas direcciones.", "Dibuja las listas e indica qué nombres señalan el mismo objeto."]),
            programa("e06", "Objetos vacíos", '''
                x = []
                y = x
                z = []
                print(x == z)
                print(x is y)
                print(id(y) == id(z))
            ''', '''
                True
                True
                False
            ''', "Cada `[]` crea otra lista. Las listas de `x` y `z` están vacías y son iguales, pero son objetos distintos. La variable `y` comparte la de `x`. No se puede exigir un valor numérico fijo para `id(x)` entre ejecuciones.", ["Escribe las tres líneas de salida.", "¿Podemos exigir un número específico como respuesta a `id(x)` en cualquier ejecución?"]),
        ],
        "variation": "En E05, cambia únicamente `c = a` por `c = b`. ¿Cuáles de las cuatro respuestas cambian?",
        "variation_answer": "Ahora se imprime `True`, `False`, `True` y `False`: cambian la tercera y la cuarta respuesta. En E06 no podemos exigir un número fijo para `id(x)`; buscamos saber si dos identificadores coinciden.",
        "checkpoint": "Puedo explicar cuándo dos listas son iguales y cuándo son la misma lista.",
    },
    {
        "number": "1.4", "title": "Mutación y reasignación",
        "goal": "Distinguir si una instrucción modifica un objeto o cambia el objeto que señala una variable.",
        "question": "Si `x` y `y` comparten una lista, ¿por qué `y.append(4)` y `y = y + [4]` afectan de forma distinta lo que vemos mediante `x`?",
        "concepts": [
            "Mutar es cambiar un objeto existente. Por ejemplo, `x.append(3)` agrega un elemento a la misma lista. Asignar es indicar qué objeto señala un nombre: con `x = x` seguimos en el mismo; con `x = x + [3]` señalamos una lista nueva.",
            "Con listas, `+` crea otra lista y `+=` amplía la existente. Con enteros, `+=` hace que el nombre señale el resultado de la suma. Antes de decidir qué cambia, mira el tipo de objeto y la operación.",
        ],
        "example": programa("d04", "La concatenación crea otra lista", '''
            x = [1, 2, 3]
            y = x
            y = y + [4]
            print(x)
            print(y)
            print(x is y)
        ''', '''
            [1, 2, 3]
            [1, 2, 3, 4]
            False
        ''', "Primero, `y + [4]` crea otra lista. Después, `y` pasa a señalarla. La variable `x` sigue señalando la lista inicial. Si hubiéramos usado `y.append(4)`, habría cambiado la lista compartida y lo veríamos también mediante `x`."),
        "diagram": "reasignacion",
        "pitfall": "`x.clear()` vacía la misma lista; `x = []` hace que `x` señale otra. Los métodos `append()` y `clear()` devuelven `None`: si escribes `x = x.append(4)`, al final `x` señalará `None`.",
        "exercises": [
            programa("e07", "La suma aumentada sobre una lista", '''
                x = [1, 2]
                y = x
                y += [3]
                print(x)
                print(y)
                print(x is y)
            ''', '''
                [1, 2, 3]
                [1, 2, 3]
                True
            ''', "Con listas, `+=` agrega elementos a la misma lista. Por eso `x` y `y` siguen compartiéndola. En D04, la operación `+` creó otra lista y después `y` pasó a señalarla.", ["Predice las tres salidas.", "¿Qué diferencia hay con el ejemplo D04?"]),
            programa("e08", "Vaciar y después reasignar", '''
                x = [1, 2]
                y = x
                y.clear()
                y = [9]
                print(x)
                print(y)
                print(x is y)
            ''', '''
                []
                [9]
                False
            ''', "Primero, `y.clear()` vacía la lista compartida. Después, `y = [9]` crea otra lista y hace que `y` la señale. La variable `x` sigue señalando la lista vacía.", ["Dibuja las referencias después de `y.clear()` y al final.", "¿Qué línea modifica la lista y cuál hace que `y` señale otra?"]),
        ],
        "variation": "En E07, cambia `y += [3]` por `y = y + [3]`. Después analiza `a = 10; b = a; b += 3`. ¿Qué cambia en cada caso?",
        "variation_answer": "Con listas se imprime `[1, 2]`, `[1, 2, 3]` y `False`: la suma crea otra lista. Con enteros, `a` sigue señalando el `10` y `b` pasa a señalar el `13`. El entero `10` conserva su valor.",
        "checkpoint": "Puedo decir qué objeto señala cada nombre antes y después de una instrucción.",
        "lab": "p01",
    },
]


UNIDADES.extend([
    {
        "number": "1.5", "title": "Referencias en funciones",
        "goal": "Explicar cuándo una función modifica un objeto compartido y cuándo entrega un resultado con `return`.",
        "question": "¿Por qué una función puede agregar elementos a tu lista, pero escribir `lst = []` dentro de ella no la vacía?",
        "concepts": [
            "Al llamar a una función, sus parámetros se convierten en nombres locales para los objetos recibidos. Es como añadir una etiqueta a cada tarjeta. Python pasa argumentos por asignación: esta regla funciona igual con listas, diccionarios, enteros y cadenas.",
            "Si la función modifica un objeto compartido, puedes ver el cambio fuera de ella. Si reasigna su parámetro, solo cambia lo que señala ese nombre local. Para entregar un resultado al código que la llamó, usa `return` y guarda ese resultado cuando lo necesites.",
        ],
        "example": programa("d05", "Dos funciones sobre el mismo argumento", '''
            def add_item(lst):
                lst.append("X")

            def reset_list(lst):
                lst = []

            my_list = []
            add_item(my_list)
            reset_list(my_list)
            print(my_list)
        ''', '''
            ['X']
        ''', "`add_item()` agrega `\"X\"` a la lista compartida por `my_list` y `lst`. En `reset_list()`, la instrucción `lst = []` hace que solo el parámetro local señale otra lista. La variable `my_list` sigue señalando la primera."),
        "diagram": "funciones",
        "pitfall": "Las listas y los enteros siguen la misma regla al entrar a una función. La diferencia está en qué operaciones permiten. Si una función termina sin ejecutar `return` con un valor, devuelve `None`.",
        "exercises": [
            programa("e09", "Reasignar dentro de la función", '''
                def modify(lst):
                    lst = lst + [99]

                numbers = [1, 2, 3]
                modify(numbers)
                print(numbers)
            ''', '''
                [1, 2, 3]
            ''', "`lst + [99]` crea otra lista, y solo el parámetro `lst` pasa a señalarla. La variable `numbers` conserva la lista inicial. Con `lst.append(99)` sí cambiaría esa lista compartida.", ["Escribe la salida y dibuja las dos listas durante la llamada.", "¿Qué cambiaría si la función usara `lst.append(99)`?"]),
            programa("e10", "Actualizar y reiniciar un diccionario", '''
                def update_dict(d):
                    d["key"] = "value"

                def reset_dict(d):
                    d = {}

                my_dict = {}
                update_dict(my_dict)
                reset_dict(my_dict)
                print(my_dict)
            ''', '''
                {'key': 'value'}
            ''', "`update_dict()` modifica el diccionario de `my_dict`. La función `reset_dict()` solo hace que su parámetro `d` señale otro diccionario. Para vaciar el recibido, podría ejecutar `d.clear()`.", ["Identifica la línea que modifica el diccionario y la que reasigna `d`.", "Propón una línea para que `reset_dict()` vacíe el diccionario recibido."]),
        ],
        "variation": "En E09, haz que la función devuelva `lst + [99]`. Compara `modify(numbers)` con `numbers = modify(numbers)`: ¿en cuál guardas la lista resultante?",
        "variation_answer": "Sin guardar el resultado, `numbers` conserva `[1, 2, 3]`. Al asignarlo, señala `[1, 2, 3, 99]`. Si usas `lst.append(99)`, cambia la lista original. En E10, `d.clear()` vacía el diccionario recibido.",
        "checkpoint": "Puedo explicar qué cambia fuera de una función y cuándo necesito guardar lo que devuelve.",
        "lab": "p02",
    },
    {
        "number": "1.6", "title": "Copias de listas simples",
        "goal": "Elegir entre compartir una lista o copiarla para modificarla por separado.",
        "question": "¿Qué cambia si escribes `copia = original.copy()` en lugar de `copia = original`?",
        "concepts": [
            "Con `original.copy()` creas otra lista. Sus posiciones empiezan señalando los mismos elementos que la original. A esto lo llamamos copia superficial: copias la lista exterior, pero no haces nuevas copias de cada objeto que contiene.",
            "También puedes copiar una lista con `original[:]`. Si contiene enteros, cadenas o booleanos, cambiar una posición de la copia no modifica la lista original. Lo que cambia es qué objeto ocupa esa posición de la lista nueva.",
        ],
        "example": programa("d06", "Una copia con elementos inmutables", '''
            original = [1, 2, "hola", True]
            copia = original.copy()
            copia[0] = 99
            print(original)
            print(copia)
            print(original is copia)
        ''', '''
            [1, 2, 'hola', True]
            [99, 2, 'hola', True]
            False
        ''', "Hay dos listas. Reemplazar la primera posición de `copia` no cambia la de `original`. Los demás elementos pueden seguir siendo los mismos objetos inmutables, aunque las listas que los contienen sean distintas."),
        "diagram": "copia_simple",
        "pitfall": "Llamar `copia` a una variable no crea una copia: `copia = original` comparte la lista. Más adelante veremos por qué una tupla que contiene una lista requiere mirar un nivel adicional.",
        "exercises": [
            programa("e11", "Una copia y un alias", '''
                original = [10, 20]
                copia = original.copy()
                alias = original
                copia.append(30)
                alias[0] = 99
                print(original)
                print(copia)
            ''', '''
                [99, 20]
                [10, 20, 30]
            ''', "`copia` señala otra lista, a la que se agrega `30`. La variable `alias` comparte la lista de `original` y reemplaza su primer elemento por `99`. Son dos cambios sobre dos listas distintas.", ["Predice la salida y dibuja las dos listas.", "¿Qué nombres señalan la misma lista?"]),
            programa("e12", "Copiar mediante un corte", '''
                a = ["A", "B"]
                b = a[:]
                print(a == b)
                print(a is b)
                b.clear()
                print(a)
                print(b)
            ''', '''
                True
                False
                ['A', 'B']
                []
            ''', "`a[:]` crea otra lista con los mismos elementos. Al principio son iguales, pero `a is b` da `False`. Después, `b.clear()` vacía solamente la lista de `b`.", ["Escribe cada línea de salida.", "¿Por qué vaciar la lista de `b` no vacía la de `a`?"]),
        ],
        "variation": "En E12, cambia `b = a[:]` por `b = a`. Vuelve a predecir las cuatro salidas.",
        "variation_answer": "Se imprime `True`, `True`, `[]` y `[]`. Ahora `a` y `b` comparten una lista y `b.clear()` la vacía. En E11, quienes comparten la misma lista son `original` y `alias`.",
        "checkpoint": "Puedo decidir cuándo compartir una lista y cuándo necesito una copia.",
    },
    {
        "number": "1.7", "title": "Anidamiento y copia superficial",
        "goal": "Seguir las referencias de una lista anidada y distinguir entre reemplazar una fila y modificarla.",
        "question": "Si copias una lista, ¿pueden seguir compartidas las listas que hay dentro?",
        "concepts": [
            "Una lista puede señalar otras listas. En `original[0][0]`, el primer índice nos lleva a la primera lista interior y el segundo a su primer elemento. Dibuja la lista exterior y cada lista interior en cajas separadas.",
            "Una copia superficial crea otra lista exterior, pero conserva las referencias a las interiores. Así, `copia[0] = [99]` reemplaza una fila de la copia; `copia[0][0] = 99` cambia una fila que puede seguir compartida con `original`.",
        ],
        "example": programa("d07", "Dos exteriores y una lista interior", '''
            a = [1, 2]
            b = [a, a]
            c = b.copy()
            c[0][0] = 99
            print(a)
            print(b)
            print(c)
            print(b is c)
        ''', '''
            [99, 2]
            [[99, 2], [99, 2]]
            [[99, 2], [99, 2]]
            False
        ''', "`b` y `c` son dos listas exteriores distintas. Las cuatro posiciones entre ambas señalan la misma lista de `a`. La instrucción `c[0][0] = 99` cambia esa lista interior y el cambio se ve al imprimir cualquiera de las dos listas exteriores."),
        "diagram": "anidamiento",
        "pitfall": "Cuando leas «se hizo una copia», pregunta: ¿de qué objeto? Después identifica cuáles siguen compartidos.",
        "exercises": [
            programa("e13", "Sustituir una fila de la copia", '''
                original = [[1, 2], [3, 4]]
                copia = original.copy()
                copia[0] = [99, 2]
                print(original)
                print(copia)
                print(original[1] is copia[1])
            ''', '''
                [[1, 2], [3, 4]]
                [[99, 2], [3, 4]]
                True
            ''', "`copia[0] = [99, 2]` reemplaza la primera fila de la copia. La primera fila de `original` conserva su contenido. La segunda fila sigue compartida entre ambas listas exteriores.", ["Escribe la salida y señala qué referencia se reemplazó.", "¿Sigue compartida alguna fila?"]),
            programa("e14", "Modificar una fila compartida", '''
                original = [[1, 2], [3, 4]]
                copia = original.copy()
                copia[0][0] = 99
                print(original)
                print(copia)
                print(original[0] is copia[0])
            ''', '''
                [[99, 2], [3, 4]]
                [[99, 2], [3, 4]]
                True
            ''', "La primera fila sigue siendo una sola lista compartida. Al cambiar su primer elemento, ves el resultado desde `original` y desde `copia`. En E13 se reemplazó la referencia a la fila; aquí se modifica la fila misma.", ["Predice las salidas y dibuja ambos niveles.", "¿Por qué E13 y E14 afectan de forma distinta a `original`?"]),
        ],
        "variation": "En E14, cambia únicamente `copia[0][0] = 99` por `copia.append([5, 6])`. ¿Qué lista se modifica?",
        "variation_answer": "Solo cambia la lista exterior `copia`. La lista `original` conserva `[[1, 2], [3, 4]]`; la copia queda `[[1, 2], [3, 4], [5, 6]]`. La primera fila sigue compartida: la comparación da `True`.",
        "checkpoint": "Puedo seguir los índices hasta la lista que cambia y reconocer qué partes siguen compartidas.",
    },
])


UNIDADES.extend([
    {
        "number": "1.8", "title": "Repetición de listas y matrices",
        "goal": "Reconocer qué referencias se repiten con `*` y construir matrices cuyas filas puedan cambiar por separado.",
        "question": "¿Por qué modificar una sola celda puede cambiar lo que vemos en las tres filas?",
        "concepts": [
            "Al repetir una lista con `*`, se repiten las referencias a sus elementos. En `[0] * 3` obtienes tres posiciones que señalan el entero `0`. Puedes reemplazar una posición de esa lista sin modificar el entero.",
            "En `[[0] * 3] * 3` hay una sola fila `[0, 0, 0]`: la lista exterior la señala tres veces. Para tener filas independientes, crea una nueva en cada vuelta del ciclo. La expresión `[[0] * 3 for _ in range(3)]` hace justamente eso.",
        ],
        "example": programa("d08", "Una fila compartida tres veces", '''
            matrix = [[0] * 3] * 3
            matrix[0][0] = 1
            print(matrix)
            print(matrix[0] is matrix[1])
        ''', '''
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
            True
        ''', "Hay una lista exterior y una sola fila interior. La instrucción `matrix[0][0] = 1` cambia esa fila. Como las tres posiciones de la lista exterior señalan la misma fila, el cambio aparece tres veces al imprimir."),
        "diagram": "matrices",
        "pitfall": "La comprensión evalúa `[0] * 3` en cada vuelta. Usamos `_` porque no necesitamos el contador. Con `a = [0]` y `[a * 3] * 3`, también se crea una sola fila nueva y se comparte tres veces.",
        "exercises": [
            programa("e15", "Una variable explícita", '''
                a = [0]
                matrix = [a * 3] * 3
                matrix[0][0] = 1
                print(a)
                print(matrix)
                print(matrix[0] is matrix[2])
            ''', '''
                [0]
                [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
                True
            ''', "`a * 3` crea una fila distinta de la lista de `a`. La lista exterior la señala tres veces. Cambia esa fila, mientras `a` conserva `[0]`. Al final, desde `a` y `matrix` puedes llegar a tres listas: la de `a`, la fila y la exterior.", ["Predice las tres salidas.", "¿La lista de `a` y la fila creada por `a * 3` son el mismo objeto? Explica."]),
            programa("e16", "Construcción con un ciclo", '''
                matrix = []
                for _ in range(3):
                    matrix.append([0] * 3)
                matrix[0][0] = 1
                print(matrix)
                print(matrix[0] is matrix[1])
            ''', '''
                [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
                False
            ''', "Cada vuelta del ciclo crea otra fila. Al cambiar una celda de la primera, las otras dos conservan su contenido. Puedes escribir la construcción como `matrix = [[0] * 3 for _ in range(3)]`.", ["Predice la salida y dibuja las tres filas.", "Escribe la construcción con una comprensión de listas."]),
        ],
        "variation": "En E15, usa `matrix = [(a * 3).copy() for _ in range(3)]`. ¿Hace falta `.copy()` aquí? Con `a = [0]`, ¿qué tamaño tendría `[a.copy(), a.copy(), a.copy()]`?",
        "variation_answer": "Las filas son independientes. Aquí sobra `.copy()`, porque `a * 3` ya crea otra fila en cada vuelta. En E16 puedes usar `[[0] * 3 for _ in range(3)]`. Si copias tres veces `a = [0]`, obtienes 3 filas y 1 columna.",
        "checkpoint": "Puedo explicar por qué repetir una fila no equivale a crear varias filas independientes.",
        "lab": "p03",
    },
    {
        "number": "1.9", "title": "Copia profunda",
        "goal": "Decidir qué necesitas copiar para modificar los objetos interiores sin afectar los originales.",
        "question": "Si necesito modificar listas interiores sin afectar al original, ¿qué debo copiar?",
        "concepts": [
            "El módulo `copy` viene incluido en Python. Con `copy.copy(objeto)` haces una copia superficial. Con `copy.deepcopy(objeto)` también copias los contenedores interiores de nuestros ejemplos: las listas y los diccionarios anidados.",
            "Elige según lo que necesites cambiar. Una asignación permite compartir el objeto. Una copia superficial separa el contenedor exterior. Una copia profunda permite cambiar los contenedores interiores de estos ejemplos sin modificar los originales.",
        ],
        "example": programa("d09", "Separar también las filas", '''
            import copy

            original = [[1, 2], [3, 4]]
            profunda = copy.deepcopy(original)
            profunda[0][0] = 99
            print(original)
            print(profunda)
            print(original[0] is profunda[0])
        ''', '''
            [[1, 2], [3, 4]]
            [[99, 2], [3, 4]]
            False
        ''', "Se copian la lista exterior y las filas. Ahora `profunda[0]` y `original[0]` son listas distintas: cambiar una no modifica la otra. Para lograrlo no hace falta copiar también cada entero."),
        "diagram": "profunda",
        "pitfall": "`deepcopy()` puede mantener referencias compartidas dentro de la copia. Si dos posiciones señalaban una sola fila, pueden seguir señalando una sola fila copiada. Para separar esas filas, revisa cómo las construyes.",
        "exercises": [
            programa("e17", "Una lista dentro de un diccionario", '''
                import copy

                original = {"notas": [8, 9]}
                copia = copy.deepcopy(original)
                copia["notas"].append(10)
                print(original["notas"])
                print(copia["notas"])
            ''', '''
                [8, 9]
                [8, 9, 10]
            ''', "Se copian el diccionario y su lista `\"notas\"`. La instrucción `append(10)` cambia solo la lista copiada. Una copia superficial del diccionario dejaría esa lista compartida.", ["Predice las dos líneas de salida.", "¿Qué objetos mutables necesitas copiar para que este cambio no afecte al original?"]),
            programa("e18", "Una copia profunda conserva un alias interno", '''
                import copy

                fila = [0]
                original = [fila, fila]
                copia = copy.deepcopy(original)
                copia[0][0] = 7
                print(original)
                print(copia)
                print(copia[0] is copia[1])
                print(copia[0] is fila)
            ''', '''
                [[0], [0]]
                [[7], [7]]
                True
                False
            ''', "`deepcopy()` copia la fila una vez y usa esa misma copia en las dos posiciones. La fila original conserva `[0]`. Hay independencia respecto al original, pero las dos posiciones de `copia` siguen compartiendo una fila.", ["Predice la salida y dibuja las listas originales y las copiadas.", "¿Las filas de `copia` son independientes de la original? ¿Son independientes entre sí?"]),
        ],
        "variation": "En E17, usa `original.copy()`. En E18, usa `copia = [elemento.copy() for elemento in original]`. ¿Qué cambia en cada caso?",
        "variation_answer": "En E17 se imprime `[8, 9, 10]` dos veces: la lista interior sigue compartida. En E18 se imprime `[[0], [0]]`, `[[7], [0]]`, `False` y `False`. Cada vuelta copia la fila por separado; sus elementos son enteros.",
        "checkpoint": "Puedo elegir qué copiar y explicar si la copia comparte objetos con el original o entre sus propias posiciones.",
    },
    {
        "number": "1.10", "title": "Integración y matices de mutabilidad",
        "goal": "Resolver ejemplos que combinan funciones y contenedores, sin perder de vista qué objeto cambia.",
        "question": "¿Puede cambiar una lista contenida en una tupla aunque la tupla sea inmutable?",
        "concepts": [
            "Una tupla conserva los objetos a los que apuntan sus posiciones: no puedes reemplazarlos. Pero, si uno de ellos es una lista, esa lista sí puede cambiar. Por eso puedes observar contenido diferente al imprimir la tupla sin haber reemplazado ninguno de sus elementos.",
            "Sigue la ruta hasta el objeto que cambia. En `carro[\"motor\"][\"caballos\"] = 300` modificas el diccionario del motor. Copiar solo el diccionario del carro no separa ese motor. Aquí representamos carros, personas y equipos mediante diccionarios.",
        ],
        "example": programa("d10", "Una tupla y su lista interior", '''
            datos = ([1, 2], "grupo A")
            alias = datos
            datos[0].append(3)
            print(datos)
            print(alias is datos)
        ''', '''
            ([1, 2, 3], 'grupo A')
            True
        ''', "La tupla sigue señalando la misma lista y la misma cadena. Solo cambia la lista interior. Si intentaras `datos[0] = [9]`, tratarías de reemplazar un elemento de la tupla y obtendrías `TypeError`."),
        "diagram": "tupla",
        "pitfall": "Que haya una tupla no vuelve inmutables los objetos que contiene. Que haya una copia tampoco garantiza que todos los objetos interiores sean independientes.",
        "exercises": [
            programa("e19", "Copiar una lista que contiene una tupla", '''
                original = [([1], "A")]
                copia = original.copy()
                copia[0][0].append(2)
                print(original)
                print(copia)
                print(original[0] is copia[0])
            ''', '''
                [([1, 2], 'A')]
                [([1, 2], 'A')]
                True
            ''', "Se copia la lista exterior, pero su elemento sigue siendo la misma tupla. Esa tupla señala la misma lista interior, a la que se agrega `2`. Continúan compartidas la tupla y la lista que contiene.", ["Predice las salidas y dibuja los tres niveles.", "¿Qué objeto cambia y cuáles siguen compartidos?"]),
            programa("e20", "Dos carros comparten motor", '''
                motor = {"caballos": 200}
                carro1 = {"marca": "Toyota", "motor": motor}
                carro2 = carro1.copy()
                carro2["marca"] = "Honda"
                carro2["motor"]["caballos"] = 300
                print(carro1["marca"])
                print(carro1["motor"]["caballos"])
                print(carro1["motor"] is carro2["motor"])
            ''', '''
                Toyota
                300
                True
            ''', "Los carros son diccionarios distintos: cambiar `carro2[\"marca\"]` no afecta a `carro1`. Sin embargo, comparten el diccionario `motor`, que ahora contiene `300` caballos. Para conservar el motor original, puedes usar `copy.deepcopy(carro1)`.", ["Predice las salidas. ¿Por qué la marca y el motor se comportan de forma distinta?", "¿Cómo harías que el motor de `carro1` conserve su valor?"]),
        ],
        "variation": "En E20, importa `copy` y usa `copy.deepcopy(carro1)`. En D10, compara `datos[0].append(3)` con `datos[0] = [3]`: ¿qué objeto intenta modificar cada operación?",
        "variation_answer": "E20 imprime `Toyota`, `200` y `False`: la copia tiene su propio diccionario del motor. En D10, `append(3)` cambia la lista interior; `datos[0] = [3]` intenta reemplazar un elemento de la tupla y produce `TypeError`.",
        "checkpoint": "Puedo localizar y corregir un cambio compartido inesperado explicando cada paso.",
        "lab": "p04",
    },
])


PRACTICAS = [
    {
        "id": "p01", "section": "1.4", "title": "Identidad y cambios de estado",
        "goal": "Comprobar qué ocurre al ampliar una lista compartida, crear otra lista y sumar a un entero.",
        "initial": programa("p01", "Programa inicial", '''
            x = [1, 2]
            y = x
            y += [3]
            a = 10
            b = a
            b += 3
            print(x)
            print(x is y)
            print(a, b)
        ''', '''
            [1, 2, 3]
            True
            10 13
        ''', "La lista compartida crece. El entero conserva su valor: `b` pasa a señalar el resultado de la suma."),
        "tasks": [
            "Predice la salida y dibuja las referencias del programa inicial.",
            "Ejecuta el archivo. Conserva tu predicción y explica las diferencias que encuentres.",
            "Variante A: cambia solo `y += [3]` por `y = y + [3]`. Predice y vuelve a ejecutar desde el inicio.",
            "Variante B: haz que las listas de `x` y `y` terminen vacías y sigan siendo el mismo objeto. Elige entre `y.clear()` y `y = []`, y comprueba tu decisión.",
        ],
        "solution": programa("s01", "Solución de la variante B", '''
            x = [1, 2]
            y = x
            y.clear()
            a = 10
            b = a
            b += 3
            print(x)
            print(x is y)
            print(a, b)
        ''', '''
            []
            True
            10 13
        ''', "`clear()` vacía la lista que comparten `x` y `y`. Con `y = []`, la lista de `x` conservaría su contenido y los nombres señalarían listas distintas."),
        "answers": [
            "Inicial: se imprime `[1, 2, 3]`, `True` y `10 13`. La lista cambia; el entero `10` conserva su valor.",
            "Variante A: se imprime `[1, 2]`, `False` y `10 13`. La operación `+` crea otra lista y `y` pasa a señalarla.",
            "Variante B: `y.clear()` cumple ambas condiciones. Puedes imprimir `y` y comprobar `id(x) == id(y)`: debe dar `True`.",
        ],
    },
    {
        "id": "p02", "section": "1.5", "title": "Modificar, reasignar y devolver",
        "goal": "Decidir si una función debe modificar la lista recibida o devolver otra lista.",
        "initial": programa("p02", "Programa inicial", '''
            def agregar_final(datos):
                datos = datos + [99]

            original = [1, 2]
            resultado = agregar_final(original)
            print(original)
            print(resultado)
        ''', '''
            [1, 2]
            None
        ''', "La función hace que `datos` señale otra lista y termina sin devolverla. La lista de `original` conserva su contenido, y `resultado` recibe `None`."),
        "tasks": [
            "Predice lo que se imprime mediante `original` y `resultado`. Dibuja qué señalan `original` y `datos` dentro de la función.",
            "Variante A: reemplaza el cuerpo por `datos.append(99)`, sin añadir `return`. Vuelve a predecir las salidas.",
            "Variante B: conserva la lista de `original` y devuelve otra con `99` al final. Guárdala en `resultado` y compara ambas identidades.",
            "En la variante B, llama a `agregar_final(original)` sin guardar el resultado. ¿Qué lista puedes seguir consultando mediante `original`?",
        ],
        "solution": programa("s02", "Solución de la variante B", '''
            def agregar_final(datos):
                return datos + [99]

            original = [1, 2]
            resultado = agregar_final(original)
            print(original)
            print(resultado)
            print(original is resultado)
        ''', '''
            [1, 2]
            [1, 2, 99]
            False
        ''', "`return` entrega la lista nueva al código que llamó a la función. La variable `resultado` la señala, mientras `original` conserva la primera lista."),
        "answers": [
            "Inicial: se imprime `[1, 2]` y `None`. Dentro de la función, `datos` termina señalando otra lista, `[1, 2, 99]`, mientras `original` conserva la primera.",
            "Variante A: la lista de `original` cambia a `[1, 2, 99]`. La variable `resultado` sigue recibiendo `None`: la función termina sin devolver un valor.",
            "Variante B: la función devuelve otra lista. Si no guardas ese resultado, `original` sigue señalando `[1, 2]` y no conservas un nombre para la lista nueva.",
        ],
    },
    {
        "id": "p03", "section": "1.8", "title": "Construir filas independientes",
        "goal": "Separar dos decisiones: crear filas independientes y copiar esas filas para otra matriz.",
        "initial": programa("p03", "Programa inicial", '''
            matrix = [[0] * 3] * 3
            copia = matrix.copy()
            copia[0][0] = 1
            print(matrix)
            print(copia)
            print(matrix is copia)
            print(matrix[0] is copia[0])
        ''', '''
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
            False
            True
        ''', "`copy()` crea otra lista exterior, pero ambas siguen señalando una sola fila compartida."),
        "tasks": [
            "Dibuja las listas exteriores y sus filas. Predice las cuatro salidas y después ejecuta.",
            "Variante A: construye `matrix` con un ciclo que cree una fila en cada vuelta. Conserva `copia = matrix.copy()`. ¿Qué filas siguen compartidas?",
            "Variante B: además de crear filas independientes, copia cada fila para que cambiar una celda de `copia` no cambie `matrix`. Usa lo aprendido hasta 1.8.",
            "Comprueba con `is` si las filas son distintas entre sí y si cada original es distinta de su copia. Compara identidades; no escribas números fijos de `id()`.",
        ],
        "solution": programa("s03", "Solución de la variante B", '''
            matrix = [[0] * 3 for _ in range(3)]
            copia = [fila.copy() for fila in matrix]
            copia[0][0] = 1
            print(matrix)
            print(copia)
            print(copia[0] is copia[1])
            print(matrix[0] is copia[0])
        ''', '''
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
            False
            False
        ''', "Cada fila se crea por separado y después se copia por separado. Como las celdas contienen enteros, basta con copiar estos dos niveles para cambiarlas sin afectar la matriz original."),
        "answers": [
            "Inicial: ambas matrices muestran tres veces `[1, 0, 0]`. Las listas exteriores son distintas, pero todas sus posiciones señalan la misma fila.",
            "Variante A: `matrix` y `copia` muestran `[[1, 0, 0], [0, 0, 0], [0, 0, 0]]`. Las filas de `matrix` son distintas entre sí, pero cada una sigue compartida con su posición en `copia`.",
            "Variante B: se separan las listas exteriores y cada fila. Para estas celdas enteras, una copia de cada fila es suficiente. Si hubiera otros objetos mutables dentro, revisaríamos ese nivel también.",
        ],
    },
    {
        "id": "p04", "section": "1.10", "title": "Un equipo de trabajo independiente",
        "goal": "Usar funciones y copia profunda para modificar un equipo sin alterar los datos del original.",
        "initial": programa("p04", "Programa inicial", '''
            def preparar_equipo(equipo):
                nuevo = equipo.copy()
                nuevo["nombre"] = "Pruebas"
                nuevo["miembros"][0]["edad"] = 99
                return nuevo

            ana = {"nombre": "Ana", "edad": 25}
            original = {"nombre": "Desarrollo", "miembros": [ana]}
            copia = preparar_equipo(original)
            print(original["nombre"], ana["edad"])
            print(copia["nombre"], copia["miembros"][0]["edad"])
        ''', '''
            Desarrollo 99
            Pruebas 99
        ''', "Se crea otro diccionario exterior, pero se comparten la lista `\"miembros\"` y el diccionario de Ana. Por eso la edad también cambia al consultarla mediante `ana`."),
        "tasks": [
            "Antes de ejecutar, dibuja el equipo, la lista `\"miembros\"` y el diccionario de Ana. Predice las dos salidas.",
            "Corrige `preparar_equipo()` para que el equipo devuelto cambie de nombre y edad sin modificar los objetos de `original` y `ana`.",
            "Compara con `is` tres niveles: equipo, lista de miembros y primer diccionario de persona. Explica cada resultado.",
            "Después, cambia la edad de Ana en el original. Comprueba que la copia conserva su edad y explica qué demuestra.",
        ],
        "solution": programa("s04", "Una solución con copia profunda", '''
            import copy

            def preparar_equipo(equipo):
                nuevo = copy.deepcopy(equipo)
                nuevo["nombre"] = "Pruebas"
                nuevo["miembros"][0]["edad"] = 99
                return nuevo

            ana = {"nombre": "Ana", "edad": 25}
            original = {"nombre": "Desarrollo", "miembros": [ana]}
            copia = preparar_equipo(original)
            print(original["nombre"], ana["edad"])
            print(copia["nombre"], copia["miembros"][0]["edad"])
            print(original is copia)
            print(original["miembros"] is copia["miembros"])
            print(ana is copia["miembros"][0])
        ''', '''
            Desarrollo 25
            Pruebas 99
            False
            False
            False
        ''', "`deepcopy()` separa los tres niveles mutables. La función devuelve el nuevo diccionario y la variable `copia` lo conserva."),
        "answers": [
            "Inicial: se imprime `Desarrollo 99` y `Pruebas 99`. Solo se copió el diccionario exterior. El nombre del equipo cambia por separado, pero la edad pertenece a un diccionario compartido.",
            "Con la solución se imprime `Desarrollo 25` y `Pruebas 99`. Las tres comparaciones dan `False`: se copiaron el equipo, la lista de miembros y el diccionario de la persona.",
            "Si después escribes `ana[\"edad\"] = 26`, el equipo original muestra `26` y la copia conserva `99`. Los dos equipos tienen diccionarios de persona independientes.",
        ],
    },
]


ANALOGIA = {
    "title": "Tarjetas, etiquetas y flechas",
    "intro": "Imagina tarjetas con números impresos. Una tiene el 5 y otra el 6. Como representan enteros, no podemos borrar el número para escribir otro. Cada tarjeta tiene además un folio que permite reconocerla.",
    "labels": "La variable `x` es una etiqueta: señala una tarjeta. Si lo dibujamos, la flecha es la referencia y el folio representa la identidad. A y B son folios inventados para el dibujo; no son resultados de `id()`.",
    "table": {
        "headers": ["Concepto", "En `x = 5`"],
        "rows": [["Nombre", "La etiqueta `x`."], ["Referencia", "La flecha desde `x` hasta la tarjeta."], ["Tipo", "`int`: la tarjeta representa un entero."], ["Valor", "El número `5` impreso en la tarjeta."], ["Identidad", "La tarjeta concreta, que distinguimos con su folio A."]],
    },
    "same": "Con `x = x`, miramos qué tarjeta señala `x` y volvemos a colocar la etiqueta en esa tarjeta. Hay una asignación, pero la etiqueta termina donde ya estaba.",
    "other": "Con `x = x + 1`, leemos el 5, sumamos 1 y colocamos `x` en la tarjeta del 6. No cambiamos el número de la primera tarjeta: ahora señalamos otra.",
    "code": "x = 5\nidentificador_inicial = id(x)\nx = x\nprint(id(x) == identificador_inicial)\nx = x + 1\nprint(id(x) == identificador_inicial)\n",
    "expected": "True\nFalse\n",
    "conclusion": "La identidad pertenece al objeto. Una asignación puede dejar una variable señalando el mismo objeto o hacer que señale otro. En este ejemplo, cuando cambia `id(x)`, cambia el objeto que señala `x`; ninguna tarjeta cambia de identidad.",
}


FUENTES = [
    ("Python: objetos, valores y tipos", "https://docs.python.org/3/reference/datamodel.html#objects-values-and-types", "Consulta para 1.1-1.3 y 1.10: mutabilidad, identidad y contenedores."),
    ("Python: asignación de argumentos", "https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference", "Consulta para 1.5: asociación de parámetros y uso de valores devueltos."),
    ("Python: copia superficial y profunda", "https://docs.python.org/3/library/copy.html", "Consulta para 1.6, 1.7 y 1.9: operaciones del módulo copy."),
    ("Python: operaciones de secuencias", "https://docs.python.org/3/library/stdtypes.html#common-sequence-operations", "Consulta para 1.8: repetición de referencias y construcción de listas."),
    ("Raspberry Pi Foundation: PRIMM", "https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_US_PRIMM.pdf", "Referencia del diseño de actividades: predecir, ejecutar, investigar, modificar y crear."),
]
