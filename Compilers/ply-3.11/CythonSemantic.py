from CythonParser import *
from CythonLexer import *
import sys


def Semantic(text):

    tokent = []
    symbolTable = []
    lex.input(text)
    while True:
        tok = lex.token()
        if not tok:
            break
        if tok.type == "ERROR":
            return "Syntax Error"
        token = [tok.type, tok.value]
        tokent.append(token)
    elements = {}
    scope = 0
    code = ""
    aux = ""
    while len(tokent) > 0:
        #print(tokent[0][1])
        elements = {}

        #PRINT
        if tokent[0][0] == 'PRINT':
            aux += ("  "*scope)+ "print"
            tokent.pop(0)
            while tokent[0][0] != 'RPAREN':#NEWLINE
                #agregar sintaxis extra(valor)

                aux += tokent[0][1]
                tokent.pop(0)
            tokent.pop(0)
            aux += ') \n'
            print("Termine con print")
            code += aux
            aux = ''

        #CDEF
        elif tokent[0][0]== 'CDEF':
            tokent.pop(0)
        elif tokent[0][0] == 'INT' or tokent[0][0] ==  'DOUBLE' or tokent [0][0]=='CHAR':

            if sameVariableName(symbolTable,tokent[1][1], scope):
                print("Error two declarations of the same variable")
                sys.exit()

            elements['type'] = tokent[0][0]

            print(tokent[0][0])
            tokent.pop(0)
            elements['name'] = tokent[0][1]
            print(tokent[0][1])

            aux += tokent[0][1]
            tokent.pop(0)

            elements['value'] = None
            #scope for scope level
            elements['level'] = scope

            print("Sali tabla de asignacion")
            if tokent[0][0] == 'PLUS_ASSIGN' or tokent[0][0] == 'MINUS_ASSIGN' or tokent[0][0] =='DIVIDE_ASSIGN' or tokent[0][0] =='TIMES_ASSIGN':
                print("Entre op  assign")
                print("ERROR, asignment error: "+tokent[0][1])
                sys.exit()
            if tokent[0][0] == 'ASSIGN':
                print("Entre op simple")
                print(tokent[0][1])
                aux += " = "
                tokent.pop(0)
                #input
                if tokent[0][0] == 'INPUT' and tokent[0][1] =='input':
                    aux+=("  "*scope)+ "input"
                    tokent.pop(0)
                    while tokent[0][1] != ')':
                        aux += tokent[0][1]
                        tokent.pop(0)

                    aux += ")"
                    code+= ("  "*scope)+aux
                    aux= ""


                #asignacion a id

                elif tokent[0][0] == 'ID':
                    print("Entre a asignacion de id")
                    temp = getValue(symbolTable, tokent[0][1], scope)

                    if temp == None:
                        print ("Variable not defined"+tokent[0][1])

                    elif  is_int(temp) and elements['type'] == 'INT':
                        elements['value'] = temp
                        aux += str(tokent[0][1])
                        tokent.pop(0)
                        sys.exit()
                    elif  is_float(temp) and elements['type'] == 'DOUBLE':
                        elements['value'] = temp
                        aux += str(tokent[0][1])
                        tokent.pop(0)

                    elif temp and elements['type'] == 'BOOL_TRUE':
                        elements['value'] = temp
                        aux += str(tokent[0][1])
                        tokent.pop(0)

                    elif  temp and elements['type'] == 'CHAR':
                        elements['value'] = temp
                        aux += tokent[0][1]
                        tokent.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                        sys.exit()
                elif  is_float(tokent[0][1]) and elements['type'] == 'DOUBLE':
                    print("Entre a float assignment")
                    print(tokent[0][1])
                    elements['value'] = tokent[0][1]
                    aux += str(tokent[0][1])
                    tokent.pop(0)

                elif  is_int(tokent[0][1]) and elements['type'] == 'INT':
                    print("Entre a int assignment")
                    print(tokent[0][1])
                    elements['value'] = tokent[0][1]
                    aux += str(tokent[0][1])
                    tokent.pop(0)


                elif  (tokent[0][1]) and elements['type'] == 'CHAR':
                    elements['value'] = tokent[0][1]
                    aux += tokent[0][1]
                    tokent.pop(0)
                else:
                    print("ERROR No same type")
                    print("Variable ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                    sys.exit()
                # if tokent[0][1] == ';':
                #     symbolTable.append(elements)
                #     tokent.pop(0)
                #     code += ("  ")*scope+aux+"\n"
                #     aux = ""
                # else:
                    # print("entro ahi")

                while tokent[0][1] != ')':
                    print (tokent[0][1])
                    if tokent[0][1] == '+' or tokent[0][1] == '-' or tokent[0][1] == '*'or tokent[0][1] == '/' or tokent[0][1] == '%':

                        aux += " "+tokent[0][1]+" "

                        print(aux)
                        tokent.pop(0)

                    if tokent[0][0] == 'ID':
                        temp = getValue(symbolTable, tokent[0][1], scope)
                        if temp == None:
                            print ("Variable "+tokent[0][1]+" not define")
                            sys.exit()

                        elif  is_int(temp) and elements['type'] == 'INT':
                            elements['value'] = temp
                            aux += tokent[0][1]
                            tokent.pop(0)

                        elif  is_int(temp) and elements['type'] == 'SHORT':
                            elements['value'] = temp
                            aux += tokent[0][1]
                            tokent.pop(0)

                        elif  is_float(temp) and elements['type'] == 'DOUBLE':
                            elements['value'] = temp
                            aux += tokent[0][1]
                            tokent.pop(0)

                        elif  temp and elements['type'] == 'CHAR':
                            elements['value'] = temp
                            aux += tokent[0][1]
                            tokent.pop(0)
                        else:
                            print("ERROR No same type")
                            print("Variable ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                            sys.exit()
                    elif  is_float(tokent[0][1]) and elements['type'] == 'DOUBLE':
                        elements['value'] = tokent[0][1]
                        aux += tokent[0][1]
                        tokent.pop(0)
                    elif  is_int(tokent[0][1]) and elements['type'] == 'INT':
                        print("Entre a int de suma")
                        elements['value'] = tokent[0][1]

                        aux +=str(tokent[0][1])
                        tokent.pop(0)
                    elif  (tokent[0][1]) and elements['type'] == 'CHAR':
                        elements['value'] = tokent[0][1]
                        aux += str(tokent[0][1])
                        tokent.pop(0)
                    else:
                        print("ERROR No same type")
                        print("Variable ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                        sys.exit()
                if tokent[0][1] == ')':
                    symbolTable.append(elements)
                    tokent.pop(0)
                    code += ("  ")*scope+aux+"\n"
                    aux = ""
            else:
                symbolTable.append(elements)
                tokent.pop(0)
                code += ("  ")*scope+aux+" = None\n"
                aux = ""

        elif tokent[0][0] == 'ID':
            temp = getElement(symbolTable, tokent[0][1], scope)

            aux = tokent[0][1]

            if temp == None:
                print("ERROR Variable not defined:", tokent[0][1])
                sys.exit()
            tokent.pop(0)
            if (tokent[0][0] == 'PLUS_ASSIGN' or tokent[0][0] == 'MINUS_ASSIGN' or tokent[0][0] =='TIMES_ASSIGN' or tokent[0][0] =='DIVIDE_ASSIGN')or tokent[0][0]=='ASSIGN':
                aux += " "+ tokent[0][1] +" "
                tokent.pop(0)
                #input
                if tokent[0][0] == 'INPUT' and tokent[0][1] =='input':
                    aux+=("  "*scope)+ "input"
                    tokent.pop(0)
                    while tokent[0][1] != ')':
                        aux += tokent[0][1]
                        tokent.pop(0)
                    aux += ")"
                    code+= ("  "*scope)+aux
                    aux= ""

                elif tokent[0][0] == 'ID':
                    temp2 = getValue(symbolTable, tokent[0][1], scope)

                    if temp2 == None:
                        print("ERROR Variable not defined:", tokent[0][1])
                        sys.exit()
                    elif  is_int(temp2) and temp['type'] == 'INT':
                        temp['value'] = temp2
                        aux += str(tokent[0][1])
                        tokent.pop(0)
                    elif  is_int(temp2) and temp['type'] == 'SHORT':
                        temp['value'] = temp2
                        aux += str(tokent[0][1])
                        tokent.pop(0)

                    elif  is_float(temp2) and temp['type'] == 'DOUBLE':
                        temp['value'] = temp2
                        aux += str(tokent[0][1])
                        tokent.pop(0)

                    elif  temp2 and temp['type'] == 'CHAR':
                        temp['value'] = temp2
                        aux += tokent[0][1]
                        tokent.pop(0)
                    else:
                        print("ERROR:")
                        print("Variable: ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                        sys.exit()
                elif  is_float(tokent[0][1]) and temp['type'] == 'DOUBLE':
                    temp['value'] = tokent[0][1]
                    aux += str(tokent[0][1])
                    tokent.pop(0)
                elif  is_int(tokent[0][1]) and temp['type'] == 'INT':
                    print("entre a id int")
                    temp['value'] = tokent[0][1]
                    aux += str(tokent[0][1])
                    tokent.pop(0)
                elif  (tokent[0][1]) and temp['type'] == 'CHAR':
                    temp['value'] = tokent[0][1]
                    aux += tokent[0][1]
                    tokent.pop(0)
                else:
                    print("ERROR:")
                    print("Variable ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                    sys.exit()
                while tokent[0][1] != ')':
                    if tokent[0][1] == '+' or tokent[0][1] == '-' or tokent[0][1] == '*'or tokent[0][1] == '/' or tokent[0][1] == '%':
                        aux += " "+tokent[0][1]+" "
                        tokent.pop(0)
                    if tokent[0][0] == 'ID':
                        temp2 = getValue(symbolTable, tokent[0][1], scope)
                        if temp2 == None:
                            print ("Variable "+tokent[0][1]+" not define")
                            sys.exit()
                        if  is_float(temp2) and temp['type'] == 'DOUBLE':
                            temp['value'] = temp2
                            aux += str(tokent[0][1])
                            tokent.pop(0)
                        elif  is_int(temp2) and temp['type'] == 'INT':
                            temp['value'] = temp2
                            aux += str(tokent[0][1])
                            tokent.pop(0)
                        elif  temp2 and temp['type'] == 'CHAR':
                            temp['value'] = temp2
                            aux += tokent[0][1]
                            tokent.pop(0)
                        else:
                            print("ERROR No same type")
                            sys.exit()
                    elif  is_float(tokent[0][1]) and temp['type'] == 'DOUBLE':
                        temp['value'] = tokent[0][1]
                        aux += str(tokent[0][1])
                        tokent.pop(0)
                    elif  is_int(tokent[0][1]) and temp['type'] == 'INT':
                        temp['value'] = tokent[0][1]
                        aux += str(tokent[0][1])
                        tokent.pop(0)
                    elif  (tokent[0][1]) and temp['type'] == 'CHAR':
                        temp['value'] = tokent[0][1]
                        aux += tokent[0][1]
                        tokent.pop(0)
                    else:
                        print("ERROR")
                        print("Variable ",temp['name']," is not of the same type as: ",tokent[0][1],"that has type of:",tokent[0][0])
                        sys.exit()
                if tokent[0][1] == ')':
                    #symbolTable.append(elements)
                    setElement(symbolTable, temp)
                    tokent.pop(0)
                    code += ("  ")*scope+aux+"\n"
                    aux = ""

                    #####IF
        elif tokent[0][0] == "IF" :
            aux+='if'

            tokent.pop(0)
            while tokent[0][0] != "THEN":

                if tokent[0][0] == 'ID':
                    temp=getValue(symbolTable,tokent[0][1],scope)
                    if temp == None:
                        print ("ERROR:Variable "+tokent[0][1]+" not defined")
                        sys.exit()
                    else:

                        print(tokent[0][1])
                        aux+=" "+tokent[0][1]+ " "
                        tokent.pop(0)

                elif tokent[0][0]=='LESS_THAN' or tokent[0][0]== 'MORE_THAN' or tokent[0][0]=="EQUALS" or tokent[0][0]=="LESS_EQUAL" or tokent[0][0]=="MORE_EQUAL":
                    print(tokent[0][1])
                    aux+=" "+tokent[0][1]+ " "
                    tokent.pop(0)

                elif tokent[0][0] == "AND" or tokent [0][0]=="OR":
                    print(tokent[0][1])
                    aux+=" "+tokent[0][1]+ " "
                    tokent.pop(0)

            if tokent[0][1] == ":":
                tokent.pop(0)
                aux+=":"
                code+=("  ")*scope+aux+"\n"
                aux=""
                scope+=1

        #uso esto para poder cerrar ciclo de if y elif y for
        elif tokent[0][1]=="]":
            scope-=1
            tokent.pop(0)

        elif tokent[0][1]=="else":

            aux+=tokent[0][1]+":"
            code+=("  ")*scope+aux+"\n"
            aux=""
            scope+=1

            tokent.pop(0)
            tokent.pop(0)

        ####ELIF#######
        elif tokent[0][0] == "ELIF" :
            aux+='elif'

            tokent.pop(0)
            while tokent[0][0] != "THEN":

                if tokent[0][0] == 'ID':
                    temp=getValue(symbolTable,tokent[0][1],scope)
                    if temp == None:
                        print ("ERROR:Variable "+tokent[0][1]+" not defined")
                        sys.exit()
                    else:

                        print(tokent[0][1])
                        aux+=" "+tokent[0][1]+ " "
                        tokent.pop(0)

                elif tokent[0][0]=='LESS_THAN' or tokent[0][0]== 'MORE_THAN' or tokent[0][0]=="EQUALS" or tokent[0][0]=="LESS_EQUAL" or tokent[0][0]=="MORE_EQUAL":
                    print(tokent[0][1])
                    aux+=" "+tokent[0][1]+ " "
                    tokent.pop(0)

                elif tokent[0][0] == "AND" or tokent [0][0]=="OR":
                    print(tokent[0][1])
                    aux+=" "+tokent[0][1]+ " "
                    tokent.pop(0)

            if tokent[0][1] == ":":
                tokent.pop(0)
                aux+=":"
                code+=("  ")*scope+aux+"\n"
                aux=""
                scope+=1

        ######### ciclo for

        elif tokent[0][1]=="for":
            aux += 'for'
            tokent.pop(0)

            while tokent[0][0]!="THEN":
                aux+=" " + tokent[0][1]+" "
                tokent.pop(0)


            if tokent[0][1]==":":
                tokent.pop(0)
                aux+=":"
                code+=("  ")*scope+aux+"\n"
                aux=""
                scope+=1


    print(symbolTable)
    return code





def sameVariableName(symbolTable, name, scope):
    for element in symbolTable:
        if element['name'] == name:
            if element['level']== scope:
                return True
    return False

def getValue(symbolTable, name, scope):
    a = None
    cont = 0
    for element in symbolTable:
        if element['name'] == name:
            if element['level'] == scope:
                return element['value']
            elif element['level'] < scope and cont < scope:
                cont = scope
                a = element['value']
    return a

def getElement(symbolTable, name, scope):
    a = None
    cont = 0
    for element in symbolTable:
        if element['name'] == name:
            if element['level'] == scope:
                return element
            elif element['level'] < scope and cont < scope:
                cont = scope
                a = element

    return a

def setElement(symbolTable, temp):
    for element in symbolTable:
        if element['name'] == temp['name'] and element['level'] == temp['level']:
            element = temp


def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def is_int(value):
  try:
    float(value)
    return float(value).is_integer()
  except ValueError:
    return False
