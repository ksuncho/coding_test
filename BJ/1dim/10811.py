N, M = map(int,input().split())
B = [x+1 for x in range(N)]
for _ in range(M):
    i, j = map(int,input().split())
    B = B[0:i-1]+list(reversed(B[i-1:j]))+B[j:N]
    #B[i-1:j] = bsub
    #print(bsub)
for ball in B:
    print(ball,end=' ')