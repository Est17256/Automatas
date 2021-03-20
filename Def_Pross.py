from Def_Sup import *

"""
Function that preparing the expression and adding the concatenation symbol before posfix.
convert a+ to aa* and a? to (a|e)
"""
def processing(expression):
    temp = []
    temp2 = []
    for n in expression:
        if n != "?" and n != "+":
            temp.append(n)
        if n == "?" or n == "+":
            #Enter if (a)+ or (a)?
            if (n == "?" and temp[-1] != ")") or (n == "+" and temp[-1] != ")"):
                bol = True
                t = len(temp)-1
                while bol == True and t != -1:
                    if temp[t] == ")" or temp[t] == ".":
                        temp.pop()
                        bol = False
                    else:
                        temp2.append(temp[t])
                        temp.pop()
                    t-=1
                if n == "?":
                    temp.append(str("("+lst_str(temp2[::-1],0)+"|e)"))
                elif n == "+":
                    temp.append(")")
                    temp.append(str("("+lst_str(temp2[0],0)+").("+lst_str(temp2[0],0)+"*)"))
                temp2 = []
            #Enter if a+ or a?
            else: 
                t = len(temp)-1
                bol = True
                while bol == True:
                    if temp[t] == "(" :
                        temp2.append("(")
                        temp.pop()
                        bol = False
                    else:
                        temp2.append(temp[t])
                        temp.pop()
                    t-=1
                if n == "?":
                    temp.append(str("("+lst_str(temp2[::-1],0)+"|e)"))
                elif n == "+":
                    temp.append(str("("+lst_str(temp2[::-1],0)+"*)."+lst_str(temp2[::-1],0)))
                temp2 = []
    #Add the concatenation symbol
    temp3=[]
    for i in range(len(temp)):
        temp3.append(temp[i])
        try:
            if temp[i+1]!="|" and temp[i+1]!="*" and temp[i+1]!=")" and temp[i]!="(" and temp[i+1]!=" " and temp[i]!="|":
                temp3.append(".")
        except:
            a=0
    #Fix if the first pos is a . or if pos 0 is a expression and the first pos is .
    i = 0
    expresionN = lst_str(temp3,0)
    if expresionN[0] == ".":
        expresionN.pop(0)
    elif expresionN[0][0]==".":
        a=list(expresionN[0])
        a.pop(0)
        b="".join(a)
        expresionN.pop(0)
        expresionN.insert(0,b)
    return lst_str(expresionN,1)
"""
Function that convert the ready expression to postfix
Search through the () ​​to find the operators and values
"""
def postfix(expression):
    temp = []
    oprs = []
    i = 0
    #Search in the expression ( to add the operators
    while i < len(expression):
        if expression[i] == "(":
            temp.append(expression[i])
        elif expression[i] == ")":
            x = len(temp) - 1
            while temp[x] != "(":
                oprs.append(temp[x])
                temp.pop()
                x -= 1
            temp.pop()
        #append in order of precedence
        elif expression[i] =="|" or expression[i] =="*" or expression[i] ==".":
            if len(temp) == 0:
                temp.append(expression[i])
            else:
                if temp[-1] != '(':
                    if precedence(expression[i]) < precedence(temp[-1]):
                        x = len(temp) - 1
                        if x != 0:
                            while temp[x] != '(':
                                oprs.append(temp[-1])
                                temp.pop()
                                x -= 1
                            temp.append(expression[i])
                        else:
                            oprs.append(temp[-1])
                            temp.pop()
                            temp.append(expression[i])
                    elif precedence(expression[i]) >= precedence(temp[-1]):
                        temp.append(expression[i])
                else:
                    temp.append(expression[i])
        else:
            oprs.append(expression[i])
        i += 1
    #Clean the remains
    if len(temp) != 0:
        for i in range(len(temp)):
            oprs.append(temp[-1])
            temp.pop()
    return oprs