import sys
T = int(sys.stdin.readline().rstrip())
prime=[]
check = [1] * 1000001
check[0] = 0
check[1] = 0

for i in range(2,1000001):
    if check[i] == 1:
        prime.append(check[i])
        for j in range(i*2, 1000001, i):
            check[j]=0

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for j in range(2, n//2+1):
        if check[j] and check[n-j] :
            count +=1            
    print(count)
