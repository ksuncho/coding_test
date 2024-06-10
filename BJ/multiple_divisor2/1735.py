import sys
def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

# def lcm (a,b):
#     return a*b//gcd(a,b)

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

print((A*D+B*C)//gcd(A*D+B*C, B*D), (B*D)//gcd(A*D+B*C, B*D))
