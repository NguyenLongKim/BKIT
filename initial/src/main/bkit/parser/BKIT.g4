//1812742
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

/*****************
Parser Declaration 
*****************/
program: (var_declare)*(func_declare)* ;

var_declare: VAR COLON vars_list SEMI;
vars_list: (scalar_var|composite_var)(','(scalar_var|composite_var))*;
scalar_var: ID('='literal)?;
literal: INTEGER|FLOAT|STRING|TRUE|FALSE;
composite_var: ID dimension+ ('='ARRAY)?;
dimension: '['INTEGER']';

func_declare: FUNCTION COLON ID (PARAMETER COLON params_list)? BODY COLON stms_list ENDBODY DOT;
params_list: (ID|ID dimension+)(','(ID|ID dimension+))*;
stms_list: (var_delcare_stm)*(asm_stm|break_stm|call_stm|coninue_stm|do_while_stm|for_stm|if_stm|while_stm|return_stm)*;

expr: int_expr|float_expr|bool_expr|element_expr|relational_expr;

int_type
    : ID
    | INTEGER
    | int_of_float
    | int_of_string
    | func_call
    | int_expr;

int_expr
    : LP int_expr RP
    | <assoc=right> (ADD|SUB) int_expr
    | int_expr MOD int_expr
    | int_expr (MUL|DIV) int_expr
    | int_expr (ADD|SUB) int_expr
    | int_type;

float_type
    : ID
    | FLOAT
    | float_of_int
    | float_of_int
    | func_call
    | float_expr;

float_expr
    : LP float_expr RP
    | <assoc=right> (ADDDOT|SUBDOT) float_expr
    | float_expr (MULDOT|DIVDOT) float_expr
    | float_expr (ADDDOT|SUBDOT) float_expr
    | float_type;

relational_expr
    : int_expr (EQ|NEI|LT|GT|LTE|GTE) int_expr
    | float_expr (NEF|LTDOT|GTDOT|LTEDOT|GTEDOT) float_expr;

bool_type
    : ID
    | TRUE
    | FALSE
    | bool_of_string
    | func_call
    | relational_expr
    | bool_expr;

bool_expr
    : LP bool_expr RP
    | <assoc=right> NEG bool_expr
    | bool_expr (AND|OR) bool_expr
    | bool_type;

element_expr: (ID|func_call) index_operators ;

index_operators
    : '[' int_expr ']' (index_operators)*;

string_type
    : ID
    | STRING
    | string_of_bool
    | string_of_float
    | string_of_int
    | func_call;

int_of_float: 'int_of_float' LP (float_type) RP;
float_of_int: 'float_of_int' LP (int_type) RP;
int_of_string: 'int_of_string' LP (string_type) RP;
string_of_int: 'string_of_int' LP (int_type) RP;
float_of_string: 'float_of_string' LP (string_type) RP;
string_of_float: 'string_of_float' LP (float_type) RP;
bool_of_string: 'bool_of_string' LP (string_type) RP;
string_of_bool: 'string_of_bool' LP (bool_type) RP;

type_coercion_func
    : int_of_float
    | float_of_int
    | int_of_string
    | string_of_int
    | float_of_string
    | string_of_float
    | bool_of_string
    | string_of_bool;

var_delcare_stm: var_declare ;

asm_stm: ID '=' expr SEMI;

if_stm: IF bool_expr THEN stms_list (ELSEIF bool_expr THEN stms_list)* (ELSE stms_list)? ENDIF DOT ;

for_stm: FOR LP scalar_var '=' initExpr COMMA conditionExpr COMMA updateExpr RP DO stms_list ENDFOR;
initExpr: int_expr;
conditionExpr: bool_expr ;
updateExpr: int_expr|float_expr;

while_stm: WHILE bool_expr DO stms_list ENDWHILE;

do_while_stm: DO stms_list WHILE bool_expr ENDDO;

break_stm: BREAK SEMI;

coninue_stm: CONTINUE SEMI;

call_stm: func_call SEMI ;

return_stm: RETURN expr SEMI ;

func_call: ID LP params_func_call? RP;
params_func_call: (expr)(','expr)* ;

printLn_func: 'printLn' LP RP;
print_func: 'print' LP (string_type) RP;
printStrLn_func: 'printStrLn' LP (string_type) RP;
read_func: 'read' LP RP; 

/*****************
Lexer Declaration 
*****************/

/* Seperators */
SEMI: ';'; 
COMMA: ',';
COLON: ':';
DOT: '.';
LP: '(';
RP: ')';

/* Identifier*/
ID: [a-z]+[A-Za-z'_'0-9]* ;

/* Keywords */
BODY: 'Body';
ELSE: 'Else';
ENDFOR: 'EndFor';
IF: 'If';
VAR: 'Var';
ENDDO: 'EndDo';
BREAK: 'Break';
ELSEIF: 'ElseIf';
ENDWHILE: 'EndWhile';
PARAMETER: 'Parameter';
WHILE: 'While';
CONTINUE: 'Continue';
ENDBODY: 'EndBody';
FOR: 'For';
RETURN: 'Return';
TRUE: 'True';
DO: 'Do';
ENDIF: 'EndIf';
FUNCTION: 'Function';
THEN: 'Then';
FALSE: 'False';

/* Operators */
ADD: '+';
ADDDOT: '+.';
SUB: '-';
SUBDOT: '-.';
MUL: '*';
MULDOT: '*.';
DIV: '\\';
DIVDOT: '\\.';
MOD: '%';
NEG: '!';
AND: '&&';
OR: '||';
EQ: '==';
NEI: '!=';
GT : '>' ;
LT : '<' ;
LTE: '<=';
GTE: '>=';
NEF: '=/=';
GTDOT : '>.' ;
LTDOT : '<.' ;
LTEDOT: '<=.';
GTEDOT: '>=.';

/* Literals */
INTEGER: '0'|[1-9]+[0-9]*|('0x'|'0X')[0-9A-F]*|('0o'|'0O')[0-7]*;

FLOAT: [0-9]+'.'(([0-9]+[Ee]('+'|'-')?[0-9]+)|([0-9]+)|([Ee]('+'|'-')?[0-9]+)) ;

fragment STR_CHAR: ~[\b\f\r\n\t"'\\] | ESC_SEQ | '\'"';
fragment ESC_SEQ: '\\'[bftnr'\\] ;
STRING: '"' STR_CHAR* '"'
    {
        y = str(self.text)
        self.text = y[1:-1]
    };

ARRAY
    : '{'(|INTEGER(','INTEGER)*)'}'
    | '{'(|FLOAT(','FLOAT)*)'}'
    | '{'(|(TRUE|FALSE)(','(TRUE|FALSE))*)'}'
    | '{'(|STRING(','STRING)*)'}' 
    | '{'(|ARRAY(','ARRAY)*)'}' ;

WS : [ \t\r\f\n]+ -> skip ; // skip spaces

BLOCK_COMMENT: '**'.*?'**' -> skip; // block comment

ERROR_CHAR: .
	{
		raise ErrorToken(str(self.text))
	};

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		raise UncloseString(y[1:])
	};

fragment ESC_ILLEGAL: '\\'~[btnfr'\\];
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};


UNTERMINATED_COMMENT: '**' (~[*])*('*'|('*'(~[*])+)*) EOF 
    {
        raise UnterminatedComment()
    };