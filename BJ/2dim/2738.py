N, M = map(int,input().split())
A = []
for i in range(N*2):
    A.append([int(x) for x in input().split()])
for i in range(N):
    for j in range(M):
        print(A[i][j]+A[N+i][j],end=' ')
    print('')