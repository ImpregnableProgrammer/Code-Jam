
def Rounding(N, L, C):
    
    
    

N=int(input())
for i in range(1, N+1):
    N, L = map(int, input().split(" "))
    C = map(int, input().split(" "))
    print("Case #%d:"%i, Rounding(N, L, C))
