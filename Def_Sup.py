"""
Function to measure the value of precedence
"""
def precedence(opr):
    if opr == "(":
        return 3
    elif opr == '*':
        return 3
    elif opr == '|':
        return 2
    elif opr == ".":
        return 1
    else:
        return 0
"""
Function to convert list to string or string to list
"""
def lst_str(val,opc):
    if opc==0:
        temp = ''
        for i in range(0, len(val)):
            temp = temp + str(val[i])
        return temp
    elif opc==1:
        i = 0
        temp = []
        while i< len(val):
            temp.append(val[i])
            i+= 1
        return temp

"""
Function that clean the "()" for concatenation and compact in "[]"
"""
def clean(y, c):
    temp = []
    for i in y:
        if isinstance(i, list):
            clean(i, c)
        else:
            c.append(i)
    for i in range(0,len(c),3):
        if i != len(c):
            temp.append([c[i],c[i+1],c[i+2]])
    return temp
"""
Function that calc the moves of the chain
"""
def movesP(nodes,chn, sub):
    moves = []
    for n in sub:
        if n[0] == nodes and n[1] == str(chn):
            moves.append(n) 
    return moves
"""
Function that move the part of the chain for a expression
"""
def move(nodes, chn, sub):
    nodes = list(nodes)
    moves = []
    if isinstance(nodes, list):
        for i in range(len(nodes)):
            move = movesP(nodes[i], chn, sub)
            for j in move:
                if j[2] not in moves:
                    moves.append(j[2])
        it = set()
        for item in moves:
            it.add(item)
        return it
    else:
        move = movesP(nodes, chn, sub)
        for x in move:
            if x[2] not in moves:
                moves.append(x[2])      
        it = set()
        for item in moves:
            it.add(item)
        return it
""" 
Function that see if the expression is correct
"""
def verify(a):
    temp=[]
    for i in a:
        temp.append(i)
    temp2=0
    temp3=0
    for i in temp:
        if i=="(":
            temp2+=1
        if i==")":
            temp3+=1
    if temp2==temp3:
        return True
    else:
        return False
"""
Function that says the moves with epsilon
"""
def eclosure(x, sub):
    if isinstance(x, int):
        nodes = []
        nodes.append(x)
    else: 
        nodes = list(x)
    if isinstance(nodes, list):
        for n in nodes:
            move = movesP(n, "e", sub)
            for x in move:
                if x[2] not in nodes:
                    nodes.append(x[2])
    it = set()
    for item in nodes:
        it.add(item)
    return it