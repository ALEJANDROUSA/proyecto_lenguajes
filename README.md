# Arcanum

DSL de ciencia de datos con temática de magia. Proyecto de Lenguajes de
Programación y Transducción, primer corte (especificación y front-end del
lenguaje).

## Idea del lenguaje

La ciencia de datos consiste en revelar información oculta a partir de datos
crudos. Arcanum representa cada paso de ese proceso como una operación
mágica:

- **Grimorio**: el programa completo, la secuencia de hechizos.
- **Hechizo**: cada instrucción (una línea del programa).
- **Poción**: el conjunto de datos que resulta de un hechizo. Nunca se
  modifica una poción existente, cada hechizo genera una poción nueva.
- **Ingrediente**: una columna dentro de una poción.
- **Artefacto**: el resultado de una visualización (todavía no se genera en
  este corte, solo se reconoce la instrucción).

## Alcance de este corte

Lo que el lenguaje reconoce ahora mismo:

- Asignaciones y expresiones aritméticas/booleanas básicas.
- `invocar desde "archivo.csv"` — carga de un CSV en una poción.
- `recolectar [col1, col2] de poción` — selección de columnas.
- `purificar poción donde condición` — filtro con comparaciones (`>`, `<`,
  `>=`, `<=`, `==`, `!=`) y conectores lógicos (`y`, `o`, `no`).
- `forjar artefacto tipo desde poción con ...` — instrucción de
  visualización. Solo se valida su sintaxis, todavía no produce ninguna
  gráfica.

Lo que **no** está implementado todavía (corresponde a los siguientes
cortes): ejecución real de las operaciones, tabla de símbolos, estadísticas,
agrupamientos y generación de gráficas de verdad. En este corte el programa
solo verifica que un archivo `.arc` esté bien escrito y muestra su árbol de
análisis.

## Estructura del proyecto

```
arcanum/
├── grammar/
│   └── Arcanum.g4        # gramática ANTLR4 (lexer + parser en un archivo)
├── generated/             # código que genera ANTLR, no se edita a mano
├── docs/
│   ├── 01_documento_alcance.md
│   ├── 02_catalogo_instrucciones.md
│   ├── 03_gramatica_bnf_ebnf.md
│   └── 04_arquitectura_librerias_futuras.md
├── src/
│   ├── main.py            # corre el lexer/parser sobre un archivo .arc
│   └── errores.py         # mensajes de error con línea y columna
├── examples/
├── requirements.txt
└── README.md
```

Ver `docs/01_documento_alcance.md` para el alcance, usuarios,
entradas/salidas y restricciones del lenguaje; `docs/02_catalogo_instrucciones.md`
para el catálogo completo de palabras reservadas, operadores y literales;
`docs/03_gramatica_bnf_ebnf.md` para la gramática formal en BNF/EBNF; y
`docs/04_arquitectura_librerias_futuras.md` para el diseño planeado del
sistema de librerías propias (compendios) de los próximos cortes.

## Instalación

Se necesita Java (para correr ANTLR) y Python 3.

```bash
sudo apt install antlr4
```

Si `apt install antlr4` no está disponible en el sistema (por ejemplo en
Windows), se puede descargar `antlr-4.9.2-complete.jar` manualmente y correr
`java -jar antlr-4.9.2-complete.jar` en vez de `antlr4`. Lo importante es
que la versión del runtime de Python (`requirements.txt`) coincida con la
versión de la herramienta que generó el código; si se usa otra versión de
ANTLR, hay que actualizar también `requirements.txt`.

## Cómo correrlo

Crear y activar el entorno virtual, e instalar las dependencias de Python
dentro de él:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Con el entorno activado, correr un archivo de ejemplo:

```bash
cd src
python3 main.py ../examples/valido_completo.arc
```

Con un archivo correcto, imprime el árbol de análisis completo. Con un
archivo con errores, imprime cada error con línea y columna en vez del árbol.

Para salir del entorno virtual cuando se termine:

```bash
deactivate
```

## Cómo regenerar el lexer y el parser

La carpeta `generated/` ya viene con el código armado, pero si se modifica
`Arcanum.g4` hay que volver a generarlo:

```bash
cd grammar
antlr4 -Dlanguage=Python3 -visitor -o ../generated Arcanum.g4
```

`-visitor` le pide a ANTLR que también genere `ArcanumVisitor.py`, que se
usará en el siguiente corte cuando sí se ejecuten las operaciones sobre los
datos. En este corte no se usa porque no hay semántica que ejecutar
todavía — usar un Visitor vacío hubiera sido código de relleno sin función
real.

### Programas de prueba incluidos

| Archivo | Tipo | Qué demuestra |
|---|---|---|
| `valido_completo.arc` | válido | flujo completo: carga, selección, filtro y visualización |
| `valido_asignaciones.arc` | válido | asignaciones y expresiones aritméticas/booleanas básicas |
| `valido_carga_seleccion.arc` | válido | `invocar` + `recolectar` |
| `valido_filtro_avanzado.arc` | válido | `purificar ... donde` con `y`/`o`/`no` y paréntesis |
| `invalido_lexico.arc` | inválido | cadena sin comilla de cierre + carácter `@` no reconocido |
| `invalido_lexico_caracter.arc` | inválido | carácter `~` no reconocido |
| `invalido_sintactico.arc` | inválido | falta el nombre de la poción después de `purificar`, y expresión incompleta |
| `invalido_sintactico_recolectar.arc` | inválido | falta la palabra reservada `de` en `recolectar` |

Para correrlos todos de una vez y ver el resultado de cada uno:

```bash
cd src
for f in ../examples/*.arc; do
    echo "=== $f ==="
    python3 main.py "$f"
    echo
done
```

## De la gramática al código (para la sustentación)

- **Lexer** (`ArcanumLexer.py`): agrupa los caracteres del archivo en
  tokens (`INVOCAR`, `ID`, `NUMERO`, `CADENA`, etc.). Cada tipo de token es,
  en el fondo, un AFD: por ejemplo, el token `NUMERO` reconoce el lenguaje
  regular "uno o más dígitos, opcionalmente seguidos de un punto y más
  dígitos".
- **Parser** (`ArcanumParser.py`): toma la secuencia de tokens y verifica
  que respete la estructura de las reglas del `.g4` (una gramática libre de
  contexto, más potente que un AFD porque puede anidar estructuras, como
  paréntesis dentro de expresiones).
- **Árbol de análisis**: lo que devuelve `parser.programa()`. Cada nodo es
  una regla de la gramática (por ejemplo `asignacion`) y sus hijos son los
  tokens o sub-reglas que la componen. `main.py` lo recorre con
  `imprimir_arbol` para mostrarlo de forma legible.
- **Manejo de errores**: se reemplazan los listeners por defecto de ANTLR
  (`errores.py`) para capturar cada error con su línea y columna, en vez de
  dejar que ANTLR los imprima con su formato técnico en inglés.

## Palabras reservadas

| Palabra | Significado |
|---|---|
| `invocar`, `desde` | carga de datos desde un archivo |
| `recolectar`, `de` | selección de columnas |
| `purificar`, `donde` | filtro de filas |
| `forjar`, `artefacto`, `con`, `eje_x`, `eje_y`, `titulo` | visualización |
| `y`, `o`, `no` | conectores lógicos |
| `verdadero`, `falso` | literales booleanos |
