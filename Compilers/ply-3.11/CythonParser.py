#PENDIENTES
# Ignorar comentario
# acceder a nodos


import ply.yacc as yacc

 # Get the token map from the lexer.  This is required.
from CythonLexer import tokens

precedence = (
    ('nonassoc', 'LESS_THAN', 'MORE_THAN','LESS_EQUAL','MORE_EQUAL'),
    ('right' ,'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE','MODULE'),
    ('left', 'POWER'),
    ('left','EQUALS' ,'NOT_EQUAL'),
    ('right','ASSIGN'),
    ('left','AND'),
    ('left','OR'),
    ('right','MINUS_ASSIGN','PLUS_ASSIGN','ASSIGN_MODULE','DIVIDE_ASSIGN','TIMES_ASSIGN'),
    ('left','COMA'),

)

#single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE




#file_input: (NEWLINE | stmt)* ENDMARKER

def p_file_input(p):
        '''
            file_input : stmt file_inputhelp


        '''

        p[0] = p[1] , p[2]

def p_file_inputhelp(p):
        '''
            file_inputhelp : file_input
                        | empty
        '''

        p[0]= p[1]
#-------------------------------------------- START Statements ----------------------------------------------#

#stmt: simple_stmt | compound_stmt
def p_stmt(p):
    '''
        stmt : simple_stmt
            | compound_stmt



    '''
    p[0] = p[1]




#simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE ??

def p_simple_stmt(p):
    '''

        simple_stmt : small_stmt simplehelper



    '''

    p[0]=p[1] , p[2]


def p_simplehelper(p):
    '''
        simplehelper : NEWLINE small_stmt simplehelper
                    | empty

    '''

    if p[1] == "NEWLINE":
        p[0] = NEWLINE , p[1] , p[2]
    else:
        p[0] = p[1]


#small_stmt: expr_stmt

def p_small_stmt(p):
    '''
        small_stmt : expr_stmt
                    | print_stmt
                    | input_stmt
    '''

    p[0]=p[1]

def p_print_stmt(p):
    '''
        print_stmt : PRINT LPAREN test RPAREN


    '''

    p[0] = p[1],(p[3])

def p_input_stmt(p):
    '''
        input_stmt : test ASSIGN INPUT LPAREN STRING RPAREN

    '''
    p[0] = p[1] = p[3],(p[5])



#expr_stmt: testlist_star_expr (annassign | augassign (yield_expr|testlist) |('=' (yield_expr|testlist_star_expr))*)

def p_expr_stmt(p):
    '''
        expr_stmt : typotest
                    | augassign
                    | annassign

    '''
    p[0] = p[1]

def p_typotest(p):

    '''
        typotest : CDEF vartypes

    '''
    p[0] = p[1], p[2]



#-------------------------------------------- END Statements ----------------------------------------------#

#-------------------------------------------- START VARTYPES ----------------------------------------------#

def p_vartypes(p):
    '''
        vartypes : INT test ASSIGN test
                | DOUBLE test ASSIGN test
                | SHORT test ASSIGN test
                | LONG test ASSIGN test
                | CHAR test ASSIGN test
                | FLOAT test ASSIGN test


    '''

    p[0] = p[1] ,p[2], p[3],p[4]

#-------------------------------------------- END VARTYPES ----------------------------------------------#


#-------------------------------------------- START Assignments ----------------------------------------------#


#annassign: ':' test ['=' test]
def p_annasign(p):
    '''
        annassign : test ASSIGN test

    '''

    p[0] = p[1],p[2],p[3]

#augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' |
            #'<<=' | '>>=' | '**=' | '//=')

def p_augassign(p):
    '''

        augassign : test PLUS_ASSIGN test
                | test MINUS_ASSIGN test
                | test TIMES_ASSIGN test
                | test DIVIDE_ASSIGN test
                | test ASSIGN_MODULE test


    '''

    p[0] = p[1],p[2],p[3]



