
import sys

def Strategize(iO, jO, i, j):
    #print(iO, jO, i, j, file=sys.stderr)
    
    Done = True
    for x in range(iO-1, iO+2):
        for y in range(jO-1, jO+2):
            if (x,y) not in Prepped:
                Done = False
                
    if not Done:
        return iO, jO
    else:
        return iO, jO+3
    
    # if i - iO < 0:
    #     if j - jO < 0:
    #         return i, j+1
    #     elif j - jO > 0:
    #         return i+1, j
    #     else:
    #         return i, j+1
    # elif i - iO > 0:
    #     if j - jO < 0:
    #         return i-1, j
    #     elif j - jO > 0:
    #         return i, j-1
    #     else:
    #         return i, j-1
    # else:
    #     if j - jO < 0:
    #         return i-1, j
    #     elif j - jO > 0:
    #         return i+1, j
    #     else:
    #         return i, j

T = int(input())
for i in range(T):
    A = int(input())
    Prepped = set()
    iO, jO, i, j = 500, 500, 1, 1
    while i > 0 and j > 0:
        print(iO, jO, flush = True)
        S = input().split(" ")
        i, j = int(S[0]), int(S[1])
        Prepped.add((i,j))
        iO, jO = Strategize(iO, jO, i, j)
    if i < 0:
        exit(-1)
