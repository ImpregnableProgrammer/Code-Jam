

def Word(N, L, Words):
    Indices = [0]*L
    Limit = [N-1]*L
    while Indices != Limit:
        Word = ""
        for j in range(L):
            Word += Words[Indices[j]][j]
        Carry = 1
        for j in range(L-1, -1, -1):
            Add = Indices[j] + Carry
            Carry = 1 if Add >= N else 0
            Indices[j] = Add % N
        if Word not in Words:
            return Word
    return "-"
        
        

T = int(input())
for i in range(1, T+1):
    N, L = [*map(int, input().split(" "))]
    Words = []
    for j in range(N):
        Words += [input()]
    print("Case #%d:"%i, Word(N, L, Words))
