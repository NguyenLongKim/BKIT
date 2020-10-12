# Generated from e:\Principle of Programming Language\assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\33")
        buf.write("\n\2\r\2\16\2\34\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\6")
        buf.write("\6(\n\6\r\6\16\6)\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\7\b")
        buf.write("\64\n\b\f\b\16\b\67\13\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\3\2\4\3\2c|\5\2\13\13\16\17\"\"\2E")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\32\3\2\2\2\5\36\3\2")
        buf.write("\2\2\7 \3\2\2\2\t\"\3\2\2\2\13\'\3\2\2\2\r-\3\2\2\2\17")
        buf.write("/\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27A\3\2")
        buf.write("\2\2\31\33\t\2\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3")
        buf.write("\2\2\2\34\35\3\2\2\2\35\4\3\2\2\2\36\37\7=\2\2\37\6\3")
        buf.write("\2\2\2 !\7<\2\2!\b\3\2\2\2\"#\7X\2\2#$\7c\2\2$%\7t\2\2")
        buf.write("%\n\3\2\2\2&(\t\3\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2")
        buf.write(")*\3\2\2\2*+\3\2\2\2+,\b\6\2\2,\f\3\2\2\2-.\7\f\2\2.\16")
        buf.write("\3\2\2\2/\60\7$\2\2\60\61\7$\2\2\61\65\3\2\2\2\62\64\13")
        buf.write("\2\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66")
        buf.write("\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\7$\2\29:\7$\2\2:")
        buf.write("\20\3\2\2\2;<\13\2\2\2<\22\3\2\2\2=>\13\2\2\2>\24\3\2")
        buf.write("\2\2?@\13\2\2\2@\26\3\2\2\2AB\13\2\2\2B\30\3\2\2\2\6\2")
        buf.write("\34)\65\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    NL = 6
    CM = 7
    ERROR_CHAR = 8
    UNCLOSE_STRING = 9
    ILLEGAL_ESCAPE = 10
    UNTERMINATED_COMMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "WS", "NL", "CM", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "WS", "NL", "CM", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


