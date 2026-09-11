# Etapa 1: Objetos y referencias en memoria

[Abrir la guía imprimible en PDF](output/pdf/guia_objetos_referencias.pdf) · [Abrir la guía web interactiva](https://learning-dsa-objetos-referencias.noisy-spool-3552.chatgpt.site)

La guía está diseñada para estudiar primero en papel y utilizar la computadora en cuatro prácticas de comprobación. El PDF incluye toda la lectura, el código que se debe analizar, diagramas, espacios de respuesta y soluciones razonadas. No necesitas abrir enlaces externos para completar las actividades.

## Usar la versión web

La web alojada es una vista privada de revisión. Para trabajar sin conexión, descarga el repositorio completo y abre `dist/index.html` en un navegador. No requiere servidor, paquetes ni acceso a servicios externos; conserva juntos los archivos de `dist/`.

Elige un tema y alterna entre **Lectura**, **Ejercicios** y, donde corresponde, **Laboratorio**. Cada ejercicio tiene pestañas **Caso inicial** y **Variación**. Las respuestas de cada caso se conservan al cambiar de pestaña durante la sesión y se reinician al recargar la página.

Selecciona todas las líneas de salida y escribe la explicación antes de pulsar **Verificar mis respuestas**. Si falta un campo, la web lo señala y mantiene oculta la solución. Las salidas se comprueban automáticamente; las explicaciones y propuestas de código se contrastan con una respuesta razonada, sin calificarlas automáticamente. Si editas una respuesta, la revisión se oculta hasta que vuelvas a verificar.

El PDF conserva la secuencia de lectura, ejercicios, espacios para escribir y soluciones posteriores. Ahora incluye la analogía de tarjetas y etiquetas, código destacado dentro del texto y referencias uniformes como **E01**.

## Contenido

| Tema | Conceptos |
| --- | --- |
| 1.1 | Objetos, tipos y mutabilidad |
| 1.2 | Variables, asignación y referencias |
| 1.3 | Identidad e igualdad |
| 1.4 | Mutación y reasignación |
| 1.5 | Referencias en funciones |
| 1.6 | Copias de listas simples |
| 1.7 | Contenedores anidados y copia superficial |
| 1.8 | Repetición de listas y matrices |
| 1.9 | Copia profunda |
| 1.10 | Integración y matices de mutabilidad |

## Archivos para estudiantes

| Ubicación | Uso |
| --- | --- |
| [output/pdf/guia_objetos_referencias.pdf](output/pdf/guia_objetos_referencias.pdf) | Guía de 44 páginas, tamaño carta, con fuentes incorporadas y marcadores de navegación. |
| [ejemplos](ejemplos) | D01–D10: los 10 ejemplos resueltos de las secciones. |
| [ejercicios](ejercicios) | E01–E20: programas para predecir antes de ejecutar. |
| [practicas](practicas) | P01–P04: programas iniciales de las cuatro prácticas. |
| [soluciones](soluciones) | S01–S04: soluciones de referencia de las prácticas; consúltalas después del intento. |
| [diagramas](diagramas) | Diez diagramas vectoriales de referencias. |

### Ejecutar un programa

Abre una terminal en esta carpeta, `etapa_01_objetos_referencias`. No necesitas instalar dependencias para los programas de aprendizaje.

En macOS o Linux:

```bash
python3 ejercicios/e05.py
python3 practicas/p01.py
```

En Windows, con el lanzador de Python disponible:

```powershell
py ejercicios/e05.py
py practicas/p01.py
```

También puedes ejecutar el archivo completo desde tu editor. Si tu instalación utiliza el comando `python`, úsalo en lugar de `python3` o `py`.

Cada programa incluye su propia inicialización. Ejecuta el archivo desde el inicio al cambiar de variante. Si trabajas en un cuaderno interactivo, reinicia el entorno antes de cada ejemplo.

### Prácticas

| Práctica | Momento | Archivo inicial | Solución |
| --- | --- | --- | --- |
| P01: Identidad y cambios de estado | Después de 1.4 | [p01.py](practicas/p01.py) | [s01.py](soluciones/s01.py) |
| P02: Modificar, reasignar y devolver | Después de 1.5 | [p02.py](practicas/p02.py) | [s02.py](soluciones/s02.py) |
| P03: Construir filas independientes | Después de 1.8 | [p03.py](practicas/p03.py) | [s03.py](soluciones/s03.py) |
| P04: Un equipo de trabajo independiente | Después de 1.10 | [p04.py](practicas/p04.py) | [s04.py](soluciones/s04.py) |

Las instrucciones completas, variantes y espacios de registro están en la guía. No basta obtener una salida: explica qué objetos se comparten y qué instrucción produce el cambio.

### Impresión

Selecciona papel carta y una escala del 100 %. El documento funciona en blanco y negro. Puedes imprimirlo por ambas caras; las soluciones aparecen después de los ejercicios y las prácticas. Usa tu cuaderno cuando necesites más espacio para dibujar.

## Edición y verificación docente

La fuente principal es [fuentes/contenido.py](fuentes/contenido.py). Allí se editan explicaciones, programas, salidas esperadas, preguntas y soluciones. La presentación y los diagramas se definen en [herramientas/generar_material.py](herramientas/generar_material.py).

El PDF, `dist/contenido.js`, la copia del PDF servida en `dist/`, los SVG y los scripts de estudiantes son archivos generados. Para mantenerlos sincronizados, modifica la fuente y vuelve a generar el material. La presentación web se edita directamente en `dist/index.html`, `dist/guia.css` y `dist/guia.js`.

Las variaciones y distractores de la web se definen en [fuentes/casos_web.py](fuentes/casos_web.py). La web ofrece 20 variaciones; incluye las 10 de la guía impresa y añade una segunda situación para cada uno de los otros ejercicios.

Las siguientes dependencias solo se necesitan para **editar y verificar la publicación**:

```bash
python3 -m pip install -r herramientas/requirements.txt
python3 herramientas/generar_material.py
python3 herramientas/verificar_material.py
python3 herramientas/verificar_web.py
```

Para comprobar los formularios desde la raíz del repositorio, instala las dependencias de verificación con `npm ci` y ejecuta `npm test`. Se usa un DOM simulado para probar las interacciones; no son paquetes necesarios para abrir la web ni para ejecutar los programas de Python.

El generador:

- Reutiliza exactamente los mismos fragmentos en la guía y en los archivos `.py`.
- Produce páginas con límites definidos y falla si algún contenido no cabe.
- Calcula el índice y los marcadores a partir de la secuencia real de páginas.
- Incorpora las fuentes DejaVu para conservar la legibilidad al imprimir y evitar sustituciones tipográficas.

El verificador ejecuta los **38 programas en procesos independientes**, compara las salidas con las declaradas y comprueba la correspondencia del PDF con sus temas y prácticas. No es un instrumento para calificar las explicaciones de los estudiantes.

Después de editar, revisa visualmente el PDF. Si dispones de Poppler, puedes renderizarlo con:

```bash
pdftoppm -scale-to 1400 -png output/pdf/guia_objetos_referencias.pdf pagina
```

Revisa especialmente bloques de código completos, flechas de los diagramas, espacios para responder y saltos de página. El índice actual corresponde a 44 páginas; actualiza este dato en los README si cambia la extensión.

Las fuentes tipográficas redistribuidas conservan su [licencia original](herramientas/fuentes_tipograficas/LICENSE-DejaVu.txt). Consulta también las [notas docentes](notas_docentes.md).
