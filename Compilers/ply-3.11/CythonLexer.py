#Andres Quiroz
#Cython Lexer
#ignorar comentarios


import ply.lex as lex

#RESERVED WORDS
reserved = {
    'for':'FOR',
    'True' : 'BOOL_TRUE',
    'False' : 'BOOL_FALSE',
    'and' : 'AND',
    'or' : 'OR',
    'return':'RETURN',
    'if' : 'IF',
    'else' : 'ELSE',
    'elif' : 'ELIF',
    'cdef' : 'CDEF',
    'int' : 'INT',
    'double' : 'DOUBLE',
    'short' : 'SHORT',
    'long' : 'LONG',
    'char': 'CHAR',
    'float':'FLOAT',
    'def' : 'DEF',
    'list' : 'LIST',
    'in' : 'IN',
    'not in' : 'NOT_IN',
    'is' : 'IS',
    'is not': 'IS_NOT',
    'not' : 'NOT',
    'range' : 'RANGE',
    'none' : 'NONE',
    'print':'PRINT',
    'input' : 'INPUT',
    'break':'BREAK',


 }

# TOKENS
tokens = [
'ASSIGN',
'EQUALS',
'MORE_THAN',
'LESS_THAN',
'LESS_EQUAL',
'MORE_EQUAL',
'NOT_EQUAL',
'PLUS_ASSIGN',
'PLUS',
'MINUS_ASSIGN',
'MINUS',

'TIMES_ASSIGN',
'TIMES',
'DIVIDE_ASSIGN',
'DIVIDE',
'ASSIGN_MODULE',
'MODULE',
'POWER',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'ARRAY',
'LCORCHETE',
'RCORCHETE',
'COMMENT_LINE',
'FLOAT_NUMBER',
'NUMBER',
'ID',
'THEN',
'STRING',
'APOSTROPHE',
'DOUBLEAPOSTROPHE',
'COMA',
'DOT',
'NEWLINE',
'INDENT',
]+list(reserved.values())

# Regular expression for simple tokens that are not reserved words
t_EQUALS = r'\=='
t_NOT_EQUAL=r'\!='
t_ASSIGN = r'\='
t_MORE_EQUAL = r'\>='
t_LESS_EQUAL = r'\<='
t_MORE_THAN = r'\>'
t_LESS_THAN = r'\<'
t_PLUS_ASSIGN=r'\+='
t_MINUS_ASSIGN=r'-='
t_DIVIDE_ASSIGN=r'/='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES_ASSIGN = r'\*='
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN_MODULE=r'\%='
t_MODULE = r'\%'
t_POWER= r'\*\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET= r'\['
t_RBRACKET= r'\]'
t_LCORCHETE= r'\{'
t_RCORCHETE= r'\}'

t_THEN=r'\:'
t_COMMENT_LINE= r'\"\"\".*\n+\"\"\"'
t_DOUBLEAPOSTROPHE=r'\"'
t_APOSTROPHE=r'\''
t_COMA=r'\,'
t_DOT=r'\.'
t_INDENT=r'\t'






# SPACES AND TAB
t_ignore  = r' ' or r'\#.*'

# REGULAR EXPRESSIONS complex tokens
def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

'''def t_NEGATIVE_FLOAT_NUMBER(t):
    r'\-\d+\.\d+'
    t.value = float(t.value)
    return t'''

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_STRING(t):
    r'\'\w.+\'|\"\w.+\"'
    t.value = str(t.value)
    return t

def t_ID(t):
     r'\w+'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t


# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# PANIC ERROR
def t_error(t):
    t.lexer.lineno += t.value.count('\n+')
    line=t.lexer.lineno
    print("Illegal character '%s'" % t.value[0])
    print("In line :%i" % line)
    exit()

# Create LEXER
lexer = lex.lex()



# Tests
'''

def test0():
    file= open ("comment_line.pyx","r")
    return file


def test1():
    file = open("comment_test.pyx","r")
    return file

def test2():
    file = open("variables.pyx","r")
    return file

def test3():
    file= open ("strings.pyx","r")
    return file

def test4():
    file= open ("datatypes.pyx","r")
    return file


def test5():
    file= open ("loops_condition.pyx","r")
    return file


def test6():
    file= open ("input_output.pyx","r")
    return file


def test7():
    file= open ("everything.pyx","r")
    return file

def test8():
    file= open ("loop_error.pyx","r")
    return file

def test9():
    file= open ("variable_error.pyx","r")
    return file

def test10():
    file= open ("place_error.pyx","r")
    return file






def choice(userInput):
    switcher={
    0:test0(),
    1:test1(),
    2:test2(),
    3:test3(),
    4:test4(),
    5:test5(),
    6:test6(),
    7:test7(),
    8:test8(),
    9:test9(),
    10:test10(),
    }

    userchoice = switcher.get(userInput)
    return userchoice





active = True

while(active):
    print("Test cases:\n")
    print("0. Line Comments: \n")
    print("1. Word Comments: \n")
    print("2. Variables: \n")
    print("3. Strings: \n")
    print("4. DataTypes: \n")
    print("5. Lopps_condition: \n")
    print("6. Input_Output: \n")
    print("7. Everything together: \n")
    print("8. Loop Error: \n")
    print("9. Variable Error: \n")
    print("10. Place Error: \n")
    print("11. Quit: \n")


    userInput=input("Give me the test case: ")

    intInput=int(userInput)

    if(intInput==11):

        active = False

        print("Goodbye")

    else:

        prepdata=choice(intInput)
        data=prepdata.read()
        '''
data='''3+5/7'''
        # Give the lexer some input(data)
lexer.input(data)
'''
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
    '''
