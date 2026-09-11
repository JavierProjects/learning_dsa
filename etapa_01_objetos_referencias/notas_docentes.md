# Notas docentes

## Alcance

Este material desarrolla únicamente la etapa de objetos y referencias en memoria. Utiliza los objetos incorporados de Python. Los casos de personas, equipos, carros y motores se representan con listas y diccionarios, de modo que no requieren haber estudiado clases.

## Dinámica sugerida

La secuencia de actividades adapta la idea de predecir, ejecutar, investigar, modificar y crear de PRIMM. La guía combina lectura individual y trabajo en papel con cuatro prácticas locales de Python. Una predicción incorrecta es una oportunidad para identificar una asociación equivocada entre nombres y objetos.

Antes de mostrar la salida o la solución, pide una predicción escrita. Después de ejecutar, solicita una corrección explicada. Para comprobar comprensión, cambia una sola condición y pide una nueva predicción.

No es necesario ejecutar cada fragmento durante la lectura. Los ejemplos D01–D10 están resueltos en el PDF; E01–E20 se predicen en papel. Las prácticas P01–P04 reúnen los momentos de comprobación. El alumno puede recurrir a los scripts correspondientes si necesita investigar una discrepancia después de su intento.

## Aspectos que conviene escuchar en una explicación

- Identifica el objeto concreto afectado y distingue los niveles de un contenedor anidado.
- Separa la mutación del objeto de la reasignación del nombre.
- Justifica qué referencias permanecen compartidas después de una operación.
- Elige y comprueba una corrección que satisface el comportamiento solicitado.

Los números concretos de `id()` nunca son un criterio de evaluación. Se comparan identidades de objetos vivos simultáneamente mediante `is` o la igualdad de sus identificadores. No se utilizan ejemplos cuya respuesta dependa de la reutilización de literales enteros o cadenas.

## Adaptación del material de referencia

| Casos aportados | Lugar en la guía |
| --- | --- |
| `add_item`, `reset_list`, modificación frente a reasignación local | 1.5, E09–E10 y P02 |
| `x`, `y`, `append()` y concatenación | 1.2, 1.4 y P01 |
| `id()` y referencias compartidas | 1.3; comparaciones booleanas |
| Lista simple con inmutables y `.copy()` | 1.6 |
| `original`, `copy`, listas interiores y el caso `a`, `b`, `c` | 1.7 |
| `[[0] * 3] * 3` y `[a * 3] * 3` | 1.8 y P03 |
| Copia profunda | 1.9 |
| Persona, Equipo, Carro y Motor | Adaptaciones con diccionarios en 1.10, E20 y P04 |

Se añadieron ejemplos con cadenas y enteros, igualdad frente a identidad, diferencias entre `+` y `+=`, retorno de funciones, sustitución de filas, tuplas que contienen listas y conservación de alias internos en una copia profunda.

## Precisiones técnicas aplicadas

- Los argumentos se pasan por asignación. El parámetro es un nombre local vinculado al objeto recibido; el lenguaje no usa dos mecanismos diferentes para listas e inmutables.
- `id()` representa la identidad durante la vida del objeto. Su interpretación como dirección de memoria corresponde a CPython; no se asume un número fijo ni un cambio numérico obligatorio en cada ejecución.
- La copia superficial no separa automáticamente los objetos anidados.
- `deepcopy()` puede conservar referencias compartidas dentro de la copia. La independencia respecto al original no equivale a la independencia entre todas las posiciones de la copia.
- Con `a = [0]`, `[a.copy(), a.copy(), a.copy()]` construye tres filas de una columna, no una matriz de tres por tres.
- Las muestras se inicializan de manera independiente. Una demostración de copia profunda no reutiliza accidentalmente un original modificado por una demostración anterior.

## Consulta

- [Modelo de datos de Python](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Asignación de argumentos](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
- [Módulo copy](https://docs.python.org/3/library/copy.html)
- [Operaciones de secuencias](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [PRIMM, Raspberry Pi Foundation](https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_US_PRIMM.pdf)

## Edición 1.1: lectura y práctica web

La analogía distingue cinco elementos: nombre (etiqueta), referencia (flecha), tipo, valor e identidad (folio de la tarjeta). La identidad pertenece al objeto. En `x = x` se hace una asignación sin cambiar de objeto; con `x = x + 1`, para un entero, el nombre pasa a señalar otro objeto. Se conserva la precisión sobre `id()` en CPython y otras implementaciones.

La pregunta de 1.4 explicita que `x` y `y` inicialmente comparten una lista. Pregunta por el contenido observado mediante `x`: `y.append(4)` modifica esa lista; `y = y + [4]` hace que `y` señale una nueva.

En ambos formatos, los nombres, funciones, métodos y expresiones se destacan con tipografía de código. En las referencias de la prosa se escribe E01, D01 o P01; los nombres reales de archivo permanecen en minúsculas.

La web reemplaza la versión completa en Markdown. Incluye 20 casos iniciales, 20 variaciones y las 4 prácticas. Cada caso exige todas sus salidas y respuestas escritas antes de mostrar la revisión. Los campos con solo espacios se consideran vacíos. La revisión de salidas es automática; las explicaciones abiertas y el código propuesto requieren autoevaluación o revisión docente. No se usa IA ni se envían respuestas a un servidor.

Las comprobaciones de interacción usan un DOM simulado y cubren formularios incompletos, respuestas correctas e incorrectas, edición posterior, independencia de las pestañas y conservación de respuestas durante la navegación. No sustituyen una revisión visual en dispositivos reales. La web aloja una copia del mismo PDF y puede distribuirse completa para abrirla sin conexión.
