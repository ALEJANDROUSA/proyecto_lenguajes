grammar Arcanum;

// Reglas del parser

programa
    : hechizo+ EOF
    ;

hechizo
    : asignacion
    | instruccionForjar
    ;

asignacion
    : ID '=' expresion ';'
    ;

expresion
    : invocarExpr
    | recolectarExpr
    | purificarExpr
    | expresionAritmetica
    ;

invocarExpr
    : INVOCAR DESDE CADENA
    ;

recolectarExpr
    : RECOLECTAR '[' listaIds ']' DE ID
    ;

purificarExpr
    : PURIFICAR ID DONDE condicion
    ;

listaIds
    : ID (',' ID)*
    ;

instruccionForjar
    : FORJAR ARTEFACTO ID DESDE ID CON listaParametros ';'
    ;

listaParametros
    : parametro (',' parametro)*
    ;

parametro
    : EJE_X ID
    | EJE_Y ID
    | TITULO CADENA
    ;

condicion
    : condicion Y condicion              # condicionY
    | condicion O condicion              # condicionO
    | NO condicion                       # condicionNo
    | '(' condicion ')'                  # condicionParentesis
    | comparacion                        # condicionComparacion
    ;

comparacion
    : expresionAritmetica operadorComparacion expresionAritmetica
    ;

operadorComparacion
    : '>' | '<' | '>=' | '<=' | '==' | '!='
    ;

expresionAritmetica
    : expresionAritmetica ( '*' | '/' ) expresionAritmetica   # multDiv
    | expresionAritmetica ( '+' | '-' ) expresionAritmetica   # sumaResta
    | '(' expresionAritmetica ')'                             # parentesis
    | NUMERO                                                  # numero
    | CADENA                                                  # cadenaLiteral
    | ( VERDADERO | FALSO )                                   # booleano
    | ID                                                      # identificador
    ;

// Reglas del lexer

INVOCAR    : 'invocar';
RECOLECTAR : 'recolectar';
PURIFICAR  : 'purificar';
FORJAR     : 'forjar';
ARTEFACTO  : 'artefacto';
DESDE      : 'desde';
DE         : 'de';
DONDE      : 'donde';
CON        : 'con';
EJE_X      : 'eje_x';
EJE_Y      : 'eje_y';
TITULO     : 'titulo';
Y          : 'y';
O          : 'o';
NO         : 'no';
VERDADERO  : 'verdadero';
FALSO      : 'falso';

ID      : [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO  : [0-9]+ ('.' [0-9]+)?;
CADENA  : '"' (~["\r\n])* '"';

COMENTARIO : '#' ~[\r\n]* -> skip;
ESPACIO    : [ \t\r\n]+ -> skip;
