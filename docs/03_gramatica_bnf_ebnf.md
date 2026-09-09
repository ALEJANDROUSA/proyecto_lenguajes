# Gramática formal — Arcanum (Corte 1)

Esta es la especificación formal que respalda el archivo `grammar/Arcanum.g4`.
Se presenta primero en **EBNF** (la notación más cercana a como está
escrita en ANTLR) y luego su equivalente en **BNF**.

## 1. Notación EBNF

```ebnf
programa              ::= hechizo+ ;

hechizo                ::= asignacion | instruccionForjar ;

asignacion             ::= ID "=" expresion ";" ;

expresion              ::= invocarExpr
                          | recolectarExpr
                          | purificarExpr
                          | expresionAritmetica ;

invocarExpr            ::= "invocar" "desde" CADENA ;

recolectarExpr         ::= "recolectar" "[" listaIds "]" "de" ID ;

purificarExpr          ::= "purificar" ID "donde" condicion ;

listaIds               ::= ID ( "," ID )* ;

instruccionForjar       ::= "forjar" "artefacto" ID "desde" ID "con" listaParametros ";" ;

listaParametros         ::= parametro ( "," parametro )* ;

parametro               ::= "eje_x" ID
                           | "eje_y" ID
                           | "titulo" CADENA ;

condicion                ::= condicion "y" condicion
                            | condicion "o" condicion
                            | "no" condicion
                            | "(" condicion ")"
                            | comparacion ;

comparacion              ::= expresionAritmetica operadorComparacion expresionAritmetica ;

operadorComparacion      ::= ">" | "<" | ">=" | "<=" | "==" | "!=" ;

expresionAritmetica       ::= expresionAritmetica ( "*" | "/" ) expresionAritmetica
                             | expresionAritmetica ( "+" | "-" ) expresionAritmetica
                             | "(" expresionAritmetica ")"
                             | NUMERO
                             | CADENA
                             | ( "verdadero" | "falso" )
                             | ID ;
```

> **Nota sobre `condicion` y `expresionAritmetica`:** están escritas con
> **recursión izquierda** (la propia regla aparece al principio de su
> definición). Esto es válido en una gramática libre de contexto (BNF es
> exactamente eso) y ANTLR4, a diferencia de ANTLR3, sabe manejarlo
> directamente. El **orden** en que se listan las alternativas es lo que
> le indica a ANTLR la precedencia: en `expresionAritmetica`, la
> alternativa de `*`/`/` está antes que la de `+`/`-`, por lo que
> `*`/`/` se evalúa primero (más "pegado"). Lo mismo ocurre en
> `condicion`, donde `y` está antes que `o`.

## 2. Notación BNF

La BNF clásica no admite `*`, `+`, `?` ni agrupaciones `(...)`, así que
cada operador de repetición/opcionalidad se traduce a recursión y a
producciones alternativas explícitas (incluyendo la producción vacía
`ε`). La recursión izquierda de `condicion` y `expresionAritmetica` se
conserva tal cual, porque es una construcción legítima en BNF (el
problema de la recursión izquierda es exclusivo de los parsers
descendentes recursivos simples/LL clásicos, no de la notación BNF en sí).

```bnf
<programa>              ::= <hechizo> <programa> | <hechizo>

<hechizo>                ::= <asignacion> | <instruccion-forjar>

<asignacion>             ::= <id> "=" <expresion> ";"

<expresion>              ::= <invocar-expr>
                            | <recolectar-expr>
                            | <purificar-expr>
                            | <expresion-aritmetica>

<invocar-expr>           ::= "invocar" "desde" <cadena>

<recolectar-expr>        ::= "recolectar" "[" <lista-ids> "]" "de" <id>

<purificar-expr>         ::= "purificar" <id> "donde" <condicion>

<lista-ids>              ::= <id> <resto-ids>
<resto-ids>              ::= "," <id> <resto-ids> | ε

<instruccion-forjar>      ::= "forjar" "artefacto" <id> "desde" <id> "con" <lista-parametros> ";"

<lista-parametros>        ::= <parametro> <resto-parametros>
<resto-parametros>        ::= "," <parametro> <resto-parametros> | ε

<parametro>               ::= "eje_x" <id>
                             | "eje_y" <id>
                             | "titulo" <cadena>

<condicion>                ::= <condicion> "y" <condicion>
                              | <condicion> "o" <condicion>
                              | "no" <condicion>
                              | "(" <condicion> ")"
                              | <comparacion>

<comparacion>              ::= <expresion-aritmetica> <op-comparacion> <expresion-aritmetica>

<op-comparacion>           ::= ">" | "<" | ">=" | "<=" | "==" | "!="

<expresion-aritmetica>      ::= <expresion-aritmetica> "*" <expresion-aritmetica>
                               | <expresion-aritmetica> "/" <expresion-aritmetica>
                               | <expresion-aritmetica> "+" <expresion-aritmetica>
                               | <expresion-aritmetica> "-" <expresion-aritmetica>
                               | "(" <expresion-aritmetica> ")"
                               | <numero>
                               | <cadena>
                               | "verdadero"
                               | "falso"
                               | <id>
```

## 3. Diagrama del AFD (Autómata Finito Determinista) del Lexer

ANTLR construye internamente un AFD (o más precisamente un autómata que
combina todos los tokens mediante el algoritmo de construcción de
subconjuntos) a partir de cada expresión regular del Lexer. A modo de
ejemplo docente, este es el AFD simplificado del token `CADENA`
(`'"' (~["\r\n])* '"'`):

```
             cualquier caracter
             excepto " \r \n
                  ┌────────┐
                  │        │
                  ▼        │
 ┌───────┐   "   ┌─────────┐   "   ┌─────────┐
▶│  q0   │──────▶│   q1    │──────▶│ q2 (*)  │
 └───────┘       └─────────┘       └─────────┘
```

- `q0`: estado inicial, antes de leer la primera comilla.
- `q1`: ya se leyó la comilla de apertura; se queda en `q1` mientras lea
  cualquier caracter que no sea `"`, `\r` o `\n` (por eso la
  auto-transición).
- `q2`: estado de aceptación, alcanzado al leer la comilla de cierre.
- Si el AFD llega a un salto de línea estando en `q1` sin haber visto la
  comilla de cierre, no hay transición válida: el Lexer reporta un error
  léxico (esto es justamente lo que provoca el error en
  `examples/invalido_lexico.arc`, que tiene una cadena sin comilla de
  cierre).

El mismo principio (un AFD por token, combinados luego por ANTLR en un
autómata global) aplica a los demás tokens léxicos (`ID`, `NUMERO`,
palabras reservadas, operadores, etc.).
