
import itertools

def V(R, B, C, A):
    #Groups = {i for i in itertools.product(*[range(B+1)]*R) if sum(i)==B and all(o <= max(A, key=lambda h:h[0])[0] for o in i)}
    Times = []
    #print(Groups)
    for Group in Groups:
        S = []
        P = []
        #print(Group)
        for i in Group:
            if i:
                T = []
                q = 0
                for j in A:
                    if i <= j[0] and q not in P:
                        T += [(j[1]*i + j[2], q)]
                    q += 1
                #print("T", T)
                if len(T):
                    Z = min(T, key=lambda f:f[0])
                    S += [Z[0]]
                    P += [Z[1]]
                    #print("P",P)
        if S:
            #print("S",S)
            Times += [max(S)]
        #print("Times",Times)
    return min(Times)
        
T = int(input())
for i in range(1, T+1):
    R,B,C = map(int,input().split(" "))
    A = []
    for l in range(C):
        A += [tuple(map(int, input().split(" ")))]
    print("Case #%d:"%i,V(R, B, C, A))


        
            
    
    
