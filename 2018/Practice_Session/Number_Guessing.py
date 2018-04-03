Test_Cases = int(input())
for i in range(Test_Cases):
    a, b = map(int, input().split(" "))
    n = int(input())
    print(a + (b - a) // 2, flush = True)
    s = input()
    while s != "CORRECT":
        if s == "TOO_SMALL":
            a = a + (b - a) // 2
        elif s == "TOO_BIG":
            b = b - (b - a) // 2
        elif s == "WRONG_ANSWER":
            exit(-1)
        print(a + (b - a) // 2, flush = True)
        s = input()
