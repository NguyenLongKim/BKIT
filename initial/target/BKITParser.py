# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'.'", "'('", "')'", 
                     "<INVALID>", "'Body'", "'Else'", "'EndFor'", "'If'", 
                     "'Var'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", 
                     "'Parameter'", "'While'", "'Continue'", "'EndBody'", 
                     "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", "'Function'", 
                     "'Then'", "'False'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'>'", "'<'", "'<='", "'>='", 
                     "'=/='", "'>.'", "'<.'", "'<=.'", "'>=.'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "SEMI", "COMMA", "COLON", "DOT", "LP", 
                      "RP", "ID", "BODY", "ELSE", "ENDFOR", "IF", "VAR", 
                      "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
                      "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", 
                      "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "ADD", 
                      "ADDDOT", "SUB", "SUBDOT", "MUL", "MULDOT", "DIV", 
                      "DIVDOT", "MOD", "NEG", "AND", "OR", "EQ", "NEI", 
                      "GT", "LT", "LTE", "GTE", "NEF", "GTDOT", "LTDOT", 
                      "LTEDOT", "GTEDOT", "SEPERATOR", "LITERAL", "INTEGER", 
                      "FLOAT", "BOOLEAN", "STRING", "ARRAY", "WS", "NEW_LINE", 
                      "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    SEMI=1
    COMMA=2
    COLON=3
    DOT=4
    LP=5
    RP=6
    ID=7
    BODY=8
    ELSE=9
    ENDFOR=10
    IF=11
    VAR=12
    ENDDO=13
    BREAK=14
    ELSEIF=15
    ENDWHILE=16
    PARAMETER=17
    WHILE=18
    CONTINUE=19
    ENDBODY=20
    FOR=21
    RETURN=22
    TRUE=23
    DO=24
    ENDIF=25
    FUNCTION=26
    THEN=27
    FALSE=28
    ADD=29
    ADDDOT=30
    SUB=31
    SUBDOT=32
    MUL=33
    MULDOT=34
    DIV=35
    DIVDOT=36
    MOD=37
    NEG=38
    AND=39
    OR=40
    EQ=41
    NEI=42
    GT=43
    LT=44
    LTE=45
    GTE=46
    NEF=47
    GTDOT=48
    LTDOT=49
    LTEDOT=50
    GTEDOT=51
    SEPERATOR=52
    LITERAL=53
    INTEGER=54
    FLOAT=55
    BOOLEAN=56
    STRING=57
    ARRAY=58
    WS=59
    NEW_LINE=60
    BLOCK_COMMENT=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    UNTERMINATED_COMMENT=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





