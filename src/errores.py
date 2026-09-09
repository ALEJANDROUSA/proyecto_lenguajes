from antlr4.error.ErrorListener import ErrorListener


class ManejadorErrores(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        texto = f"Línea {line}, columna {column}: {msg}"
        self.errores.append(texto)

    def hay_errores(self):
        return len(self.errores) > 0

    def imprimir(self):
        for err in self.errores:
            print(f"  - {err}")
