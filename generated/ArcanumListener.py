# Generated from Arcanum.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArcanumParser import ArcanumParser
else:
    from ArcanumParser import ArcanumParser

# This class defines a complete listener for a parse tree produced by ArcanumParser.
class ArcanumListener(ParseTreeListener):

    # Enter a parse tree produced by ArcanumParser#programa.
    def enterPrograma(self, ctx:ArcanumParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ArcanumParser#programa.
    def exitPrograma(self, ctx:ArcanumParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ArcanumParser#hechizo.
    def enterHechizo(self, ctx:ArcanumParser.HechizoContext):
        pass

    # Exit a parse tree produced by ArcanumParser#hechizo.
    def exitHechizo(self, ctx:ArcanumParser.HechizoContext):
        pass


    # Enter a parse tree produced by ArcanumParser#asignacion.
    def enterAsignacion(self, ctx:ArcanumParser.AsignacionContext):
        pass

    # Exit a parse tree produced by ArcanumParser#asignacion.
    def exitAsignacion(self, ctx:ArcanumParser.AsignacionContext):
        pass


    # Enter a parse tree produced by ArcanumParser#expresion.
    def enterExpresion(self, ctx:ArcanumParser.ExpresionContext):
        pass

    # Exit a parse tree produced by ArcanumParser#expresion.
    def exitExpresion(self, ctx:ArcanumParser.ExpresionContext):
        pass


    # Enter a parse tree produced by ArcanumParser#invocarExpr.
    def enterInvocarExpr(self, ctx:ArcanumParser.InvocarExprContext):
        pass

    # Exit a parse tree produced by ArcanumParser#invocarExpr.
    def exitInvocarExpr(self, ctx:ArcanumParser.InvocarExprContext):
        pass


    # Enter a parse tree produced by ArcanumParser#recolectarExpr.
    def enterRecolectarExpr(self, ctx:ArcanumParser.RecolectarExprContext):
        pass

    # Exit a parse tree produced by ArcanumParser#recolectarExpr.
    def exitRecolectarExpr(self, ctx:ArcanumParser.RecolectarExprContext):
        pass


    # Enter a parse tree produced by ArcanumParser#purificarExpr.
    def enterPurificarExpr(self, ctx:ArcanumParser.PurificarExprContext):
        pass

    # Exit a parse tree produced by ArcanumParser#purificarExpr.
    def exitPurificarExpr(self, ctx:ArcanumParser.PurificarExprContext):
        pass


    # Enter a parse tree produced by ArcanumParser#listaIds.
    def enterListaIds(self, ctx:ArcanumParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by ArcanumParser#listaIds.
    def exitListaIds(self, ctx:ArcanumParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by ArcanumParser#instruccionForjar.
    def enterInstruccionForjar(self, ctx:ArcanumParser.InstruccionForjarContext):
        pass

    # Exit a parse tree produced by ArcanumParser#instruccionForjar.
    def exitInstruccionForjar(self, ctx:ArcanumParser.InstruccionForjarContext):
        pass


    # Enter a parse tree produced by ArcanumParser#listaParametros.
    def enterListaParametros(self, ctx:ArcanumParser.ListaParametrosContext):
        pass

    # Exit a parse tree produced by ArcanumParser#listaParametros.
    def exitListaParametros(self, ctx:ArcanumParser.ListaParametrosContext):
        pass


    # Enter a parse tree produced by ArcanumParser#parametro.
    def enterParametro(self, ctx:ArcanumParser.ParametroContext):
        pass

    # Exit a parse tree produced by ArcanumParser#parametro.
    def exitParametro(self, ctx:ArcanumParser.ParametroContext):
        pass


    # Enter a parse tree produced by ArcanumParser#condicionParentesis.
    def enterCondicionParentesis(self, ctx:ArcanumParser.CondicionParentesisContext):
        pass

    # Exit a parse tree produced by ArcanumParser#condicionParentesis.
    def exitCondicionParentesis(self, ctx:ArcanumParser.CondicionParentesisContext):
        pass


    # Enter a parse tree produced by ArcanumParser#condicionComparacion.
    def enterCondicionComparacion(self, ctx:ArcanumParser.CondicionComparacionContext):
        pass

    # Exit a parse tree produced by ArcanumParser#condicionComparacion.
    def exitCondicionComparacion(self, ctx:ArcanumParser.CondicionComparacionContext):
        pass


    # Enter a parse tree produced by ArcanumParser#condicionO.
    def enterCondicionO(self, ctx:ArcanumParser.CondicionOContext):
        pass

    # Exit a parse tree produced by ArcanumParser#condicionO.
    def exitCondicionO(self, ctx:ArcanumParser.CondicionOContext):
        pass


    # Enter a parse tree produced by ArcanumParser#condicionY.
    def enterCondicionY(self, ctx:ArcanumParser.CondicionYContext):
        pass

    # Exit a parse tree produced by ArcanumParser#condicionY.
    def exitCondicionY(self, ctx:ArcanumParser.CondicionYContext):
        pass


    # Enter a parse tree produced by ArcanumParser#condicionNo.
    def enterCondicionNo(self, ctx:ArcanumParser.CondicionNoContext):
        pass

    # Exit a parse tree produced by ArcanumParser#condicionNo.
    def exitCondicionNo(self, ctx:ArcanumParser.CondicionNoContext):
        pass


    # Enter a parse tree produced by ArcanumParser#comparacion.
    def enterComparacion(self, ctx:ArcanumParser.ComparacionContext):
        pass

    # Exit a parse tree produced by ArcanumParser#comparacion.
    def exitComparacion(self, ctx:ArcanumParser.ComparacionContext):
        pass


    # Enter a parse tree produced by ArcanumParser#operadorComparacion.
    def enterOperadorComparacion(self, ctx:ArcanumParser.OperadorComparacionContext):
        pass

    # Exit a parse tree produced by ArcanumParser#operadorComparacion.
    def exitOperadorComparacion(self, ctx:ArcanumParser.OperadorComparacionContext):
        pass


    # Enter a parse tree produced by ArcanumParser#parentesis.
    def enterParentesis(self, ctx:ArcanumParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ArcanumParser#parentesis.
    def exitParentesis(self, ctx:ArcanumParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ArcanumParser#cadenaLiteral.
    def enterCadenaLiteral(self, ctx:ArcanumParser.CadenaLiteralContext):
        pass

    # Exit a parse tree produced by ArcanumParser#cadenaLiteral.
    def exitCadenaLiteral(self, ctx:ArcanumParser.CadenaLiteralContext):
        pass


    # Enter a parse tree produced by ArcanumParser#sumaResta.
    def enterSumaResta(self, ctx:ArcanumParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by ArcanumParser#sumaResta.
    def exitSumaResta(self, ctx:ArcanumParser.SumaRestaContext):
        pass


    # Enter a parse tree produced by ArcanumParser#numero.
    def enterNumero(self, ctx:ArcanumParser.NumeroContext):
        pass

    # Exit a parse tree produced by ArcanumParser#numero.
    def exitNumero(self, ctx:ArcanumParser.NumeroContext):
        pass


    # Enter a parse tree produced by ArcanumParser#multDiv.
    def enterMultDiv(self, ctx:ArcanumParser.MultDivContext):
        pass

    # Exit a parse tree produced by ArcanumParser#multDiv.
    def exitMultDiv(self, ctx:ArcanumParser.MultDivContext):
        pass


    # Enter a parse tree produced by ArcanumParser#booleano.
    def enterBooleano(self, ctx:ArcanumParser.BooleanoContext):
        pass

    # Exit a parse tree produced by ArcanumParser#booleano.
    def exitBooleano(self, ctx:ArcanumParser.BooleanoContext):
        pass


    # Enter a parse tree produced by ArcanumParser#identificador.
    def enterIdentificador(self, ctx:ArcanumParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by ArcanumParser#identificador.
    def exitIdentificador(self, ctx:ArcanumParser.IdentificadorContext):
        pass



del ArcanumParser