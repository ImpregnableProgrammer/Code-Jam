
# Not passing judging on question page, and I do not know why
# Passes the provided sample test cases though
# VERY frustrating

def Signs(S, D):
    C = []
    for i in range(S):
        
        T = 0
        M = None
        N = None
        for d,A,B in D[i:]:
            if d + A == M or not M:
                T += 1
                M = d + A
            elif d - B == N or not N:
                T += 1
                N = d - B
            else:
                break

    #     T2 = 0
    #     M = None
    #     N = None
    #     for d,A,B in D[i:]:
    #         if d - B == N or not N:
    #             T2 += 1
    #             N = d - B
    #         elif d + A == M or not M:
    #             T2 += 1
    #             M = d + A
    #         else:
    #             break
            
    #     C += [max(T, T2)]
    # print(C)
        
    return max(C), C.count(max(C))
        

N = int(input())
for i in range(1, N+1):
    S = int(input())
    D = []
    for j in range(S):
        L = [*map(int,input().split(" "))]
        D += [[L[0],L[1], L[2]]]
    Z = Signs(S, D)
    print("Case #%d:"%i, Z[0], Z[1])
    
    
