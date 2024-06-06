N, M = map(int,input().split())
B = [x+1 for x in range(N)]
for k in range(M):
    i, j = map(int,input().split())
    tmp = B[j-1]
    B[j-1] = B[i-1]
    B[i-1] = tmp
for ball in B:
    print(ball,end=' ')
