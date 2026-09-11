window.DSA = {
  "edition": "1.1",
  "units": [
    {
      "number": "1.1",
      "title": "Objetos, tipos y mutabilidad",
      "goal": "Reconocer qué objetos pueden cambiar y qué ocurre cuando una variable señala otro objeto.",
      "question": "Si los enteros no pueden cambiar, ¿por qué funciona `n = n + 1`?",
      "concepts": [
        "En Python trabajamos con objetos. Cada uno tiene un tipo, un valor y una identidad. En `x = 5`, el objeto es de tipo `int` y su valor es `5`. Su identidad permite reconocer ese objeto concreto, aunque otros tengan el mismo valor.",
        "Un objeto mutable puede cambiar su contenido; uno inmutable lo conserva. Una variable es un nombre que señala un objeto. Por eso `n = n + 1` funciona: `n` pasa a señalar el entero resultante. El entero anterior conserva su valor."
      ],
      "table": {
        "headers": [
          "Mutables",
          "Inmutables"
        ],
        "rows": [
          [
            "`list`, `dict`, `set`",
            "`int`, `float`, `bool`, `str`, `tuple`"
          ],
          [
            "Consulta adicional: `bytearray`",
            "Consulta: `complex`, `bytes`, `range`, `frozenset`"
          ]
        ]
      },
      "example": {
        "id": "d01",
        "title": "Una lista cambia; un entero se sustituye",
        "code": "numero = 10\nnumero = numero + 1\ndatos = [10]\ndatos[0] = 11\nprint(numero)\nprint(datos)\n",
        "expected": "11\n[11]\n",
        "explanation": "La suma da `11` y `numero` pasa a señalar ese entero. El entero `10` conserva su valor. En la lista, `datos[0] = 11` reemplaza su primer elemento: cambia la misma lista, no el entero que estaba allí.",
        "questions": []
      },
      "diagram": "mutabilidad",
      "pitfall": "Que una variable muestre otro valor no demuestra que el objeto anterior haya cambiado. Por ejemplo, `upper()` obtiene una cadena en mayúsculas sin modificar la cadena original.",
      "exercises": [
        {
          "id": "E01",
          "title": "Una operación sobre una cadena",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "texto = \"hola\"\nmayusculas = texto.upper()\nprint(texto)\nprint(mayusculas)\n",
              "expected": "hola\nHOLA\n",
              "answer": "`texto.upper()` obtiene la cadena en mayúsculas. La cadena original conserva `hola`, y `texto` sigue señalándola. La variable `mayusculas` señala el resultado: `HOLA`.",
              "change": "",
              "prompts": [
                "¿Se modificó la cadena que señala `texto`? Explica."
              ],
              "options": [
                [
                  "\"hola\"",
                  "None",
                  "HOLA",
                  "hola"
                ],
                [
                  "None",
                  "HOLA",
                  "\"hola\"",
                  "hola"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "texto = \"hola\"\ntexto = texto.upper()\nprint(texto)\n",
              "expected": "HOLA\n",
              "answer": "`texto` pasa a señalar la cadena `HOLA`. La cadena original conserva su contenido. Cambiar la asignación no cambia la mutabilidad de `str`.",
              "change": "Reemplaza la segunda línea por `texto = texto.upper()` y muestra solo `texto`.",
              "prompts": [
                "¿Se modificó la cadena original o cambió la cadena que señala `texto`? ¿Las cadenas siguen siendo inmutables?"
              ],
              "options": [
                [
                  "hola",
                  "HOLA",
                  "None",
                  "\"hola\""
                ]
              ]
            }
          ]
        },
        {
          "id": "E02",
          "title": "Modificar un diccionario",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "alumno = {\"nombre\": \"Ana\", \"edad\": 18}\nalumno[\"edad\"] = 19\nprint(alumno[\"nombre\"])\nprint(alumno[\"edad\"])\n",
              "expected": "Ana\n19\n",
              "answer": "Cambia el diccionario de `alumno`, en la entrada `\"edad\"`. El entero `18` no se transforma en `19`. Los tipos `int`, `str` y `tuple` son inmutables; `list`, `dict` y `set` son mutables.",
              "change": "",
              "prompts": [
                "¿Qué objeto cambió? Clasifica `int`, `str`, `list`, `tuple`, `dict` y `set` según su mutabilidad."
              ],
              "options": [
                [
                  "Ana",
                  "Luis",
                  "\"Ana\"",
                  "None"
                ],
                [
                  "20",
                  "19",
                  "18",
                  "None"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "alumno = {\"nombre\": \"Ana\", \"edad\": 18}\nalumno[\"nombre\"] = \"Luis\"\nprint(alumno[\"nombre\"])\nprint(alumno[\"edad\"])\n",
              "expected": "Luis\n18\n",
              "answer": "Cambia la entrada `\"nombre\"` del diccionario y se conserva la entrada `\"edad\"`. La cadena `\"Ana\"` no se modifica: esa posición del diccionario pasa a señalar `\"Luis\"`.",
              "change": "En lugar de cambiar la edad, cambia `alumno[\"nombre\"]` a `\"Luis\"`.",
              "prompts": [
                "¿Por qué la edad conserva su valor? ¿Cambió el diccionario o se modificó la cadena `\"Ana\"`?"
              ],
              "options": [
                [
                  "\"Ana\"",
                  "Luis",
                  "None",
                  "Ana"
                ],
                [
                  "20",
                  "18",
                  "19",
                  "None"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E01, reemplaza la segunda línea por `texto = texto.upper()` y muestra solo `texto`. ¿Las cadenas dejarían de ser inmutables?",
      "variation_answer": "Se imprimiría `HOLA`. Las cadenas siguen siendo inmutables: ahora `texto` señala la cadena resultante, y la original conserva su contenido.",
      "checkpoint": "Puedo explicar la diferencia entre cambiar un objeto y hacer que una variable señale otro."
    },
    {
      "number": "1.2",
      "title": "Variables, asignación y referencias",
      "goal": "Dibujar las referencias y reconocer cuándo varios nombres señalan el mismo objeto.",
      "question": "Cuando escribes `y = x`, ¿creas otra lista o das otro nombre a la misma lista?",
      "concepts": [
        "Piensa en una variable como una etiqueta y en un objeto como una tarjeta. La referencia es la flecha que une ambos. Con `x = [1, 2, 3]` creamos una lista y la señalamos con `x`. Con `y = x`, también `y` señala esa lista.",
        "La asignación no hace una copia. Si dos nombres señalan el mismo objeto, los llamamos alias. Cuando modificas la lista usando uno, ves el cambio también desde el otro: ambos te llevan a la misma lista."
      ],
      "example": {
        "id": "d02",
        "title": "Dos nombres, una lista",
        "code": "x = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)\nprint(y)\n",
        "expected": "[1, 2, 3, 4]\n[1, 2, 3, 4]\n",
        "explanation": "`x` y `y` señalan la misma lista. Al ejecutar `y.append(4)`, esa lista cambia. Las dos impresiones muestran el cambio porque consultan el mismo objeto.",
        "questions": []
      },
      "diagram": "alias",
      "pitfall": "Dos nombres no significan dos objetos. Cuenta las cajas de objetos y sigue las flechas. Los folios A y B de los dibujos son simbólicos; no son direcciones reales.",
      "exercises": [
        {
          "id": "E03",
          "title": "Una tercera referencia",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "a = [7]\nb = a\nc = b\nc.append(8)\nprint(a)\nprint(b)\nprint(c)\n",
              "expected": "[7, 8]\n[7, 8]\n[7, 8]\n",
              "answer": "Se crea una sola lista. Los nombres `a`, `b` y `c` la señalan. La instrucción `c.append(8)` la modifica; las asignaciones anteriores no hicieron copias.",
              "change": "",
              "prompts": [
                "Describe las referencias de `a`, `b` y `c`. ¿Cuántas listas se crearon?"
              ],
              "options": [
                [
                  "[7, 8]",
                  "[8]",
                  "[[7], 8]",
                  "[7]"
                ],
                [
                  "[[7], 8]",
                  "[8]",
                  "[7]",
                  "[7, 8]"
                ],
                [
                  "[8]",
                  "[[7], 8]",
                  "[7]",
                  "[7, 8]"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "a = [7]\nb = [7]\nc = b\nc.append(8)\nprint(a)\nprint(b)\nprint(c)\n",
              "expected": "[7]\n[7, 8]\n[7, 8]\n",
              "answer": "`a` señala una lista; `b` y `c` comparten otra. Se crearon dos listas. Solo la segunda recibe el `8`.",
              "change": "Cambia solo `b = a` por `b = [7]`. Mantén `c = b`.",
              "prompts": [
                "Describe qué nombres comparten una lista y cuántas listas se crearon."
              ],
              "options": [
                [
                  "[7, 8]",
                  "[7]",
                  "[8]",
                  "[[7], 8]"
                ],
                [
                  "[8]",
                  "[7]",
                  "[7, 8]",
                  "[[7], 8]"
                ],
                [
                  "[7]",
                  "[7, 8]",
                  "[[7], 8]",
                  "[8]"
                ]
              ]
            }
          ]
        },
        {
          "id": "E04",
          "title": "La misma asignación con enteros",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "a = 7\nb = a\nb = b + 1\nprint(a)\nprint(b)\n",
              "expected": "7\n8\n",
              "answer": "Después de `b = a`, ambos nombres señalan el entero `7`. La suma hace que `b` pase a señalar el `8`. La variable `a` sigue señalando el `7`, que conserva su valor.",
              "change": "",
              "prompts": [
                "Describe qué señalan `a` y `b` al final. ¿Se modificó el entero `7`?"
              ],
              "options": [
                [
                  "7",
                  "None",
                  "14",
                  "8"
                ],
                [
                  "None",
                  "14",
                  "7",
                  "8"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "a = 7\nb = a\nb = b\nprint(a)\nprint(b)\n",
              "expected": "7\n7\n",
              "answer": "No. La etiqueta `b` vuelve a quedar en la misma tarjeta, la del `7`. Hay una asignación, pero no se cambia de objeto.",
              "change": "Sustituye la última asignación por `b = b`.",
              "prompts": [
                "¿La asignación `b = b` hace que `b` señale otro objeto? Explícalo con las tarjetas."
              ],
              "options": [
                [
                  "8",
                  "None",
                  "7",
                  "14"
                ],
                [
                  "None",
                  "8",
                  "7",
                  "14"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E03, cambia únicamente `b = a` por `b = [7]`. Conserva `c = b`. ¿Qué se imprimirá y cuántas listas habrá?",
      "variation_answer": "Se imprimen `[7]`, `[7, 8]` y `[7, 8]`. La variable `a` señala una lista; `b` y `c` comparten la segunda, creada con `[7]`.",
      "checkpoint": "Puedo contar los objetos sin confundirlos con los nombres que los señalan."
    },
    {
      "number": "1.3",
      "title": "Identidad e igualdad",
      "goal": "Predecir si dos nombres señalan el mismo objeto, sin memorizar números de identificación.",
      "question": "¿Dos listas que imprimen lo mismo tienen que ser la misma lista?",
      "concepts": [
        "La identidad distingue a un objeto concreto. En la analogía, es el folio de la tarjeta; la flecha representa la referencia. Para nuestras listas, `==` compara el contenido e `is` comprueba si se trata del mismo objeto. Dos listas pueden ser iguales y tener identidades distintas.",
        "La función `id(objeto)` devuelve un número que identifica al objeto mientras existe. En CPython es su dirección de memoria; en otras implementaciones no tiene que serlo. Compararemos si los identificadores coinciden entre objetos que existen al mismo tiempo."
      ],
      "example": {
        "id": "d03",
        "title": "Iguales no significa compartidas",
        "code": "a = [1, 2]\nb = a\nc = [1, 2]\nprint(a == c)\nprint(a is c)\nprint(a is b)\nprint(id(a) == id(b))\n",
        "expected": "True\nFalse\nTrue\nTrue\n",
        "explanation": "`a` y `b` comparten una lista. La variable `c` señala otra con el mismo contenido. Por eso `a == c` da `True`, pero `a is c` da `False`. Los identificadores de `a` y `b` coinciden porque señalan el mismo objeto.",
        "questions": []
      },
      "diagram": "identidad",
      "pitfall": "Usa `==` para comparar valores. Con números y cadenas, Python puede reutilizar objetos: no saques reglas generales a partir de `is` entre literales. Cuando un objeto deja de existir, su identificador puede reutilizarse.",
      "exercises": [
        {
          "id": "E05",
          "title": "Tres comparaciones",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "a = [5]\nb = [5]\nc = a\nprint(a == b)\nprint(a is b)\nprint(b is c)\nprint(id(a) == id(c))\n",
              "expected": "True\nFalse\nFalse\nTrue\n",
              "answer": "`a` y `c` comparten una lista; `b` señala otra. Las dos listas contienen `5`, pero son objetos distintos. La última comparación da `True` porque `a` y `c` señalan el mismo objeto.",
              "change": "",
              "prompts": [
                "Describe las dos listas e indica qué nombres señalan el mismo objeto."
              ],
              "options": [
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "a = [5]\nb = [5]\nc = b\nprint(a == b)\nprint(a is b)\nprint(b is c)\nprint(id(a) == id(c))\n",
              "expected": "True\nFalse\nTrue\nFalse\n",
              "answer": "Cambian la tercera y la cuarta. Ahora `b` y `c` señalan la misma lista, y `a` señala otra.",
              "change": "Cambia únicamente `c = a` por `c = b`.",
              "prompts": [
                "¿Cuáles de las cuatro respuestas cambian respecto al caso inicial? ¿Por qué?"
              ],
              "options": [
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        },
        {
          "id": "E06",
          "title": "Objetos vacíos",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "x = []\ny = x\nz = []\nprint(x == z)\nprint(x is y)\nprint(id(y) == id(z))\n",
              "expected": "True\nTrue\nFalse\n",
              "answer": "Cada `[]` crea otra lista. Las listas de `x` y `z` están vacías y son iguales, pero son objetos distintos. La variable `y` comparte la de `x`. No se puede exigir un valor numérico fijo para `id(x)` entre ejecuciones.",
              "change": "",
              "prompts": [
                "¿Podemos exigir un número específico como respuesta a `id(x)` en cualquier ejecución? Explica."
              ],
              "options": [
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "x = []\ny = x\nz = y\nprint(x == z)\nprint(x is y)\nprint(id(y) == id(z))\n",
              "expected": "True\nTrue\nTrue\n",
              "answer": "Hay una sola lista, señalada por `x`, `y` y `z`. Los identificadores coinciden porque todos esos nombres te llevan al mismo objeto.",
              "change": "Cambia la creación de `z` por `z = y`.",
              "prompts": [
                "¿Cuántas listas existen ahora? ¿Por qué coinciden los identificadores?"
              ],
              "options": [
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E05, cambia únicamente `c = a` por `c = b`. ¿Cuáles de las cuatro respuestas cambian?",
      "variation_answer": "Ahora se imprime `True`, `False`, `True` y `False`: cambian la tercera y la cuarta respuesta. En E06 no podemos exigir un número fijo para `id(x)`; buscamos saber si dos identificadores coinciden.",
      "checkpoint": "Puedo explicar cuándo dos listas son iguales y cuándo son la misma lista."
    },
    {
      "number": "1.4",
      "title": "Mutación y reasignación",
      "goal": "Distinguir si una instrucción modifica un objeto o cambia el objeto que señala una variable.",
      "question": "Si `x` y `y` comparten una lista, ¿por qué `y.append(4)` y `y = y + [4]` afectan de forma distinta lo que vemos mediante `x`?",
      "concepts": [
        "Mutar es cambiar un objeto existente. Por ejemplo, `x.append(3)` agrega un elemento a la misma lista. Asignar es indicar qué objeto señala un nombre: con `x = x` seguimos en el mismo; con `x = x + [3]` señalamos una lista nueva.",
        "Con listas, `+` crea otra lista y `+=` amplía la existente. Con enteros, `+=` hace que el nombre señale el resultado de la suma. Antes de decidir qué cambia, mira el tipo de objeto y la operación."
      ],
      "example": {
        "id": "d04",
        "title": "La concatenación crea otra lista",
        "code": "x = [1, 2, 3]\ny = x\ny = y + [4]\nprint(x)\nprint(y)\nprint(x is y)\n",
        "expected": "[1, 2, 3]\n[1, 2, 3, 4]\nFalse\n",
        "explanation": "Primero, `y + [4]` crea otra lista. Después, `y` pasa a señalarla. La variable `x` sigue señalando la lista inicial. Si hubiéramos usado `y.append(4)`, habría cambiado la lista compartida y lo veríamos también mediante `x`.",
        "questions": []
      },
      "diagram": "reasignacion",
      "pitfall": "`x.clear()` vacía la misma lista; `x = []` hace que `x` señale otra. Los métodos `append()` y `clear()` devuelven `None`: si escribes `x = x.append(4)`, al final `x` señalará `None`.",
      "exercises": [
        {
          "id": "E07",
          "title": "La suma aumentada sobre una lista",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "x = [1, 2]\ny = x\ny += [3]\nprint(x)\nprint(y)\nprint(x is y)\n",
              "expected": "[1, 2, 3]\n[1, 2, 3]\nTrue\n",
              "answer": "Con listas, `+=` agrega elementos a la misma lista. Por eso `x` y `y` siguen compartiéndola. En D04, la operación `+` creó otra lista y después `y` pasó a señalarla.",
              "change": "",
              "prompts": [
                "¿Qué diferencia hay con D04, donde se utiliza `y = y + [4]`?"
              ],
              "options": [
                [
                  "[1, 2]",
                  "[3]",
                  "None",
                  "[1, 2, 3]"
                ],
                [
                  "[1, 2]",
                  "[3]",
                  "[1, 2, 3]",
                  "None"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "x = [1, 2]\ny = x\ny = y + [3]\nprint(x)\nprint(y)\nprint(x is y)\n",
              "expected": "[1, 2]\n[1, 2, 3]\nFalse\n",
              "answer": "`+` crea otra lista y `y` pasa a señalarla. En el caso de los enteros, `a` sigue señalando el `10` y `b` pasa al `13`. El entero inicial conserva su valor.",
              "change": "Cambia `y += [3]` por `y = y + [3]`.",
              "prompts": [
                "Explica por qué ahora `x` y `y` señalan listas distintas. Después analiza `a = 10; b = a; b += 3`: ¿qué señala cada nombre?"
              ],
              "options": [
                [
                  "[1, 2, 3]",
                  "[3]",
                  "[1, 2]",
                  "None"
                ],
                [
                  "[1, 2, 3]",
                  "[3]",
                  "[1, 2]",
                  "None"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        },
        {
          "id": "E08",
          "title": "Vaciar y después reasignar",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "x = [1, 2]\ny = x\ny.clear()\ny = [9]\nprint(x)\nprint(y)\nprint(x is y)\n",
              "expected": "[]\n[9]\nFalse\n",
              "answer": "Primero, `y.clear()` vacía la lista compartida. Después, `y = [9]` crea otra lista y hace que `y` la señale. La variable `x` sigue señalando la lista vacía.",
              "change": "",
              "prompts": [
                "Describe las referencias después de `y.clear()` y al final. ¿Qué línea modifica la lista y cuál reasigna `y`?"
              ],
              "options": [
                [
                  "[9]",
                  "[]",
                  "[1, 2]",
                  "[1, 2, 9]"
                ],
                [
                  "[1, 2]",
                  "[]",
                  "[9]",
                  "[1, 2, 9]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "x = [1, 2]\ny = x\ny = []\ny = [9]\nprint(x)\nprint(y)\nprint(x is y)\n",
              "expected": "[1, 2]\n[9]\nFalse\n",
              "answer": "La lista de `x` conserva `[1, 2]`. Primero `y` pasa a señalar una lista vacía y luego otra con `[9]`. Ninguna de esas asignaciones modifica la lista inicial.",
              "change": "Cambia `y.clear()` por `y = []` y conserva el resto.",
              "prompts": [
                "¿Se llegó a vaciar la lista de `x`? Describe las dos asignaciones a `y`."
              ],
              "options": [
                [
                  "[1, 2, 9]",
                  "[9]",
                  "[1, 2]",
                  "[]"
                ],
                [
                  "[9]",
                  "[]",
                  "[1, 2, 9]",
                  "[1, 2]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E07, cambia `y += [3]` por `y = y + [3]`. Después analiza `a = 10; b = a; b += 3`. ¿Qué cambia en cada caso?",
      "variation_answer": "Con listas se imprime `[1, 2]`, `[1, 2, 3]` y `False`: la suma crea otra lista. Con enteros, `a` sigue señalando el `10` y `b` pasa a señalar el `13`. El entero `10` conserva su valor.",
      "checkpoint": "Puedo decir qué objeto señala cada nombre antes y después de una instrucción.",
      "lab": "p01"
    },
    {
      "number": "1.5",
      "title": "Referencias en funciones",
      "goal": "Explicar cuándo una función modifica un objeto compartido y cuándo entrega un resultado con `return`.",
      "question": "¿Por qué una función puede agregar elementos a tu lista, pero escribir `lst = []` dentro de ella no la vacía?",
      "concepts": [
        "Al llamar a una función, sus parámetros se convierten en nombres locales para los objetos recibidos. Es como añadir una etiqueta a cada tarjeta. Python pasa argumentos por asignación: esta regla funciona igual con listas, diccionarios, enteros y cadenas.",
        "Si la función modifica un objeto compartido, puedes ver el cambio fuera de ella. Si reasigna su parámetro, solo cambia lo que señala ese nombre local. Para entregar un resultado al código que la llamó, usa `return` y guarda ese resultado cuando lo necesites."
      ],
      "example": {
        "id": "d05",
        "title": "Dos funciones sobre el mismo argumento",
        "code": "def add_item(lst):\n    lst.append(\"X\")\n\ndef reset_list(lst):\n    lst = []\n\nmy_list = []\nadd_item(my_list)\nreset_list(my_list)\nprint(my_list)\n",
        "expected": "['X']\n",
        "explanation": "`add_item()` agrega `\"X\"` a la lista compartida por `my_list` y `lst`. En `reset_list()`, la instrucción `lst = []` hace que solo el parámetro local señale otra lista. La variable `my_list` sigue señalando la primera.",
        "questions": []
      },
      "diagram": "funciones",
      "pitfall": "Las listas y los enteros siguen la misma regla al entrar a una función. La diferencia está en qué operaciones permiten. Si una función termina sin ejecutar `return` con un valor, devuelve `None`.",
      "exercises": [
        {
          "id": "E09",
          "title": "Reasignar dentro de la función",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "def modify(lst):\n    lst = lst + [99]\n\nnumbers = [1, 2, 3]\nmodify(numbers)\nprint(numbers)\n",
              "expected": "[1, 2, 3]\n",
              "answer": "`lst + [99]` crea otra lista, y solo el parámetro `lst` pasa a señalarla. La variable `numbers` conserva la lista inicial. Con `lst.append(99)` sí cambiaría esa lista compartida.",
              "change": "",
              "prompts": [
                "Describe las listas durante la llamada. ¿Qué cambiaría si la función usara `lst.append(99)`?"
              ],
              "options": [
                [
                  "[99]",
                  "None",
                  "[1, 2, 3, 99]",
                  "[1, 2, 3]"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "def modify(lst):\n    return lst + [99]\n\nnumbers = [1, 2, 3]\nmodify(numbers)\nprint(numbers)\nnumbers = modify(numbers)\nprint(numbers)\n",
              "expected": "[1, 2, 3]\n[1, 2, 3, 99]\n",
              "answer": "La primera llamada devuelve una lista que no guardamos. La segunda también devuelve otra lista, pero ahora la asignamos a `numbers`. La función no modifica la lista recibida.",
              "change": "Devuelve la lista resultante. Primero ignora el resultado y luego guárdalo en `numbers`.",
              "prompts": [
                "¿Por qué las dos llamadas producen efectos distintos sobre lo que señala `numbers`?"
              ],
              "options": [
                [
                  "[99]",
                  "None",
                  "[1, 2, 3]",
                  "[1, 2, 3, 99]"
                ],
                [
                  "[99]",
                  "[1, 2, 3]",
                  "[1, 2, 3, 99]",
                  "None"
                ]
              ]
            }
          ]
        },
        {
          "id": "E10",
          "title": "Actualizar y reiniciar un diccionario",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "def update_dict(d):\n    d[\"key\"] = \"value\"\n\ndef reset_dict(d):\n    d = {}\n\nmy_dict = {}\nupdate_dict(my_dict)\nreset_dict(my_dict)\nprint(my_dict)\n",
              "expected": "{'key': 'value'}\n",
              "answer": "`update_dict()` modifica el diccionario de `my_dict`. La función `reset_dict()` solo hace que su parámetro `d` señale otro diccionario. Para vaciar el recibido, podría ejecutar `d.clear()`.",
              "change": "",
              "prompts": [
                "Identifica la mutación y la reasignación de `d`. Propón una línea para vaciar el diccionario recibido."
              ],
              "options": [
                [
                  "{}",
                  "{'key': None}",
                  "None",
                  "{'key': 'value'}"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "def update_dict(d):\n    d[\"key\"] = \"value\"\n\ndef reset_dict(d):\n    d.clear()\n\nmy_dict = {}\nupdate_dict(my_dict)\nreset_dict(my_dict)\nprint(my_dict)\n",
              "expected": "{}\n",
              "answer": "`d.clear()` vacía el diccionario compartido. El parámetro `d` y la variable `my_dict` siguen señalando ese mismo objeto.",
              "change": "En `reset_dict()`, reemplaza `d = {}` por `d.clear()`.",
              "prompts": [
                "¿Qué hace que ahora el cambio sea visible mediante `my_dict`?"
              ],
              "options": [
                [
                  "{}",
                  "None",
                  "{'key': 'value'}",
                  "{'key': None}"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E09, haz que la función devuelva `lst + [99]`. Compara `modify(numbers)` con `numbers = modify(numbers)`: ¿en cuál guardas la lista resultante?",
      "variation_answer": "Sin guardar el resultado, `numbers` conserva `[1, 2, 3]`. Al asignarlo, señala `[1, 2, 3, 99]`. Si usas `lst.append(99)`, cambia la lista original. En E10, `d.clear()` vacía el diccionario recibido.",
      "checkpoint": "Puedo explicar qué cambia fuera de una función y cuándo necesito guardar lo que devuelve.",
      "lab": "p02"
    },
    {
      "number": "1.6",
      "title": "Copias de listas simples",
      "goal": "Elegir entre compartir una lista o copiarla para modificarla por separado.",
      "question": "¿Qué cambia si escribes `copia = original.copy()` en lugar de `copia = original`?",
      "concepts": [
        "Con `original.copy()` creas otra lista. Sus posiciones empiezan señalando los mismos elementos que la original. A esto lo llamamos copia superficial: copias la lista exterior, pero no haces nuevas copias de cada objeto que contiene.",
        "También puedes copiar una lista con `original[:]`. Si contiene enteros, cadenas o booleanos, cambiar una posición de la copia no modifica la lista original. Lo que cambia es qué objeto ocupa esa posición de la lista nueva."
      ],
      "example": {
        "id": "d06",
        "title": "Una copia con elementos inmutables",
        "code": "original = [1, 2, \"hola\", True]\ncopia = original.copy()\ncopia[0] = 99\nprint(original)\nprint(copia)\nprint(original is copia)\n",
        "expected": "[1, 2, 'hola', True]\n[99, 2, 'hola', True]\nFalse\n",
        "explanation": "Hay dos listas. Reemplazar la primera posición de `copia` no cambia la de `original`. Los demás elementos pueden seguir siendo los mismos objetos inmutables, aunque las listas que los contienen sean distintas.",
        "questions": []
      },
      "diagram": "copia_simple",
      "pitfall": "Llamar `copia` a una variable no crea una copia: `copia = original` comparte la lista. Más adelante veremos por qué una tupla que contiene una lista requiere mirar un nivel adicional.",
      "exercises": [
        {
          "id": "E11",
          "title": "Una copia y un alias",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "original = [10, 20]\ncopia = original.copy()\nalias = original\ncopia.append(30)\nalias[0] = 99\nprint(original)\nprint(copia)\n",
              "expected": "[99, 20]\n[10, 20, 30]\n",
              "answer": "`copia` señala otra lista, a la que se agrega `30`. La variable `alias` comparte la lista de `original` y reemplaza su primer elemento por `99`. Son dos cambios sobre dos listas distintas.",
              "change": "",
              "prompts": [
                "Describe las dos listas e indica qué nombres comparten una."
              ],
              "options": [
                [
                  "[10, 20, 30]",
                  "[10, 20]",
                  "[99, 20, 30]",
                  "[99, 20]"
                ],
                [
                  "[10, 20]",
                  "[10, 20, 30]",
                  "[99, 20, 30]",
                  "[99, 20]"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "original = [10, 20]\ncopia = original.copy()\nalias = copia\ncopia.append(30)\nalias[0] = 99\nprint(original)\nprint(copia)\n",
              "expected": "[10, 20]\n[99, 20, 30]\n",
              "answer": "`copia` y `alias` señalan la misma lista nueva, que recibe el `30` y el `99`. La lista de `original` conserva sus valores.",
              "change": "Reemplaza `alias = original` por `alias = copia`.",
              "prompts": [
                "¿Qué lista recibe los dos cambios? ¿Qué nombres la comparten?"
              ],
              "options": [
                [
                  "[10, 20, 30]",
                  "[10, 20]",
                  "[99, 20]",
                  "[99, 20, 30]"
                ],
                [
                  "[10, 20, 30]",
                  "[10, 20]",
                  "[99, 20, 30]",
                  "[99, 20]"
                ]
              ]
            }
          ]
        },
        {
          "id": "E12",
          "title": "Copiar mediante un corte",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "a = [\"A\", \"B\"]\nb = a[:]\nprint(a == b)\nprint(a is b)\nb.clear()\nprint(a)\nprint(b)\n",
              "expected": "True\nFalse\n['A', 'B']\n[]\n",
              "answer": "`a[:]` crea otra lista con los mismos elementos. Al principio son iguales, pero `a is b` da `False`. Después, `b.clear()` vacía solamente la lista de `b`.",
              "change": "",
              "prompts": [
                "¿Por qué vaciar la lista de `b` no vacía la de `a`?"
              ],
              "options": [
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "['A']",
                  "[]",
                  "['A', 'B']",
                  "None"
                ],
                [
                  "None",
                  "['A', 'B']",
                  "['A']",
                  "[]"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "a = [\"A\", \"B\"]\nb = a\nprint(a == b)\nprint(a is b)\nb.clear()\nprint(a)\nprint(b)\n",
              "expected": "True\nTrue\n[]\n[]\n",
              "answer": "La asignación no crea otra lista. Los dos nombres comparten la misma, y `b.clear()` la vacía.",
              "change": "Cambia `b = a[:]` por `b = a`.",
              "prompts": [
                "¿Por qué ahora vaciar la lista mediante `b` cambia lo que vemos mediante `a`?"
              ],
              "options": [
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "['A']",
                  "None",
                  "['A', 'B']",
                  "[]"
                ],
                [
                  "['A', 'B']",
                  "['A']",
                  "None",
                  "[]"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E12, cambia `b = a[:]` por `b = a`. Vuelve a predecir las cuatro salidas.",
      "variation_answer": "Se imprime `True`, `True`, `[]` y `[]`. Ahora `a` y `b` comparten una lista y `b.clear()` la vacía. En E11, quienes comparten la misma lista son `original` y `alias`.",
      "checkpoint": "Puedo decidir cuándo compartir una lista y cuándo necesito una copia."
    },
    {
      "number": "1.7",
      "title": "Anidamiento y copia superficial",
      "goal": "Seguir las referencias de una lista anidada y distinguir entre reemplazar una fila y modificarla.",
      "question": "Si copias una lista, ¿pueden seguir compartidas las listas que hay dentro?",
      "concepts": [
        "Una lista puede señalar otras listas. En `original[0][0]`, el primer índice nos lleva a la primera lista interior y el segundo a su primer elemento. Dibuja la lista exterior y cada lista interior en cajas separadas.",
        "Una copia superficial crea otra lista exterior, pero conserva las referencias a las interiores. Así, `copia[0] = [99]` reemplaza una fila de la copia; `copia[0][0] = 99` cambia una fila que puede seguir compartida con `original`."
      ],
      "example": {
        "id": "d07",
        "title": "Dos exteriores y una lista interior",
        "code": "a = [1, 2]\nb = [a, a]\nc = b.copy()\nc[0][0] = 99\nprint(a)\nprint(b)\nprint(c)\nprint(b is c)\n",
        "expected": "[99, 2]\n[[99, 2], [99, 2]]\n[[99, 2], [99, 2]]\nFalse\n",
        "explanation": "`b` y `c` son dos listas exteriores distintas. Las cuatro posiciones entre ambas señalan la misma lista de `a`. La instrucción `c[0][0] = 99` cambia esa lista interior y el cambio se ve al imprimir cualquiera de las dos listas exteriores.",
        "questions": []
      },
      "diagram": "anidamiento",
      "pitfall": "Cuando leas «se hizo una copia», pregunta: ¿de qué objeto? Después identifica cuáles siguen compartidos.",
      "exercises": [
        {
          "id": "E13",
          "title": "Sustituir una fila de la copia",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "original = [[1, 2], [3, 4]]\ncopia = original.copy()\ncopia[0] = [99, 2]\nprint(original)\nprint(copia)\nprint(original[1] is copia[1])\n",
              "expected": "[[1, 2], [3, 4]]\n[[99, 2], [3, 4]]\nTrue\n",
              "answer": "`copia[0] = [99, 2]` reemplaza la primera fila de la copia. La primera fila de `original` conserva su contenido. La segunda fila sigue compartida entre ambas listas exteriores.",
              "change": "",
              "prompts": [
                "¿Qué referencia se reemplazó? ¿Sigue compartida alguna fila?"
              ],
              "options": [
                [
                  "[[99, 2], [3, 4]]",
                  "[99, 2]",
                  "[[1, 2], [3, 4]]",
                  "[[99], [3, 4]]"
                ],
                [
                  "[99, 2]",
                  "[[99, 2], [3, 4]]",
                  "[[1, 2], [3, 4]]",
                  "[[99], [3, 4]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "original = [[1, 2], [3, 4]]\ncopia = original.copy()\ncopia[0] = [1, 2]\nprint(original)\nprint(copia)\nprint(original[0] is copia[0])\n",
              "expected": "[[1, 2], [3, 4]]\n[[1, 2], [3, 4]]\nFalse\n",
              "answer": "La nueva primera fila contiene los mismos números, pero es otra lista. Igual contenido no significa mismo objeto. La segunda fila sí permanece compartida.",
              "change": "Reemplaza la primera fila por otra lista con el mismo contenido: `[1, 2]`. Compara las primeras filas.",
              "prompts": [
                "¿Por qué las impresiones coinciden, pero las primeras filas tienen identidades distintas?"
              ],
              "options": [
                [
                  "[[99], [3, 4]]",
                  "[99, 2]",
                  "[[99, 2], [3, 4]]",
                  "[[1, 2], [3, 4]]"
                ],
                [
                  "[99, 2]",
                  "[[99], [3, 4]]",
                  "[[1, 2], [3, 4]]",
                  "[[99, 2], [3, 4]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        },
        {
          "id": "E14",
          "title": "Modificar una fila compartida",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "original = [[1, 2], [3, 4]]\ncopia = original.copy()\ncopia[0][0] = 99\nprint(original)\nprint(copia)\nprint(original[0] is copia[0])\n",
              "expected": "[[99, 2], [3, 4]]\n[[99, 2], [3, 4]]\nTrue\n",
              "answer": "La primera fila sigue siendo una sola lista compartida. Al cambiar su primer elemento, ves el resultado desde `original` y desde `copia`. En E13 se reemplazó la referencia a la fila; aquí se modifica la fila misma.",
              "change": "",
              "prompts": [
                "Describe ambos niveles. ¿Por qué E13 y E14 afectan de forma distinta a `original`?"
              ],
              "options": [
                [
                  "[[1, 2], [3, 4]]",
                  "[[99, 2], [3, 4]]",
                  "[[5, 6]]",
                  "[[1, 2], [3, 4], [5, 6]]"
                ],
                [
                  "[[1, 2], [3, 4], [5, 6]]",
                  "[[1, 2], [3, 4]]",
                  "[[5, 6]]",
                  "[[99, 2], [3, 4]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "original = [[1, 2], [3, 4]]\ncopia = original.copy()\ncopia.append([5, 6])\nprint(original)\nprint(copia)\nprint(original[0] is copia[0])\n",
              "expected": "[[1, 2], [3, 4]]\n[[1, 2], [3, 4], [5, 6]]\nTrue\n",
              "answer": "Cambia la lista exterior de `copia`: recibe otra fila. Sus dos primeras posiciones conservan las referencias copiadas de `original`.",
              "change": "Reemplaza `copia[0][0] = 99` por `copia.append([5, 6])`.",
              "prompts": [
                "¿Qué lista cambia? ¿Por qué la primera fila sigue compartida?"
              ],
              "options": [
                [
                  "[[99, 2], [3, 4]]",
                  "[[1, 2], [3, 4], [5, 6]]",
                  "[[5, 6]]",
                  "[[1, 2], [3, 4]]"
                ],
                [
                  "[[99, 2], [3, 4]]",
                  "[[1, 2], [3, 4], [5, 6]]",
                  "[[5, 6]]",
                  "[[1, 2], [3, 4]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E14, cambia únicamente `copia[0][0] = 99` por `copia.append([5, 6])`. ¿Qué lista se modifica?",
      "variation_answer": "Solo cambia la lista exterior `copia`. La lista `original` conserva `[[1, 2], [3, 4]]`; la copia queda `[[1, 2], [3, 4], [5, 6]]`. La primera fila sigue compartida: la comparación da `True`.",
      "checkpoint": "Puedo seguir los índices hasta la lista que cambia y reconocer qué partes siguen compartidas."
    },
    {
      "number": "1.8",
      "title": "Repetición de listas y matrices",
      "goal": "Reconocer qué referencias se repiten con `*` y construir matrices cuyas filas puedan cambiar por separado.",
      "question": "¿Por qué modificar una sola celda puede cambiar lo que vemos en las tres filas?",
      "concepts": [
        "Al repetir una lista con `*`, se repiten las referencias a sus elementos. En `[0] * 3` obtienes tres posiciones que señalan el entero `0`. Puedes reemplazar una posición de esa lista sin modificar el entero.",
        "En `[[0] * 3] * 3` hay una sola fila `[0, 0, 0]`: la lista exterior la señala tres veces. Para tener filas independientes, crea una nueva en cada vuelta del ciclo. La expresión `[[0] * 3 for _ in range(3)]` hace justamente eso."
      ],
      "example": {
        "id": "d08",
        "title": "Una fila compartida tres veces",
        "code": "matrix = [[0] * 3] * 3\nmatrix[0][0] = 1\nprint(matrix)\nprint(matrix[0] is matrix[1])\n",
        "expected": "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\nTrue\n",
        "explanation": "Hay una lista exterior y una sola fila interior. La instrucción `matrix[0][0] = 1` cambia esa fila. Como las tres posiciones de la lista exterior señalan la misma fila, el cambio aparece tres veces al imprimir.",
        "questions": []
      },
      "diagram": "matrices",
      "pitfall": "La comprensión evalúa `[0] * 3` en cada vuelta. Usamos `_` porque no necesitamos el contador. Con `a = [0]` y `[a * 3] * 3`, también se crea una sola fila nueva y se comparte tres veces.",
      "exercises": [
        {
          "id": "E15",
          "title": "Una variable explícita",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "a = [0]\nmatrix = [a * 3] * 3\nmatrix[0][0] = 1\nprint(a)\nprint(matrix)\nprint(matrix[0] is matrix[2])\n",
              "expected": "[0]\n[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\nTrue\n",
              "answer": "`a * 3` crea una fila distinta de la lista de `a`. La lista exterior la señala tres veces. Cambia esa fila, mientras `a` conserva `[0]`. Al final, desde `a` y `matrix` puedes llegar a tres listas: la de `a`, la fila y la exterior.",
              "change": "",
              "prompts": [
                "¿La lista de `a` y la fila creada por `a * 3` son el mismo objeto? Explica."
              ],
              "options": [
                [
                  "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
                  "[0]",
                  "[1]",
                  "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]"
                ],
                [
                  "[0]",
                  "[1]",
                  "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
                  "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "a = [0]\nmatrix = [(a * 3).copy() for _ in range(3)]\nmatrix[0][0] = 1\nprint(a)\nprint(matrix)\nprint(matrix[0] is matrix[2])\n",
              "expected": "[0]\n[[1, 0, 0], [0, 0, 0], [0, 0, 0]]\nFalse\n",
              "answer": "No hace falta: `a * 3` ya crea una fila nueva en cada vuelta. Copiar tres veces la lista `a = [0]` produciría 3 filas y 1 columna.",
              "change": "Construye las filas con `matrix = [(a * 3).copy() for _ in range(3)]`.",
              "prompts": [
                "¿Hace falta `.copy()` aquí? Si `a = [0]`, ¿cuántas filas y columnas tendría `[a.copy(), a.copy(), a.copy()]`?"
              ],
              "options": [
                [
                  "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
                  "[1]",
                  "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]",
                  "[0]"
                ],
                [
                  "[0]",
                  "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
                  "[1]",
                  "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        },
        {
          "id": "E16",
          "title": "Construcción con un ciclo",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "matrix = []\nfor _ in range(3):\n    matrix.append([0] * 3)\nmatrix[0][0] = 1\nprint(matrix)\nprint(matrix[0] is matrix[1])\n",
              "expected": "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]\nFalse\n",
              "answer": "Cada vuelta del ciclo crea otra fila. Al cambiar una celda de la primera, las otras dos conservan su contenido. Puedes escribir la construcción como `matrix = [[0] * 3 for _ in range(3)]`.",
              "change": "",
              "prompts": [
                "¿Cuántas filas distintas hay? Escribe la construcción con una comprensión de listas."
              ],
              "options": [
                [
                  "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]",
                  "[[1], [0], [0]]",
                  "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
                  "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "matrix = []\nfila = [0] * 3\nfor _ in range(3):\n    matrix.append(fila)\nmatrix[0][0] = 1\nprint(matrix)\nprint(matrix[0] is matrix[1])\n",
              "expected": "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\nTrue\n",
              "answer": "El ciclo añade tres referencias a la misma fila. Para tener filas independientes, la creación de la lista debe ocurrir dentro de cada vuelta.",
              "change": "Crea una sola fila antes del ciclo y agrégala en cada vuelta.",
              "prompts": [
                "¿Por qué usar un ciclo no garantiza por sí solo tener filas independientes?"
              ],
              "options": [
                [
                  "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
                  "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]",
                  "[[1], [0], [0]]",
                  "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E15, usa `matrix = [(a * 3).copy() for _ in range(3)]`. ¿Hace falta `.copy()` aquí? Con `a = [0]`, ¿qué tamaño tendría `[a.copy(), a.copy(), a.copy()]`?",
      "variation_answer": "Las filas son independientes. Aquí sobra `.copy()`, porque `a * 3` ya crea otra fila en cada vuelta. En E16 puedes usar `[[0] * 3 for _ in range(3)]`. Si copias tres veces `a = [0]`, obtienes 3 filas y 1 columna.",
      "checkpoint": "Puedo explicar por qué repetir una fila no equivale a crear varias filas independientes.",
      "lab": "p03"
    },
    {
      "number": "1.9",
      "title": "Copia profunda",
      "goal": "Decidir qué necesitas copiar para modificar los objetos interiores sin afectar los originales.",
      "question": "Si necesito modificar listas interiores sin afectar al original, ¿qué debo copiar?",
      "concepts": [
        "El módulo `copy` viene incluido en Python. Con `copy.copy(objeto)` haces una copia superficial. Con `copy.deepcopy(objeto)` también copias los contenedores interiores de nuestros ejemplos: las listas y los diccionarios anidados.",
        "Elige según lo que necesites cambiar. Una asignación permite compartir el objeto. Una copia superficial separa el contenedor exterior. Una copia profunda permite cambiar los contenedores interiores de estos ejemplos sin modificar los originales."
      ],
      "example": {
        "id": "d09",
        "title": "Separar también las filas",
        "code": "import copy\n\noriginal = [[1, 2], [3, 4]]\nprofunda = copy.deepcopy(original)\nprofunda[0][0] = 99\nprint(original)\nprint(profunda)\nprint(original[0] is profunda[0])\n",
        "expected": "[[1, 2], [3, 4]]\n[[99, 2], [3, 4]]\nFalse\n",
        "explanation": "Se copian la lista exterior y las filas. Ahora `profunda[0]` y `original[0]` son listas distintas: cambiar una no modifica la otra. Para lograrlo no hace falta copiar también cada entero.",
        "questions": []
      },
      "diagram": "profunda",
      "pitfall": "`deepcopy()` puede mantener referencias compartidas dentro de la copia. Si dos posiciones señalaban una sola fila, pueden seguir señalando una sola fila copiada. Para separar esas filas, revisa cómo las construyes.",
      "exercises": [
        {
          "id": "E17",
          "title": "Una lista dentro de un diccionario",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "import copy\n\noriginal = {\"notas\": [8, 9]}\ncopia = copy.deepcopy(original)\ncopia[\"notas\"].append(10)\nprint(original[\"notas\"])\nprint(copia[\"notas\"])\n",
              "expected": "[8, 9]\n[8, 9, 10]\n",
              "answer": "Se copian el diccionario y su lista `\"notas\"`. La instrucción `append(10)` cambia solo la lista copiada. Una copia superficial del diccionario dejaría esa lista compartida.",
              "change": "",
              "prompts": [
                "¿Qué objetos mutables necesitas copiar para que este cambio no afecte al original?"
              ],
              "options": [
                [
                  "None",
                  "[10]",
                  "[8, 9]",
                  "[8, 9, 10]"
                ],
                [
                  "[8, 9, 10]",
                  "[8, 9]",
                  "[10]",
                  "None"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "import copy\n\noriginal = {\"notas\": [8, 9]}\ncopia = original.copy()\ncopia[\"notas\"].append(10)\nprint(original[\"notas\"])\nprint(copia[\"notas\"])\n",
              "expected": "[8, 9, 10]\n[8, 9, 10]\n",
              "answer": "Se copió el diccionario exterior. Su lista `\"notas\"` sigue compartida, así que el cambio se ve desde ambos diccionarios.",
              "change": "Usa `original.copy()` en lugar de `copy.deepcopy(original)`.",
              "prompts": [
                "¿Qué se copió y qué sigue compartido?"
              ],
              "options": [
                [
                  "[8, 9]",
                  "[8, 9, 10]",
                  "[10]",
                  "None"
                ],
                [
                  "None",
                  "[8, 9]",
                  "[10]",
                  "[8, 9, 10]"
                ]
              ]
            }
          ]
        },
        {
          "id": "E18",
          "title": "Una copia profunda conserva un alias interno",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "import copy\n\nfila = [0]\noriginal = [fila, fila]\ncopia = copy.deepcopy(original)\ncopia[0][0] = 7\nprint(original)\nprint(copia)\nprint(copia[0] is copia[1])\nprint(copia[0] is fila)\n",
              "expected": "[[0], [0]]\n[[7], [7]]\nTrue\nFalse\n",
              "answer": "`deepcopy()` copia la fila una vez y usa esa misma copia en las dos posiciones. La fila original conserva `[0]`. Hay independencia respecto al original, pero las dos posiciones de `copia` siguen compartiendo una fila.",
              "change": "",
              "prompts": [
                "¿Las filas de `copia` son independientes de la original? ¿Son independientes entre sí? Explica."
              ],
              "options": [
                [
                  "[[0], [0]]",
                  "[[7], [0]]",
                  "[[0], [7]]",
                  "[[7], [7]]"
                ],
                [
                  "[[0], [0]]",
                  "[[0], [7]]",
                  "[[7], [0]]",
                  "[[7], [7]]"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "import copy\n\nfila = [0]\noriginal = [fila, fila]\ncopia = [elemento.copy() for elemento in original]\ncopia[0][0] = 7\nprint(original)\nprint(copia)\nprint(copia[0] is copia[1])\nprint(copia[0] is fila)\n",
              "expected": "[[0], [0]]\n[[7], [0]]\nFalse\nFalse\n",
              "answer": "Cada vuelta ejecuta `.copy()` y crea otra lista. Las dos posiciones de `copia` terminan señalando filas distintas y ninguna es la fila original.",
              "change": "Usa `copia = [elemento.copy() for elemento in original]`.",
              "prompts": [
                "¿Por qué esta construcción separa las filas entre sí, además de separarlas de la original?"
              ],
              "options": [
                [
                  "[[7], [7]]",
                  "[[7], [0]]",
                  "[[0], [7]]",
                  "[[0], [0]]"
                ],
                [
                  "[[0], [7]]",
                  "[[0], [0]]",
                  "[[7], [7]]",
                  "[[7], [0]]"
                ],
                [
                  "True",
                  "False"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E17, usa `original.copy()`. En E18, usa `copia = [elemento.copy() for elemento in original]`. ¿Qué cambia en cada caso?",
      "variation_answer": "En E17 se imprime `[8, 9, 10]` dos veces: la lista interior sigue compartida. En E18 se imprime `[[0], [0]]`, `[[7], [0]]`, `False` y `False`. Cada vuelta copia la fila por separado; sus elementos son enteros.",
      "checkpoint": "Puedo elegir qué copiar y explicar si la copia comparte objetos con el original o entre sus propias posiciones."
    },
    {
      "number": "1.10",
      "title": "Integración y matices de mutabilidad",
      "goal": "Resolver ejemplos que combinan funciones y contenedores, sin perder de vista qué objeto cambia.",
      "question": "¿Puede cambiar una lista contenida en una tupla aunque la tupla sea inmutable?",
      "concepts": [
        "Una tupla conserva los objetos a los que apuntan sus posiciones: no puedes reemplazarlos. Pero, si uno de ellos es una lista, esa lista sí puede cambiar. Por eso puedes observar contenido diferente al imprimir la tupla sin haber reemplazado ninguno de sus elementos.",
        "Sigue la ruta hasta el objeto que cambia. En `carro[\"motor\"][\"caballos\"] = 300` modificas el diccionario del motor. Copiar solo el diccionario del carro no separa ese motor. Aquí representamos carros, personas y equipos mediante diccionarios."
      ],
      "example": {
        "id": "d10",
        "title": "Una tupla y su lista interior",
        "code": "datos = ([1, 2], \"grupo A\")\nalias = datos\ndatos[0].append(3)\nprint(datos)\nprint(alias is datos)\n",
        "expected": "([1, 2, 3], 'grupo A')\nTrue\n",
        "explanation": "La tupla sigue señalando la misma lista y la misma cadena. Solo cambia la lista interior. Si intentaras `datos[0] = [9]`, tratarías de reemplazar un elemento de la tupla y obtendrías `TypeError`.",
        "questions": []
      },
      "diagram": "tupla",
      "pitfall": "Que haya una tupla no vuelve inmutables los objetos que contiene. Que haya una copia tampoco garantiza que todos los objetos interiores sean independientes.",
      "exercises": [
        {
          "id": "E19",
          "title": "Copiar una lista que contiene una tupla",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "original = [([1], \"A\")]\ncopia = original.copy()\ncopia[0][0].append(2)\nprint(original)\nprint(copia)\nprint(original[0] is copia[0])\n",
              "expected": "[([1, 2], 'A')]\n[([1, 2], 'A')]\nTrue\n",
              "answer": "Se copia la lista exterior, pero su elemento sigue siendo la misma tupla. Esa tupla señala la misma lista interior, a la que se agrega `2`. Continúan compartidas la tupla y la lista que contiene.",
              "change": "",
              "prompts": [
                "Describe los tres niveles. ¿Qué objeto cambia y cuáles siguen compartidos?"
              ],
              "options": [
                [
                  "[([1], 'A')]",
                  "[([2], 'A')]",
                  "[([1, 2], 'A')]",
                  "None"
                ],
                [
                  "[([2], 'A')]",
                  "None",
                  "[([1, 2], 'A')]",
                  "[([1], 'A')]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "import copy\n\noriginal = [([1], \"A\")]\ncopia = copy.deepcopy(original)\ncopia[0][0].append(2)\nprint(original)\nprint(copia)\nprint(original[0] is copia[0])\n",
              "expected": "[([1], 'A')]\n[([1, 2], 'A')]\nFalse\n",
              "answer": "La tupla original señala la lista original. Para que la copia señale una lista interior distinta, se necesita otra tupla que la contenga. Cambia solo la lista de la copia.",
              "change": "Importa `copy` y realiza una copia profunda de `original`.",
              "prompts": [
                "¿Por qué se necesita también otra tupla en esta copia, aunque las tuplas sean inmutables?"
              ],
              "options": [
                [
                  "[([2], 'A')]",
                  "[([1, 2], 'A')]",
                  "None",
                  "[([1], 'A')]"
                ],
                [
                  "None",
                  "[([1, 2], 'A')]",
                  "[([2], 'A')]",
                  "[([1], 'A')]"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        },
        {
          "id": "E20",
          "title": "Dos carros comparten motor",
          "cases": [
            {
              "key": "inicial",
              "label": "Caso inicial",
              "code": "motor = {\"caballos\": 200}\ncarro1 = {\"marca\": \"Toyota\", \"motor\": motor}\ncarro2 = carro1.copy()\ncarro2[\"marca\"] = \"Honda\"\ncarro2[\"motor\"][\"caballos\"] = 300\nprint(carro1[\"marca\"])\nprint(carro1[\"motor\"][\"caballos\"])\nprint(carro1[\"motor\"] is carro2[\"motor\"])\n",
              "expected": "Toyota\n300\nTrue\n",
              "answer": "Los carros son diccionarios distintos: cambiar `carro2[\"marca\"]` no afecta a `carro1`. Sin embargo, comparten el diccionario `motor`, que ahora contiene `300` caballos. Para conservar el motor original, puedes usar `copy.deepcopy(carro1)`.",
              "change": "",
              "prompts": [
                "¿Por qué la marca y el motor se comportan de forma distinta? Propón cómo conservar el motor de `carro1`."
              ],
              "options": [
                [
                  "None",
                  "Honda",
                  "Toyota",
                  "\"Toyota\""
                ],
                [
                  "Se produce un error antes de imprimir",
                  "200",
                  "None",
                  "300"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            },
            {
              "key": "variacion",
              "label": "Variación",
              "code": "import copy\n\nmotor = {\"caballos\": 200}\ncarro1 = {\"marca\": \"Toyota\", \"motor\": motor}\ncarro2 = copy.deepcopy(carro1)\ncarro2[\"marca\"] = \"Honda\"\ncarro2[\"motor\"][\"caballos\"] = 300\nprint(carro1[\"marca\"])\nprint(carro1[\"motor\"][\"caballos\"])\nprint(carro1[\"motor\"] is carro2[\"motor\"])\n",
              "expected": "Toyota\n200\nFalse\n",
              "answer": "Se copian el diccionario del carro y el del motor. Cada carro tiene ahora su propio motor: cambiar los caballos de uno no modifica el otro.",
              "change": "Importa `copy` y reemplaza la copia superficial por `copy.deepcopy(carro1)`.",
              "prompts": [
                "¿Qué objetos quedan separados y por qué el motor original conserva sus caballos?"
              ],
              "options": [
                [
                  "Toyota",
                  "None",
                  "\"Toyota\"",
                  "Honda"
                ],
                [
                  "300",
                  "Se produce un error antes de imprimir",
                  "200",
                  "None"
                ],
                [
                  "True",
                  "False"
                ]
              ]
            }
          ]
        }
      ],
      "variation": "En E20, importa `copy` y usa `copy.deepcopy(carro1)`. En D10, compara `datos[0].append(3)` con `datos[0] = [3]`: ¿qué objeto intenta modificar cada operación?",
      "variation_answer": "E20 imprime `Toyota`, `200` y `False`: la copia tiene su propio diccionario del motor. En D10, `append(3)` cambia la lista interior; `datos[0] = [3]` intenta reemplazar un elemento de la tupla y produce `TypeError`.",
      "checkpoint": "Puedo localizar y corregir un cambio compartido inesperado explicando cada paso.",
      "lab": "p04"
    }
  ],
  "labs": [
    {
      "id": "P01",
      "section": "1.4",
      "title": "Identidad y cambios de estado",
      "goal": "Comprobar qué ocurre al ampliar una lista compartida, crear otra lista y sumar a un entero.",
      "tasks": [
        "Predice la salida y dibuja las referencias del programa inicial.",
        "Ejecuta el archivo. Conserva tu predicción y explica las diferencias que encuentres.",
        "Variante A: cambia solo `y += [3]` por `y = y + [3]`. Predice y vuelve a ejecutar desde el inicio.",
        "Variante B: haz que las listas de `x` y `y` terminen vacías y sigan siendo el mismo objeto. Elige entre `y.clear()` y `y = []`, y comprueba tu decisión."
      ],
      "cases": [
        {
          "key": "inicial",
          "label": "Programa inicial",
          "code": "x = [1, 2]\ny = x\ny += [3]\na = 10\nb = a\nb += 3\nprint(x)\nprint(x is y)\nprint(a, b)\n",
          "expected": "[1, 2, 3]\nTrue\n10 13\n",
          "change": "",
          "prompts": [
            "Describe qué objetos se comparten en el programa inicial y explica sus salidas.",
            "Escribe tu propuesta de código para resolver la práctica. Incluye las variantes solicitadas.",
            "Explica cómo comprobarías tu propuesta y qué resultados esperas. Si ya ejecutaste el código, registra lo que observaste."
          ],
          "answer": "La lista compartida crece. El entero conserva su valor: `b` pasa a señalar el resultado de la suma.",
          "review": [
            "Inicial: se imprime `[1, 2, 3]`, `True` y `10 13`. La lista cambia; el entero `10` conserva su valor.",
            "Variante A: se imprime `[1, 2]`, `False` y `10 13`. La operación `+` crea otra lista y `y` pasa a señalarla.",
            "Variante B: `y.clear()` cumple ambas condiciones. Puedes imprimir `y` y comprobar `id(x) == id(y)`: debe dar `True`."
          ],
          "solution": {
            "id": "s01",
            "title": "Solución de la variante B",
            "code": "x = [1, 2]\ny = x\ny.clear()\na = 10\nb = a\nb += 3\nprint(x)\nprint(x is y)\nprint(a, b)\n",
            "expected": "[]\nTrue\n10 13\n",
            "explanation": "`clear()` vacía la lista que comparten `x` y `y`. Con `y = []`, la lista de `x` conservaría su contenido y los nombres señalarían listas distintas.",
            "questions": []
          },
          "options": [
            [
              "[]",
              "[1, 2, 3]",
              "None",
              "Se produce un error antes de imprimir"
            ],
            [
              "True",
              "False"
            ],
            [
              "10 13",
              "None",
              "Se produce un error antes de imprimir"
            ]
          ]
        }
      ]
    },
    {
      "id": "P02",
      "section": "1.5",
      "title": "Modificar, reasignar y devolver",
      "goal": "Decidir si una función debe modificar la lista recibida o devolver otra lista.",
      "tasks": [
        "Predice lo que se imprime mediante `original` y `resultado`. Dibuja qué señalan `original` y `datos` dentro de la función.",
        "Variante A: reemplaza el cuerpo por `datos.append(99)`, sin añadir `return`. Vuelve a predecir las salidas.",
        "Variante B: conserva la lista de `original` y devuelve otra con `99` al final. Guárdala en `resultado` y compara ambas identidades.",
        "En la variante B, llama a `agregar_final(original)` sin guardar el resultado. ¿Qué lista puedes seguir consultando mediante `original`?"
      ],
      "cases": [
        {
          "key": "inicial",
          "label": "Programa inicial",
          "code": "def agregar_final(datos):\n    datos = datos + [99]\n\noriginal = [1, 2]\nresultado = agregar_final(original)\nprint(original)\nprint(resultado)\n",
          "expected": "[1, 2]\nNone\n",
          "change": "",
          "prompts": [
            "Describe qué objetos se comparten en el programa inicial y explica sus salidas.",
            "Escribe tu propuesta de código para resolver la práctica. Incluye las variantes solicitadas.",
            "Explica cómo comprobarías tu propuesta y qué resultados esperas. Si ya ejecutaste el código, registra lo que observaste."
          ],
          "answer": "La función hace que `datos` señale otra lista y termina sin devolverla. La lista de `original` conserva su contenido, y `resultado` recibe `None`.",
          "review": [
            "Inicial: se imprime `[1, 2]` y `None`. Dentro de la función, `datos` termina señalando otra lista, `[1, 2, 99]`, mientras `original` conserva la primera.",
            "Variante A: la lista de `original` cambia a `[1, 2, 99]`. La variable `resultado` sigue recibiendo `None`: la función termina sin devolver un valor.",
            "Variante B: la función devuelve otra lista. Si no guardas ese resultado, `original` sigue señalando `[1, 2]` y no conservas un nombre para la lista nueva."
          ],
          "solution": {
            "id": "s02",
            "title": "Solución de la variante B",
            "code": "def agregar_final(datos):\n    return datos + [99]\n\noriginal = [1, 2]\nresultado = agregar_final(original)\nprint(original)\nprint(resultado)\nprint(original is resultado)\n",
            "expected": "[1, 2]\n[1, 2, 99]\nFalse\n",
            "explanation": "`return` entrega la lista nueva al código que llamó a la función. La variable `resultado` la señala, mientras `original` conserva la primera lista.",
            "questions": []
          },
          "options": [
            [
              "[1, 2]",
              "None",
              "Se produce un error antes de imprimir"
            ],
            [
              "[1, 2, 99]",
              "Se produce un error antes de imprimir",
              "None"
            ]
          ]
        }
      ]
    },
    {
      "id": "P03",
      "section": "1.8",
      "title": "Construir filas independientes",
      "goal": "Separar dos decisiones: crear filas independientes y copiar esas filas para otra matriz.",
      "tasks": [
        "Dibuja las listas exteriores y sus filas. Predice las cuatro salidas y después ejecuta.",
        "Variante A: construye `matrix` con un ciclo que cree una fila en cada vuelta. Conserva `copia = matrix.copy()`. ¿Qué filas siguen compartidas?",
        "Variante B: además de crear filas independientes, copia cada fila para que cambiar una celda de `copia` no cambie `matrix`. Usa lo aprendido hasta 1.8.",
        "Comprueba con `is` si las filas son distintas entre sí y si cada original es distinta de su copia. Compara identidades; no escribas números fijos de `id()`."
      ],
      "cases": [
        {
          "key": "inicial",
          "label": "Programa inicial",
          "code": "matrix = [[0] * 3] * 3\ncopia = matrix.copy()\ncopia[0][0] = 1\nprint(matrix)\nprint(copia)\nprint(matrix is copia)\nprint(matrix[0] is copia[0])\n",
          "expected": "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\n[[1, 0, 0], [1, 0, 0], [1, 0, 0]]\nFalse\nTrue\n",
          "change": "",
          "prompts": [
            "Describe qué objetos se comparten en el programa inicial y explica sus salidas.",
            "Escribe tu propuesta de código para resolver la práctica. Incluye las variantes solicitadas.",
            "Explica cómo comprobarías tu propuesta y qué resultados esperas. Si ya ejecutaste el código, registra lo que observaste."
          ],
          "answer": "`copy()` crea otra lista exterior, pero ambas siguen señalando una sola fila compartida.",
          "review": [
            "Inicial: ambas matrices muestran tres veces `[1, 0, 0]`. Las listas exteriores son distintas, pero todas sus posiciones señalan la misma fila.",
            "Variante A: `matrix` y `copia` muestran `[[1, 0, 0], [0, 0, 0], [0, 0, 0]]`. Las filas de `matrix` son distintas entre sí, pero cada una sigue compartida con su posición en `copia`.",
            "Variante B: se separan las listas exteriores y cada fila. Para estas celdas enteras, una copia de cada fila es suficiente. Si hubiera otros objetos mutables dentro, revisaríamos ese nivel también."
          ],
          "solution": {
            "id": "s03",
            "title": "Solución de la variante B",
            "code": "matrix = [[0] * 3 for _ in range(3)]\ncopia = [fila.copy() for fila in matrix]\ncopia[0][0] = 1\nprint(matrix)\nprint(copia)\nprint(copia[0] is copia[1])\nprint(matrix[0] is copia[0])\n",
            "expected": "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]\n[[1, 0, 0], [0, 0, 0], [0, 0, 0]]\nFalse\nFalse\n",
            "explanation": "Cada fila se crea por separado y después se copia por separado. Como las celdas contienen enteros, basta con copiar estos dos niveles para cambiarlas sin afectar la matriz original.",
            "questions": []
          },
          "options": [
            [
              "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
              "Se produce un error antes de imprimir",
              "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]",
              "None"
            ],
            [
              "None",
              "[[1, 0, 0], [0, 0, 0], [0, 0, 0]]",
              "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
              "Se produce un error antes de imprimir"
            ],
            [
              "True",
              "False"
            ],
            [
              "True",
              "False"
            ]
          ]
        }
      ]
    },
    {
      "id": "P04",
      "section": "1.10",
      "title": "Un equipo de trabajo independiente",
      "goal": "Usar funciones y copia profunda para modificar un equipo sin alterar los datos del original.",
      "tasks": [
        "Antes de ejecutar, dibuja el equipo, la lista `\"miembros\"` y el diccionario de Ana. Predice las dos salidas.",
        "Corrige `preparar_equipo()` para que el equipo devuelto cambie de nombre y edad sin modificar los objetos de `original` y `ana`.",
        "Compara con `is` tres niveles: equipo, lista de miembros y primer diccionario de persona. Explica cada resultado.",
        "Después, cambia la edad de Ana en el original. Comprueba que la copia conserva su edad y explica qué demuestra."
      ],
      "cases": [
        {
          "key": "inicial",
          "label": "Programa inicial",
          "code": "def preparar_equipo(equipo):\n    nuevo = equipo.copy()\n    nuevo[\"nombre\"] = \"Pruebas\"\n    nuevo[\"miembros\"][0][\"edad\"] = 99\n    return nuevo\n\nana = {\"nombre\": \"Ana\", \"edad\": 25}\noriginal = {\"nombre\": \"Desarrollo\", \"miembros\": [ana]}\ncopia = preparar_equipo(original)\nprint(original[\"nombre\"], ana[\"edad\"])\nprint(copia[\"nombre\"], copia[\"miembros\"][0][\"edad\"])\n",
          "expected": "Desarrollo 99\nPruebas 99\n",
          "change": "",
          "prompts": [
            "Describe qué objetos se comparten en el programa inicial y explica sus salidas.",
            "Escribe tu propuesta de código para resolver la práctica. Incluye las variantes solicitadas.",
            "Explica cómo comprobarías tu propuesta y qué resultados esperas. Si ya ejecutaste el código, registra lo que observaste."
          ],
          "answer": "Se crea otro diccionario exterior, pero se comparten la lista `\"miembros\"` y el diccionario de Ana. Por eso la edad también cambia al consultarla mediante `ana`.",
          "review": [
            "Inicial: se imprime `Desarrollo 99` y `Pruebas 99`. Solo se copió el diccionario exterior. El nombre del equipo cambia por separado, pero la edad pertenece a un diccionario compartido.",
            "Con la solución se imprime `Desarrollo 25` y `Pruebas 99`. Las tres comparaciones dan `False`: se copiaron el equipo, la lista de miembros y el diccionario de la persona.",
            "Si después escribes `ana[\"edad\"] = 26`, el equipo original muestra `26` y la copia conserva `99`. Los dos equipos tienen diccionarios de persona independientes."
          ],
          "solution": {
            "id": "s04",
            "title": "Una solución con copia profunda",
            "code": "import copy\n\ndef preparar_equipo(equipo):\n    nuevo = copy.deepcopy(equipo)\n    nuevo[\"nombre\"] = \"Pruebas\"\n    nuevo[\"miembros\"][0][\"edad\"] = 99\n    return nuevo\n\nana = {\"nombre\": \"Ana\", \"edad\": 25}\noriginal = {\"nombre\": \"Desarrollo\", \"miembros\": [ana]}\ncopia = preparar_equipo(original)\nprint(original[\"nombre\"], ana[\"edad\"])\nprint(copia[\"nombre\"], copia[\"miembros\"][0][\"edad\"])\nprint(original is copia)\nprint(original[\"miembros\"] is copia[\"miembros\"])\nprint(ana is copia[\"miembros\"][0])\n",
            "expected": "Desarrollo 25\nPruebas 99\nFalse\nFalse\nFalse\n",
            "explanation": "`deepcopy()` separa los tres niveles mutables. La función devuelve el nuevo diccionario y la variable `copia` lo conserva.",
            "questions": []
          },
          "options": [
            [
              "None",
              "Se produce un error antes de imprimir",
              "Desarrollo 99",
              "Desarrollo 25"
            ],
            [
              "Pruebas 99",
              "Se produce un error antes de imprimir",
              "None"
            ]
          ]
        }
      ]
    }
  ],
  "analogy": {
    "title": "Tarjetas, etiquetas y flechas",
    "intro": "Imagina tarjetas con números impresos. Una tiene el 5 y otra el 6. Como representan enteros, no podemos borrar el número para escribir otro. Cada tarjeta tiene además un folio que permite reconocerla.",
    "labels": "La variable `x` es una etiqueta: señala una tarjeta. Si lo dibujamos, la flecha es la referencia y el folio representa la identidad. A y B son folios inventados para el dibujo; no son resultados de `id()`.",
    "table": {
      "headers": [
        "Concepto",
        "En `x = 5`"
      ],
      "rows": [
        [
          "Nombre",
          "La etiqueta `x`."
        ],
        [
          "Referencia",
          "La flecha desde `x` hasta la tarjeta."
        ],
        [
          "Tipo",
          "`int`: la tarjeta representa un entero."
        ],
        [
          "Valor",
          "El número `5` impreso en la tarjeta."
        ],
        [
          "Identidad",
          "La tarjeta concreta, que distinguimos con su folio A."
        ]
      ]
    },
    "same": "Con `x = x`, miramos qué tarjeta señala `x` y volvemos a colocar la etiqueta en esa tarjeta. Hay una asignación, pero la etiqueta termina donde ya estaba.",
    "other": "Con `x = x + 1`, leemos el 5, sumamos 1 y colocamos `x` en la tarjeta del 6. No cambiamos el número de la primera tarjeta: ahora señalamos otra.",
    "code": "x = 5\nidentificador_inicial = id(x)\nx = x\nprint(id(x) == identificador_inicial)\nx = x + 1\nprint(id(x) == identificador_inicial)\n",
    "expected": "True\nFalse\n",
    "conclusion": "La identidad pertenece al objeto. Una asignación puede dejar una variable señalando el mismo objeto o hacer que señale otro. En este ejemplo, cuando cambia `id(x)`, cambia el objeto que señala `x`; ninguna tarjeta cambia de identidad."
  },
  "sources": [
    [
      "Python: objetos, valores y tipos",
      "https://docs.python.org/3/reference/datamodel.html#objects-values-and-types",
      "Consulta para 1.1-1.3 y 1.10: mutabilidad, identidad y contenedores."
    ],
    [
      "Python: asignación de argumentos",
      "https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference",
      "Consulta para 1.5: asociación de parámetros y uso de valores devueltos."
    ],
    [
      "Python: copia superficial y profunda",
      "https://docs.python.org/3/library/copy.html",
      "Consulta para 1.6, 1.7 y 1.9: operaciones del módulo copy."
    ],
    [
      "Python: operaciones de secuencias",
      "https://docs.python.org/3/library/stdtypes.html#common-sequence-operations",
      "Consulta para 1.8: repetición de referencias y construcción de listas."
    ],
    [
      "Raspberry Pi Foundation: PRIMM",
      "https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_US_PRIMM.pdf",
      "Referencia del diseño de actividades: predecir, ejecutar, investigar, modificar y crear."
    ]
  ]
};
