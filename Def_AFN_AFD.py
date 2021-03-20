from Def_Sup import *
"""
Function that convert the thomson results to subsets for AFD
"""
def dfa_nfa(thsm, infin):
    infin2 =[]
    infin3 = []
    states =[]
    subs = []
    nodeV =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    states.append(eclosure(infin[0][0], thsm))
    infin2.append(eclosure(infin[0][0], thsm))
    vals = []
    #Verify the symbols
    for i in range(len(thsm)):
        if thsm[i][1] != "e":
            if thsm[i][1] not in vals:
                vals.append(thsm[i][1])    
    i=0
    while i < len(states):
        for n in vals:
            temp1 = eclosure(move(states[i],n,thsm),thsm)
            subs.append([states[i],n,temp1])
            for j in infin:
                if j[1] in temp1:
                    infin2.append(temp1)
            if temp1 not in states and temp1 is not None:
                states.append(temp1)         
        i+=1
    i = 0
    while i < len(subs):
        if subs[i][0] == set() or subs[i][2] == set():
            subs.pop(i)
            i-=1
            
        i +=1
    i = 0 
    while i < len(subs):
        temp = states.index(subs[i][0])
        subs[i][0] = nodeV[temp]
        temp = states.index(subs[i][2])
        subs[i][2] = nodeV[temp]
        i +=1
    i = 0
    #Define the initial state and final state
    while i < len(infin2):
        temp = states.index(infin2[i])
        infin2[i]= nodeV[temp]
        i+=1
    for n in range(1,len(infin2)):
        infin3.append([infin2[0],infin2[n]])
    return subs, infin3