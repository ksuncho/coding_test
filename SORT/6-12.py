N, K = map(int,input().split())
A = [x for x in list(map(int,input().split()))]
B = [x for x in list(map(int,input().split()))]
A = sorted(A)
B = sorted(B,reverse=True)
for i in range(K):
    if(A[i]<B[i]):
        A[i],B[i]=B[i],A[i]
print(sum(A))