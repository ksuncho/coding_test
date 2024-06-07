M = int(input())
N = int(input())
prime = []
for i in range(M,N+1):
    factor = [x for x in range(1,i+1) if i%x==0]
    if factor == [1,i]:
        prime.append(i)
if len(prime)==0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