#-------------------------------------------- END Assignments ----------------------------------------------#

#-------------------------------------------- START IF EXPRESSION ----------------------------------------------#
#if_stmt: 'if' test ':' suite ('elif' test ':' suite)* ['else' ':' suite]
#ESTO NO DEBE IR AQUI SI HAY ERROR TRATA DE CAMBIARLO A SU POSICION DONDE DEBE DE ESTAR
#compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt | with_stmt | funcdef | classdef | decorated | async_stmt
def p_compound_stmt(p):
    '''
        compound_stmt : if_stmnt
                    | for_stmt
                    | break_stmt


    '''

    p[0] = p[1]


def p_break_stmt(p):
    '''
        break_stmt : BREAK
    '''
    p[0] = p[1]

def p_if_stmnt(p):
    '''
        if_stmnt : IF test THEN suite NEWLINE
                | compound_if

    '''

    if p[1] == "IF" :
        p[0] = p[1],p[2],p[3],p[4] ,NEWLINE
    else:
        p[0] = p[1]

def p_compound_if (p):
    '''
    compound_if : IF test THEN itersuite elif_stmnt else_stmnt
                    | IF test THEN itersuite if_stmnt else_stmnt

    '''

    if p[1] == "if" :
        p[0] = p[1],p[2],p[3],p[4],p[5],p[6]
    else:
        p[0]=p[1]

def p_itersuite(p):
    '''
        itersuite : suite itersuite
                | suite elif_stmnt

    '''

    p[0] = p[1],p[2]


def p_else_stmnt(p):
    '''
        else_stmnt : ELSE THEN suite
                    | ELSE THEN if_stmnt
                    | empty

    '''

    if p[1] == "else":
        p[0] = p[1],p[2],p[3]
    else:
        p[0]=p[1]

def p_elif(p):
    '''
        elif_stmnt : ELIF test THEN suite elif_stmnt
                    | else_stmnt

    '''

    if p[1] == "ELIF":
        p[0] = p[1] , p[2],p[3],p[4],p[5]
    else:
        p[0] = p[1]

#-------------------------------------------- END IF EXPRESSION ----------------------------------------------#
#-------------------------------------------- Start FOR EXPRESSION ----------------------------------------------#
#for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]

def p_for_stmt(p):
    '''
        for_stmt : FOR exprlist IN testlist THEN stmt
                | FOR exprlist IN RANGE  THEN stmt


    '''

    p[0] = p[1],p[2],p[3],p[4],p[5],p[6]


#exprlist: (expr|star_expr) (',' (expr|star_expr))* [',']
def p_exprlist(p):
    '''
        exprlist : expression exprlisthelper


    '''

    p[0] = p[1],p[2]

def p_exprlisthelper(p):

    '''
        exprlisthelper : NEWLINE expression exprlisthelper
                        | empty

    '''

    if p[1] == "NEWLINE" :
        p[0]= p[1],p[2],p[3]
    else:
        p[0]= p[1]


#testlist: test (',' test)* [',']
def p_testlist(p):
    '''

        testlist : test testlisthelper
    '''
    p[0]=p[1],p[2]

def p_testlisthelper(p):

    '''
        testlisthelper : NEWLINE test exprlisthelper
                        | empty

    '''

    if p[1] == "NEWLINE" :
        p[0]= p[1],p[2],p[3]
    else:
        p[0]= p[1]



#-------------------------------------------- END FOR EXPRESSION ----------------------------------------------#
#-------------------------------------------- START Suite ----------------------------------------------#
#EXPR es XOR IGNORALO


#ESTOY TRATANDO DE ITERAR SUITE Y NO JALA
#suite: simple_stmt | NEWLINE INDENT stmt+ DEDENT


def p_suite(p):
    '''
        suite : simple_stmt
                | NEWLINE INDENT stmt

    '''
    if p[1] == "NEWLINE" :
        p[0]= p[1],p[2],p[3]
    else:
        p[0]= p[1]




