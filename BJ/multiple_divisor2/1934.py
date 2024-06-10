import sys
T = int(sys.stdin.readline())
#my answer1 -> runtime error (ValueError)
# i = 1
# for _ in range(T):
#     A, B = map(int, sys.stdin.readline().split())
#     x = max(A,B)
#     y = min(A,B)
#     amul = []
#     bmul = []
#     while True:
#         if i*x > A*B:
#             break
#         else:
#             amul.append(i*x)
#             i+=1
#     for a in amul:
#         if a%y==0:
#             bmul.append(a)
#     print(min(bmul))
# answer2 runtime error(NameError)
def gcd (a,b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm (a,b):
    return a * b // gcd(a,b)

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(lcm(A,B))




        
        
