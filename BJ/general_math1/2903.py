N = int(input())
def pibo(x):
    if x == 0:
        return 2
    else:
        return 2*pibo(x-1)-1
    
print(pibo(N)**2)