#-------------------------------------------- END Suite ----------------------------------------------#




#-------------------------------------------- START Tests ----------------------------------------------#

#test: or_test ['if' or_test 'else' test] | lambdef
def p_test(p):
    '''
        test : or_test


    '''

    p[0] = p[1]


#or_test: and_test ('or' and_test)*

def p_or_test(p):
    '''
        or_test : and_test or_comp

    '''
    p[0] = p[1],p[2]

def p_or_comp(p):
    '''
        or_comp : OR and_test or_comp
                | empty

    '''

    if p[1] == "or" :
        p[0]= p[1],p[2],p[3]
    else:
        p[0]= p[1]

#and_test: not_test ('and' not_test)*
def p_and_test(p):
    '''
        and_test : not_test and_comp

    '''

    p[0]=p[1]

def p_and_comp(p):
    '''
        and_comp : AND not_test and_comp
                | empty

    '''

    if p[1] == "AND" :
        p[0]= p[1],p[2],p[3]
    else:
        p[0]= p[1]

#not_test: 'not' not_test | comparison
def p_not_test(p):
    '''
        not_test : NOT not_test
                | comparison

    '''

    if p[1] == "NOT" :
        p[0]= p[1],p[2]
    else:
        p[0]= p[1]
#-------------------------------------------- END Tests ----------------------------------------------#



#-------------------------------------------- START COMPARISON ----------------------------------------------#
#comparison: expr (comp_op expr)*
def p_comparison(p):
    '''
        comparison :  expression comphelper

    '''
    p[0] = p[1],p[2]

def p_comparisonhelper(p):
    '''

        comphelper :  comp_op expression comphelper
                    | empty

    '''




def p_comp_op(p):
    '''
        comp_op : LESS_THAN
                | MORE_THAN
                | EQUALS
                | MORE_EQUAL
                | LESS_EQUAL
                | NOT_EQUAL
                | IN
                | NOT_IN
                | IS
                | IS_NOT

    '''
    p[0] = p[1]
    #
    #

#-------------------------------------------- END COMPARISON ----------------------------------------------#



#-------------------------------------------- LINK FROM comparison to Arythmetic ----------------------------------------------#

def p_Expression(p):
    '''
        expression : arith_expr

    '''

    p[0] = p[1]

#--------------------------------------------START ARYTHMETIC EXPRESSIONS ----------------------------------------------#
#arith_expr: term (('+'|'-') term)*
def p_Arythmetic_expressions(p):
    '''
        arith_expr : term PLUS arith_expr
                    | term MINUS arith_expr
                    | term empty


    '''

    if p[2] == "+":
        p[0]=p[1]+p[3]
    elif p[2]=="-":
        p[0]=p[1]-p[3]
    else:
        p[0]=p[1]








#term: factor (('*'|'@'|'/'|'%'|'//') factor)*

def p_Term(p):
    '''
        term : factor TIMES  term
            | factor DIVIDE  term
            | factor MODULE  term
            | factor empty

    '''

    if p[2] == "*":
        p[0]=p[1]*p[3]
    elif p[2] == "/":
        p[0]=p[1]/p[3]
    elif p[2] == "%":
        p[0]=p[1]%p[3]
    else:
        p[0]=p[1]




#factor: ('+'|'-'|'~') factor | power
def p_factor(p):
    '''
        factor :  LPAREN MINUS factor RPAREN
                | power

    '''

    if p[1] == "(":
        p[0] = p[1],p[2],p[3],p[4]
    else:
        p[0]= p[1]



#power: atom_expr ['**' factor]
def p_power(p):
    '''
        power : factor POWER factor
                | atom_expr empty


    '''

    if p[2] == "**":
        p[0] = p[1]**p[3]
    else:
        p[0] = p[1]





#--------------------------------------------END ARYTHMETIC EXPRESSIONS ----------------------------------------------#
#--------------------------------------------Start Atom ----------------------------------------------#

