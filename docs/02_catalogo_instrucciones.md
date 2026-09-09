# Catálogo de Instrucciones — Arcanum

## 1. Palabras reservadas

| Palabra clave | Significado | Equivalente conceptual |
|---|---|---|
| `invocar` | Introduce la carga de un conjunto de datos | (parte de) `pd.read_csv(...)` |
| `desde` | Indica el origen de datos, usada junto a `invocar` y `forjar` | `from` |
| `recolectar` | Selecciona columnas (ingredientes) de una poción | `df[[...]]` |
| `de` | Palabra de enlace usada junto a `recolectar` | `from` |
| `purificar` | Filtra filas de una poción según una condición | `df[condicion]` |
| `donde` | Introduce la condición de un filtro, usada junto a `purificar` | `where` |
| `forjar` | Declara la creación de un artefacto (visualización) | — |
| `artefacto` | Palabra que acompaña a `forjar` para nombrar la visualización | — |
| `con` | Introduce la lista de parámetros de un `forjar` | — |
| `eje_x` / `eje_y` | Parámetros de `forjar` que indican qué columna va en cada eje | `xlabel` / `ylabel` |
| `titulo` | Parámetro de `forjar` para el título de la gráfica | `plt.title(...)` |
| `y` / `o` / `no` | Conectores lógicos usados dentro de una condición | `and` / `or` / `not` |
| `verdadero` / `falso` | Literales booleanos | `True` / `False` |

## 2. Operadores

| Categoría | Operadores | Regla de la gramática |
|---|---|---|
| Asignación | `=` | `asignacion` |
| Relacionales | `>` `<` `>=` `<=` `==` `!=` | `operadorComparacion` |
| Aritméticos | `+` `-` `*` `/` | `expresionAritmetica` |
| Lógicos (palabra reservada) | `y` `o` `no` | `condicion` |
| Agrupación | `(` `)` | `condicionParentesis` / `parentesis` |

La precedencia entre `*`/`/` y `+`/`-` la resuelve directamente ANTLR4
gracias a que `expresionAritmetica` está escrita con **recursión
izquierda** y el orden en que aparecen las alternativas en el archivo
`.g4` (multiplicación/división antes que suma/resta). Lo mismo ocurre
entre `y` y `o` dentro de `condicion`: como `y` aparece antes que `o` en
la gramática, `a y b o c` se interpreta como `(a y b) o c`, igual que en
la mayoría de los lenguajes de programación.

## 3. Literales

| Tipo | Ejemplo | Regla léxica (resumen) |
|---|---|---|
| Número | `100`, `0.15` | `[0-9]+ ('.' [0-9]+)?` |
| Cadena | `"datos/ventas.csv"` | `'"' (~["\r\n])* '"'` |
| Booleano | `verdadero`, `falso` | palabra reservada |
| Identificador | `ventas`, `precio_unitario` | `[a-zA-Z_][a-zA-Z0-9_]*` (no puede coincidir con una palabra reservada) |

## 4. Signos de puntuación

`; [ ] , ( )`

## 5. Comentarios y espacios en blanco

- Comentario de línea: `# esto es un comentario`
- Espacios, tabulaciones y saltos de línea se descartan (`skip`) y no
  generan tokens.

## 6. Sentencias soportadas en el Corte 1

1. **Asignación con carga de datos:**
   `id = invocar desde "archivo.csv";`
2. **Asignación con selección de columnas:**
   `id = recolectar [col1, col2, ...] de id_origen;`
3. **Asignación con filtro:**
   `id = purificar id_origen donde condicion;`
4. **Asignación con expresión aritmética/booleana:**
   `id = expresion_aritmetica;`
5. **Instrucción de visualización (solo reconocida, no ejecutada):**
   `forjar artefacto tipo desde id con parametro, parametro, ...;`
   donde cada `parametro` es `eje_x id`, `eje_y id` o `titulo "texto"`.

Una `condicion` (usada dentro de `purificar ... donde`) puede combinar
comparaciones con `y`, `o`, `no` y agruparlas con paréntesis, por
ejemplo: `(stock > 0 y precio < 100) o categoria == "oferta"`.

## 7. Ejemplo comentado

```text
# Cargamos una pocion de datos
ventas = invocar desde "datos/ventas.csv";

# Seleccionamos ingredientes (columnas) relevantes
ventas_reducidas = recolectar [fecha, ciudad, categoria, unidades, precio] de ventas;

# Filtramos filas validas combinando condiciones con "y"
ventas_validas = purificar ventas_reducidas donde unidades > 0 y precio > 0;

# Instruccion de visualizacion (solo reconocida sintacticamente en Corte 1)
forjar artefacto barras desde ventas_validas con eje_x ciudad, eje_y precio, titulo "Precios por ciudad";
```
