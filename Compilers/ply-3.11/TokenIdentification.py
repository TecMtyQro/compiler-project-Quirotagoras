# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'LIST',
'IF',
'ELSE',
'WHILE',
'ELIF',
'FOR',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LIST = r'list'
t_IF =  r'if'
t_ELSE = r'else'
t_ELIF = r'elif'
t_WHILE = r'while'
t_FOR = r'for'


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer with rules prevoiosly given
lexer = lex.lex()

# Test it out with data
data = '''
3 + 4 * 10 +
- 20 *2
'''

# Give the lexer some input(data)
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)