def p_atom_expr(p):
    '''
        atom_expr : atom
    '''
    p[0]=p[1]

def p_atom(p):
    '''
        atom : ID
            | NUMBER
            | STRING
            | BOOL_TRUE
            | BOOL_FALSE
            | NONE


    '''

    p[0]=p[1]

#--------------------------------------------End Atom ----------------------------------------------#







#--------------------------------------------PENDIENTES ----------------------------------------------#

#testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )
#atom_expr: ['await'] atom trailer*
#trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
#arglist: argument (',' argument)*  [',']
#argument: ( test [comp_for] |
            #test '=' test |
            #'**' test |
            #'*' test )


#atom: ('(' [yield_expr|testlist_comp] ')' |
#       '[' [testlist_comp] ']' |
#       '{' [dictorsetmaker] '}' |
#       NAME | NUMBER | STRING+ | '...' | 'None' | 'True' | 'False')
#power: atom_expr ['**' factor]




#Empty production
def p_empty(p):
     'empty :'
     pass


 # Error rule for syntax errors
def p_error(p):
    p.lexer.lineno += p.value.count('\n+')
    line=p.lexer.lineno
    print("Syntax error in input!")
    print("In line :%i" % line)

#
# # Tests
#
#
# def test0():
#     file= open ("testParse.pyx","r")
#     return file
#
# def test1():
#     file = open("comment_test.pyx","r")
#     return file
#
# def test2():
#     file = open("Nested_Structures.pyx","r")
#     return file
#
# def test3():
#     file= open ("Variables_Constants.pyx","r")
#     return file
#
# def test4():
#     file= open ("datatypes.pyx","r")
#     return file
#
#
# def test5():
#     file= open ("loops_condition.pyx","r")
#     return file
#
#
# def test6():
#     file= open ("input_output.pyx","r")
#     return file
#
#
# def test7():
#     file= open ("strings.pyx","r")
#     return file
#
#
# def test8():
#     file= open ("everything.pyx","r")
#     return file
#
# def test9():
#     file= open ("loop_error.pyx","r")
#     return file
#
# def test10():
#     file= open ("variable_error.pyx","r")
#     return file
#
# def test11():
#     file= open ("place_error.pyx","r")
#     return file
#
# def test12():
#     file=open("New_Cases.pyx","r")
#
#
#
#
# def choice(userInput):
#     switcher={
#     0:test0(),
#     1:test1(),
#     2:test2(),
#     3:test3(),
#     4:test4(),
#     5:test5(),
#     6:test6(),
#     7:test7(),
#     8:test8(),
#     9:test9(),
#     10:test10(),
#     11:test11(),
#     12:test12(),
#     }
#
#     userchoice = switcher.get(userInput)
#     return userchoice
#
#
#
#
#
# active = True
#
# while(active):
#     print("Test cases:\n")
#     print("0. Test Parse: \n")
#     print("1. Word Comments: \n")
#     print("2. NestedStructures: \n")
#     print("3. Variables and Constants: \n")
#     print("4. DataTypes: \n")
#     print("5. Lopps_condition: \n")
#     print("6. Input_Output: \n")
#     print("7. Strings: \n")
#     print("8. Everything together: \n")
#     print("9. Loop Error: \n")
#     print("10. Variable Error: \n")
#     print("11. Place Error: \n")
#     print("12. NEW_CASES: \n")
#     print("13. Quit: \n")
#
#
#
#     userInput=input("Give me the test case: ")
#
#     intInput=int(userInput)
#
#     if(intInput==13):
#
#         active = False
#
#         print("Goodbye")
#
#     else:
#
#         prepdata=choice(intInput)
#
#         parser = yacc.yacc()
#         while True:
#             data=prepdata.read()
#             if data == '':# EOF
#                 print("Parsed")
#                 break
#             result=parser.parse(data)
#             print(result)
#
#  # Build the parser
#
#
# #file = open("testParse.pyx")
#
#
#
yacc.yacc(debug=1)







    #print(result)
