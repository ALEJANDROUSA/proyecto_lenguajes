import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "generated"))

from antlr4 import FileStream, CommonTokenStream
from ArcanumLexer import ArcanumLexer
from ArcanumParser import ArcanumParser
from errores import ManejadorErrores


def imprimir_arbol(nodo, parser, sangria=0):
    prefijo = "  " * sangria
    if hasattr(nodo, "getRuleIndex"):
        nombre_regla = parser.ruleNames[nodo.getRuleIndex()]
        print(f"{prefijo}{nombre_regla}")
        for i in range(nodo.getChildCount()):
            imprimir_arbol(nodo.getChild(i), parser, sangria + 1)
    else:
        print(f"{prefijo}'{nodo.getText()}'")


def analizar(ruta_archivo):
    entrada = FileStream(ruta_archivo, encoding="utf-8")

    lexer = ArcanumLexer(entrada)
    manejador_lexico = ManejadorErrores()
    lexer.removeErrorListeners()
    lexer.addErrorListener(manejador_lexico)

    tokens = CommonTokenStream(lexer)

    parser = ArcanumParser(tokens)
    manejador_sintactico = ManejadorErrores()
    parser.removeErrorListeners()
    parser.addErrorListener(manejador_sintactico)

    arbol = parser.programa()

    if manejador_lexico.hay_errores() or manejador_sintactico.hay_errores():
        print(f"El archivo '{ruta_archivo}' tiene errores:\n")
        manejador_lexico.imprimir()
        manejador_sintactico.imprimir()
        return False

    print(f"'{ruta_archivo}' es un programa Arcanum válido.\n")
    print("Árbol de análisis:\n")
    imprimir_arbol(arbol, parser)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 main.py archivo.arc")
        sys.exit(1)

    valido = analizar(sys.argv[1])
    sys.exit(0 if valido else 1)
