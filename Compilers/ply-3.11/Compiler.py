from CythonSemantic import *
import ply.yacc as yacc

data1 = '''

        a="Andres"




'''
data2 = '''
        cdef int v =0)
        cdef int b =0)
        if v<b:
            cdef int a =0)
        ]
        a=10
        b=10+"Andres"





'''

#RUN
print("################################")
print("########Test Case 1#############:")
print("################################")
try:
    yacc.parse(data1)
    try:
        code = Semantic(data1)
        e = open("GeneratedCode.py", "w+")
        e.write(code)
        e.close()
        print("Compilation complete, run the generated file with python 3")
    except:
        pass
except:
    pass

print("################################")
print("########Test Case 2#############:")
print("################################")
try:
    yacc.parse(data2)
    try:
        code = Semantic(data2)
        e = open("GeneratedCode1.py", "w+")
        e.write(code)
        e.close()
        print("Compilation complete, run the generated file with python 3")
    except:
        pass
except:
    pass
