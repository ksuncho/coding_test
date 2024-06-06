N, M = map(int,input().split())
B = [0] * N
for x in range(M):
    i, j, k = map(int,input().split())
    B[i-1:j]=[k]*(j-i+1)
for ball in B:
    print(ball,end=' ')
    