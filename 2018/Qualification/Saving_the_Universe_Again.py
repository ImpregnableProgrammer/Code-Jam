
# Passed the first test set quickly
# Unfortunately, takes too long (over 20 seconds) for larger inputs

import re

def Damage(P):
    T = C = 0
    P = ''.join(P)
    Index = re.search("S+", P)
    while Index:
        Match = P[:Index.span()[1]]
        C += Match.count("C")
        T += 2**C*Match.count("S")
        P = P[Index.span()[1]:]
        Index = re.search("S+", P)
    return T
    
def Swaps(D, P):
    NodesV = set()
    Nodes = {tuple(P)}
    Step = 0
    while len(Nodes):
        NodesN = set()
        for Current in Nodes:
            if Damage(Current) <= D:
                return Step
            for i in range(len(Current) - 1):
                New = Current[:i] + (Current[i+1],) + (Current[i],) + Current[i+2:]
                if New not in NodesV and Current[i+1] != Current[i] and not (Current[i] == "S" and Current[i+1] == "C"):
                    NodesN.add(New)
        NodesV.update(Nodes)
        Nodes = NodesN
        Step += 1
    return "IMPOSSIBLE"

Test_Cases = int(input())
for Test in range(1, Test_Cases + 1):
    S = input().split(" ")
    D, P = int(S[0]), S[1]
    print("Case #%d:"%Test,Swaps(D, P))
                
                
