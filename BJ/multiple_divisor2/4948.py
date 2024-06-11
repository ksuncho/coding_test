import sys
array = [1]*(123456*2+1)
for i in range(1,123456*2+1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if  i % j == 0:
            array[i] = 0
            break

while True:
    n = int(sys.stdin.readline().rstrip())
    count=0
    if n == 0:
        break
    prime = 0
    for i in range(n+1,2*n+1):  
        prime+=array[i]
    print(prime)