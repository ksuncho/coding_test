N = 5
slist = [0] * N
for _ in range(N-2):
    i = int(input())
    slist[i-1] = 1
for x in range(N):
    if slist[x] == 0:
        print(x+1)