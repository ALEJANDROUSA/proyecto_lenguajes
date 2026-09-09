# Documento de Alcance — Arcanum

**Curso:** Lenguajes de Programación y Transducción — Semestre 2026-2
**Corte:** 1 — Especificación y front-end del lenguaje
**Temática:** Alquimia / magia aplicada a un DSL de ciencia de datos

---

## 1. Nombre y motivación del lenguaje

**Arcanum** es un lenguaje de dominio específico (DSL) para describir
flujos de carga, preparación y visualización de datos, bajo la idea de
que la ciencia de datos consiste en "revelar información oculta a partir
de datos crudos", igual que un alquimista revela conocimiento oculto a
partir de ingredientes. La correspondencia temática es:

| Concepto de Arcanum | Concepto de ciencia de datos |
|---|---|
| Grimorio | El programa completo (el archivo `.arc`) |
| Hechizo | Cada instrucción (una línea del programa) |
| Poción | El conjunto de datos resultante de un hechizo (nunca se modifica una poción existente; cada hechizo produce una poción nueva) |
| Ingrediente | Una columna dentro de una poción |
| Artefacto | El resultado de una visualización |

## 2. Dominio y casos de uso

El dominio es la **ciencia de datos y la visualización**, restringido en
este primer corte a:

- Declaración de variables mediante expresiones aritméticas y booleanas.
- Carga de un conjunto de datos desde un archivo CSV (`invocar`).
- Selección de columnas de una poción (`recolectar`).
- Filtrado de filas mediante comparaciones y conectores lógicos
  (`purificar ... donde`, con `y`, `o`, `no` y paréntesis).
- Reconocimiento sintáctico (sin ejecución todavía) de una instrucción de
  visualización (`forjar artefacto`).

Casos de uso representativos:

1. Un analista describe en un archivo `.arc` cómo cargar un CSV, quedarse
   con ciertas columnas y descartar filas inválidas antes de analizarlas.
2. Un estudiante valida que su grimorio esté bien escrito antes de que el
   motor de ejecución (Corte 2) lo procese contra datos reales.
3. El equipo docente evalúa programas con errores intencionales (léxicos
   o sintácticos) para comprobar que el compilador los detecta y reporta
   con número de línea y columna.

## 3. Usuarios del lenguaje

- **Estudiantes/analistas de datos** que describen un flujo de
  preparación de datos sin escribir Python directamente.
- **El equipo docente**, como evaluador que revisa programas de ejemplo
  correctos e incorrectos para verificar la robustez del compilador.
- **El propio equipo de desarrollo**, que extenderá este front-end
  (Lexer/Parser) en los cortes 2 y 3 con la semántica real y la
  generación de gráficas.

## 4. Entradas y salidas

| | Entrada | Salida |
|---|---|---|
| Corte 1 (este entregable) | Archivo de texto plano `.arc` con un grimorio | Árbol de análisis sintáctico impreso en consola, o lista de errores léxicos/sintácticos con línea y columna |
| Corte 2 (futuro) | Grimorio válido + archivos CSV referenciados | Pociones (DataFrames de pandas) en memoria, estadísticas, CSV de salida |
| Corte 3 (futuro) | Grimorio válido + datos procesados | Artefactos (archivos PNG con gráficas), ejecución completa por CLI |

## 5. Restricciones del lenguaje (Corte 1)

- No se implementan aún funciones definidas por el usuario ni ciclos;
  no son necesarios para el dominio de pipelines de datos declarativos.
- La instrucción `forjar artefacto` se **reconoce sintácticamente pero no
  se ejecuta**: no se genera ninguna gráfica todavía.
- No se implementa aún la tabla de símbolos ni la validación de tipos
  entre columnas (llegan en el Corte 2).
- Solo se soporta la carga de archivos `.csv`.
- Las palabras reservadas de Arcanum se escriben en **minúsculas**
  (`invocar`, `recolectar`, `purificar`, `forjar`...), a diferencia de
  otros lenguajes de la clase que usan mayúsculas; esto es una decisión
  de estilo del equipo, no una limitación técnica.
- Un identificador de usuario no puede coincidir exactamente con una
  palabra reservada (por ejemplo, no se puede llamar una variable
  `invocar`), porque el Lexer siempre reconoce primero las palabras
  reservadas.

## 6. Producto verificable de este corte

1. **Reconoce** programas válidos del DSL (`examples/valido_*.arc`).
2. **Genera el árbol de análisis** sintáctico completo (`main.py`
   lo imprime en consola con la función `imprimir_arbol`).
3. **Reporta errores comprensibles**, con número de línea y columna,
   ante programas inválidos (`examples/invalido_*.arc`).
