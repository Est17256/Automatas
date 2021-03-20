from Def_Sup import *
"""
Function to convert list to string or string to list
"""
def read_AFD(chn, sub,infin):
    i = 0
    frt = infin[0][0]
    for n in chn:
        x = move(frt, n, sub)
        if len(x)==0:
            return False
        x = list(x)
        frt = x[0]
    i = 0 
    for n in range(len(infin)):
        if frt == infin[n][1]:
            i += 1
    if i !=0:
        return True
    else:
        return False