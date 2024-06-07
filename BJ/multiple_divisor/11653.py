N = int(input())
factor = [x for x in range(1,N+1) if N%x == 0]
prime = []
for i in factor:
    x = [x for x in range(1,i+1) if i%x == 0]    
    if x == [1,i]:
        prime.append(i)
cnt=0
while True:
    if (N == 1) or (cnt > len(prime)):
        break
    elif (N%prime[cnt])==0:
        N = N/prime[cnt]
        print(prime[cnt])       
    else:
        cnt+=1