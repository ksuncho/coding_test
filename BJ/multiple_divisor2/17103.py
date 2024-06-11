#                  0 1 2 3 4 5 6 7 8 9 
# 4: 1 3          [1,1,1,0]
# 6: 1 5          [1,1,1,0,1,0]
# 8: 1 7, 3 5     [1,1,1,0,1,0,1,0]
# 10: 3 7         [1,1,1,0,1,0,1,0,0,0]
# 12: 1 11, 5 7   [1,1,1,0,1,0,1,0,0,0,1,0]

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
