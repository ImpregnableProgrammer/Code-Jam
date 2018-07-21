
def TroubleSortCheck(N):
    Done = False
    while not Done:
        Done = True
        for i in range(len(N)-2):
            if N[i] > N[i+2]:
                N = N[:i] + N[i:i+3][::-1] + N[i+3:]
                Done = False
    if sorted(N) == N:
        return "OK"
    else:
        for i in range(len(N)-1):
            if N[i] > N[i+1]:
                return i

T = int(input())
for i in range(1, T+1):
    C = int(input())
    N = list(map(int, input().split(" ")))
    print("Case #%d:"%i,TroubleSortCheck(N))
