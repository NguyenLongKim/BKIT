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

expr: int_expr|float_expr|bool_expr|element_expr|relational_expr|string_type;

int_type
    : ID
    | INTEGER
    | int_of_float
    | int_of_string
    | func_call
    | element_expr;

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
    | float_of_string
    | func_call
    | element_expr;

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
    | element_expr;

bool_expr
    : LP bool_expr RP
    | <assoc=right> NEG bool_expr
    | bool_expr (AND|OR) bool_expr
    | bool_type;

element_expr: (ID|func_call) (LSB (int_expr)+ RSB)+;

string_type
    : ID
    | STRING
    | string_of_bool
    | string_of_float
    | string_of_int
    | func_call
    | read_func
    | element_expr;

int_of_float: INT_OF_FLOAT LP float_expr RP;
float_of_int: FLOAT_OF_INT LP int_expr RP;
int_of_string: INT_OF_STRING LP string_type  RP;
string_of_int: STRING_OF_INT LP int_expr RP;
float_of_string: FLOAT_OF_STRING LP string_type RP;
string_of_float: STRING_OF_FLOAT LP float_expr RP;
bool_of_string: BOOL_OF_STRING LP string_type RP;
string_of_bool: STRING_OF_BOOL LP bool_expr RP;

INT_OF_FLOAT: 'int_of_float';
INT_OF_STRING: 'int_of_string';
FLOAT_OF_INT: 'float_of_int';
FLOAT_OF_STRING: 'float_of_string';
STRING_OF_INT: 'string_of_int';
STRING_OF_FLOAT: 'string_of_float';
STRING_OF_BOOL: 'string_of_bool';
BOOL_OF_STRING: 'bool_of_string';


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

if_stm: IF bool_expr THEN stms_list (ELSEIF bool_expr THEN stms_list)* (ELSE stms_list)? ENDIF DOT;

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

func_call
    : ID LP params_func_call? RP
    | type_coercion_func
    | built_in_func;
params_func_call: (expr)(','expr)* ;

built_in_func
    : print_func
    | printLn_func
    | printStrLn_func
    | read_func;

printLn_func: PRINTLN LP RP;
print_func:  PRINT LP string_type RP;
printStrLn_func: PRINTSTRLN LP string_type RP;
read_func: READ LP RP; 

PRINTLN: 'printLn';
PRINT: 'print';
PRINTSTRLN: 'printStrLn';
READ: 'read';

/*****************
Lexer Declaration 
*****************/

/* Seperators */
SEMI: ';'; 
COMMA: ',';
COLON: ':';
DOT: '.';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket

/* Identifier*/
ID: [a-z][a-zA-Z'_'0-9]* ;

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

FLOAT: [0-9]+'.'(([0-9]+[Ee]('+'|'-')?[0-9]+)|([0-9]+)|([Ee]('+'|'-')?[0-9]+))*;

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