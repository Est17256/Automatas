from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

"""
Function to make the graf of AFN
"""
def GrafAFN(thsm, infin):
    f = Digraph('Graf', filename='./AFN.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')
    f.node("")
    for i in range(len(infin)):
        f.edge("",str(infin[i][0]))
    f.attr('node', shape='doublecircle')
    for i in range(len(infin)):
        f.node(str(infin[i][1]))
        print(infin[i][1])
    f.attr('node', shape='circle')
    for i in range(len(thsm)):
        f.edge(str(thsm[i][0]), str(thsm[i][2]), label= str(thsm[i][1]))
    f.attr('node', shape='none')
    f.view()
"""
Function to make the graf of AFN-AFD
"""
def GrafAFN_AFD(sub, infin):
    f = Digraph('Graf', filename='./AFD.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')
    f.node("")
    for i in range(len(infin)):
        f.edge("",str(infin[i][0]))
    f.attr('node', shape='doublecircle')
    for i in range(len(infin)):
        f.node(str(infin[i][1]))
        print(infin[i][1])
    f.attr('node', shape='circle')
    for i in range(len(sub)):
        f.edge(str(sub[i][0]), str(sub[i][2]), label= str(sub[i][1]))
    f.attr('node', shape='none')
    f.view()