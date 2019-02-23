import math
import sys

def quadratic(a,b,c):
    delta = b^2 - 4*a*c
    if delta < 0:
        print('mou gai')
        sys.exit(0)
    else:
    
        x1 = (-b + math.sqrt(b^2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b^2 - 4*a*c))/(2*a)
    return x1,x2

a = int(input('a =' ))
b = int(input('b =' ))
c = int(input('c =' ))
x = quadratic(a,b,c)
print(x)

