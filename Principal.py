from Def_Pross import *
from Def_AFN_AFD import *
from Def_AFN import *
from Def_Graf import *
from Def_Cads import *
flag=True
while flag==True:
    print("Welcome")
    print("1)AFN")
    print("2)AFN-AFD")
    print("3)AFD")
    print("4)Salir")
    opc=input("Enter the option: ")
    if opc=="1":
        ver=False
        while ver==False:
            expresion=input("Enter the expresion: ")
            if verify(expresion)==True:
                ver=True
            else:
                print("Please verify the expression")
        pros=processing(expresion)
        pos= postfix(pros)  
        thsm, infin = AFN(pos)
        GrafAFN(thsm, infin)
    elif opc=="2":
        ver=False
        while ver==False:
            expresion=input("Enter the expresion: ")
            if verify(expresion)==True:
                ver=True
            else:
                print("Please verify the expression")
        ingreso = postfix(processing(expresion))
        print(ingreso) 
        thsm, infin = AFN(ingreso)
        sub, infin = dfa_nfa(thsm, infin)
        GrafAFN_AFD(sub, infin)
        mensaje1 = input("Enter the chain to verify: ")
        mensaje2 = input("Enter the chain to verify: ")
        if  read_AFD(mensaje1, sub, infin) ==True:
            print("OK")
        else:
            print("BAD") 
        if  read_AFD(mensaje2, sub, infin) ==True:
            print("OK")
        else:
            print("BAD") 
    elif opc=="3":
        print("En Desarrollo")
    elif opc=="4":
        flag=False
    else:
        print("Try another option ")