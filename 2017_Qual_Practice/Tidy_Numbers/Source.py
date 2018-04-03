
# CORECT!

# Purely mathematical approach; No string manipulations!
def Tidy_Numbers(n):
    i=0
    while(n // 10**(i+1) > 0):
        n = (n // 10**(i+2))*10**(i+2) + ((n // 10**(i+1) - 1) % 10)*10**(i+1) + (10**(i+1) - 1) if (n // 10**i) % 10 < (n // 10**(i+1)) % 10 else n
        i += 1
    return n

Input = open("Large.txt")
Test_Cases = int(Input.readline())
for i in range(1, Test_Cases + 1):
    print("Case #%d:"%i, Tidy_Numbers(int(Input.readline())))
