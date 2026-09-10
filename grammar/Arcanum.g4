grammar Arcanum;

// REGLAS DEL PARSER
// (definen cómo se combinan los tokens para formar instrucciones válidas)

// Regla inicial (punto de entrada del parser: parser.programa()).
// Un programa es UNA O MÁS instrucciones (hechizo+) y termina en EOF.
programa
    : hechizo+ EOF
    ;

// Cada instrucción del lenguaje ("hechizo") es UNA de estas dos cosas:
// una asignación, o una instrucción de graficar (instruccionForjar).
hechizo
    : asignacion
    | instruccionForjar
    ;

// Acepta cosas como: descuento = 0.10;  |  umbral = 100 * descuento;
// ID '=' expresion ';'
asignacion
    : ID '=' expresion ';'
    ;

// Lo que va a la derecha del '=' puede ser una de cuatro cosas:
// cargar datos, seleccionar columnas, filtrar filas, o un valor/cálculo simple.
expresion
    : invocarExpr
    | recolectarExpr
    | purificarExpr
    | expresionAritmetica
    ;

// *** Aquí está la regla que acepta: clientes = invocar desde "datos/clientes.csv"; ***
// (el "clientes =" lo cubre 'asignacion'; esta regla solo cubre "invocar desde <ruta>")
// INVOCAR DESDE CADENA
invocarExpr
    : INVOCAR DESDE CADENA
    ;

// Acepta: ventas_reducidas = recolectar [fecha, ciudad, categoria] de ventas;
// RECOLECTAR '[' listaIds ']' DE ID
recolectarExpr
    : RECOLECTAR '[' listaIds ']' DE ID
    ;

// Acepta: ventas_validas = purificar ventas_reducidas donde unidades > 0 y precio > 0;
// PURIFICAR ID DONDE condicion
purificarExpr
    : PURIFICAR ID DONDE condicion
    ;

// Uno o más identificadores separados por coma (ej: fecha, ciudad, categoria).
listaIds
    : ID (',' ID)*
    ;

// Acepta: forjar artefacto barras desde ventas_validas con eje_x=ciudad, eje_y=precio, titulo="...";
// FORJAR ARTEFACTO <tipo_grafico> DESDE <tabla> CON <parametros> ';'
instruccionForjar
    : FORJAR ARTEFACTO ID DESDE ID CON listaParametros ';'
    ;

// Uno o más parametros separados por coma.
listaParametros
    : parametro (',' parametro)*
    ;

// Cada parámetro solo puede tener una de estas tres formas.
// Por eso 'titulo "Precios por ciudad"' es válido pero 'titulo ciudad' (sin comillas) no.
parametro
    : EJE_X ID
    | EJE_Y ID
    | TITULO CADENA
    ;

// Regla recursiva para condiciones lógicas (usada en purificarExpr ... DONDE).
// Los nombres después de '#' son etiquetas de alternativa: le indican a ANTLR
// que genere un método de visitor distinto por cada caso (no cambian qué se acepta).
// Ej: "unidades > 0 y precio > 0"  ->  caso condicionY
condicion
    : condicion Y condicion              # condicionY
    | condicion O condicion              # condicionO
    | NO condicion                       # condicionNo
    | '(' condicion ')'                  # condicionParentesis
    | comparacion                        # condicionComparacion
    ;

// Una comparación siempre es: valor operador valor (ej: unidades > 0).
comparacion
    : expresionAritmetica operadorComparacion expresionAritmetica
    ;

// Lista cerrada de los seis operadores de comparación permitidos.
operadorComparacion
    : '>' | '<' | '>=' | '<=' | '==' | '!='
    ;

// Regla recursiva para cálculos y valores. El ORDEN de las alternativas
// define la precedencia: multDiv se evalúa/agrupa antes que sumaResta,
// por eso en "100 * descuento" la multiplicación se arma primero.
expresionAritmetica
    : expresionAritmetica ( '*' | '/' ) expresionAritmetica   # multDiv
    | expresionAritmetica ( '+' | '-' ) expresionAritmetica   # sumaResta
    | '(' expresionAritmetica ')'                             # parentesis
    | NUMERO                                                  # numero
    | CADENA                                                  # cadenaLiteral
    | ( VERDADERO | FALSO )                                   # booleano
    | ID                                                      # identificador
    ;

// REGLAS DEL LEXER
// (definen cómo el texto crudo se trocea en tokens ANTES de que
// el parser trabaje; van en MAYÚSCULAS por convención de ANTLR)

// Palabras clave literales del lenguaje.
// Van ANTES que la regla ID para que, por ejemplo, "invocar" se reconozca
// como la palabra clave INVOCAR y no como un identificador cualquiera.
INVOCAR    : 'invocar';
RECOLECTAR : 'recolectar';
PURIFICAR  : 'purificar';
FORJAR     : 'forjar';
ARTEFACTO  : 'artefacto';

// Palabras de conexión/preposición (enlazan partes de una instrucción).
DESDE      : 'desde';
DE         : 'de';
DONDE      : 'donde';
CON        : 'con';

// Nombres de los parámetros que acepta la instrucción forjar.
EJE_X      : 'eje_x';
EJE_Y      : 'eje_y';
TITULO     : 'titulo';

// Operadores lógicos usados dentro de 'condicion'.
Y          : 'y';
O          : 'o';
NO         : 'no';

// Literales booleanos.
VERDADERO  : 'verdadero';
FALSO      : 'falso';

// Identificador: letra o guion bajo, seguido de letras/dígitos/guion bajo.
// Nombra variables como 'descuento', 'ventas', 'ciudad'.
ID      : [a-zA-Z_][a-zA-Z0-9_]*;

// Número: uno o más dígitos, con parte decimal opcional (acepta 100 y 0.10).
NUMERO  : [0-9]+ ('.' [0-9]+)?;

// Cadena: texto entre comillas dobles. No puede cruzar líneas
// ni contener comillas dobles sin escapar (~["\r\n] = "cualquier
// carácter que no sea comilla doble, retorno de carro o salto de línea").
CADENA  : '"' (~["\r\n])* '"';

// Comentarios de línea: desde '#' hasta el fin de línea se descarta (skip),
// el parser nunca los ve.
COMENTARIO : '#' ~[\r\n]* -> skip;

// Espacios, tabs y saltos de línea también se descartan (skip):
// la indentación no afecta el análisis.
ESPACIO    : [ \t\r\n]+ -> skip;
