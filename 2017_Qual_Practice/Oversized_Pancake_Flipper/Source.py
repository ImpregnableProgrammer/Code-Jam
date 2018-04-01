
# Simple breadth first search
# Works for small input
# MUCH TOO SLOW FOR LARGE INPUT
def Pancake_Flip(s, c):
    Old = []
    Current = [s]
    Count = 0
    while len(Current):
        New = []
        for i in Current:
            if i.count('+') == len(i):
                return Count
            for z in range(len(i) - c + 1):
                String = i[:z] + i[z:z + c].replace('+', '#').replace('-', '+').replace('#', '-') + i[z + c:]
                New += [String] if String not in Old else []
        Old += Current
        Current = list(set(New))
        Count += 1
    return "IMPOSSIBLE"

Input = open("Small.txt")
Test_Cases = int(Input.readline())
for i in range(Test_Cases):
    L = Input.readline()
    print("Case #%d:"%(i+1), Pancake_Flip(L.split()[0], int(L.split()[-1])))
