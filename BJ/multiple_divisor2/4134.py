import sys
T = int(sys.stdin.readline())
def check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i==0:
            return False
    return True
    
for _ in range(T):
    N = int(sys.stdin.readline())
    while True:
        if N == 0 or N == 1:
            print(2)
            break
        if check(N):
            print(N)
            break
        else:
            N+=1
