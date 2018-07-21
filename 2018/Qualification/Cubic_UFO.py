
import math

def Centers(A):

    if A > 2**.5:
        Theta = math.atan(2**.5)/2
        for i in range(1000):
            Theta = Theta - (A*2**.5 - 2*math.cos(Theta) - 2**.5*math.sin(Theta)) / (2*math.sin(Theta) - 2**.5*math.cos(Theta))
        print(1/(2**1.5), 1/(2**1.5)*math.cos(Theta) or 0, -1/(2**1.5)*math.sin(Theta) or 0)
        print(1/(2**1.5), -1/(2**1.5)*math.cos(Theta) or 0, 1/(2**1.5)*math.sin(Theta) or 0)
        print(0, 0.5*math.sin(Theta) or 0, 0.5*math.cos(Theta) or 0)
        
    else:
        Theta = math.acos(A/2**.5)
        print(0.5*math.cos(math.pi/4 + Theta) or 0, 0.5*math.sin(math.pi/4 + Theta) or 0, 0)
        print(0.5*math.cos(-math.pi/4 + Theta) or 0, 0.5*math.sin(-math.pi/4 + Theta) or 0, 0)
        print(0, 0, 0.5)

T = int(input())
for i in range(1, T+1):
    F = float(input())
    print("Case #%d:"%i)
    Centers(F)
