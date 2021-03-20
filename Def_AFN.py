from Def_Pross import *
from operator import itemgetter
"""
Function that make the thomson construction with the postfix
"""
def AFN(posF):
    n = 2
    i = 0
    infin = []
    temp = []
    while i < len(posF):
        #Make Klee
        if posF[i] == "*":
            fst = infin[-1][0]
            lst = infin[-1][1]
            x1 = [n, "e", fst]
            y1 = [lst, "e", fst]
            fst = n
            n +=1
            x2 = [lst, "e", n]
            y2 = [fst, "e", n]
            lst = n
            x3 = temp[-1]
            temp.pop()
            temp.append([x3,x1,y1,x2,y2])
            infin.pop()
            infin.append([fst, lst])
            n += 1
        #Make the OR
        elif posF[i] == "|":
            x = temp[-1]
            temp.pop()
            y = temp[-1]
            temp.pop()
            temp.append([x,y, [n,"e", infin[-2][0]],[n,"e",infin[-1][0]],[infin[-2][1],"e",n+1],[infin[-1][1],"e",n+1]])
            fst = n
            lst = n +1
            n +=2
            infin.pop()
            infin.pop()
            infin.append([fst,lst])
        #Make Concatenation
        elif posF[i] == ".":
            x = temp[-1]
            temp.pop()
            y = temp[-1]
            temp.pop()
            temp3 = infin[-1]
            infin.pop()
            temp2 = infin[-1]
            infin.pop()
            try:
                 y = clean(y, [])
                 for a in range(len(y)):
                     for n in range(0,3):
                         if y[a][n] == temp2[1]:
                             y[a][n] = temp3[0]       
            except:
                for a in range(len(y)):
                    if y[a] == temp2[1]:
                        y[a] = temp3[0]
            infin.append([temp2[0], temp3[1]])
            temp.append([y, x])
        elif posF[i] != "." and posF[i] != "|" and posF[i] != "*" :
            temp.append([n, posF[i], n+1])
            infin.append([n, n +1])
            n +=2
        i+=1
    thsm = sorted(clean(temp,[]), key= itemgetter(0))
    return thsm, infin