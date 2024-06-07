N, K = map(int, input().split())
factor = [x for x in range(1,N+1) if (N%x == 0)]

if len(factor) < K:
    print(0)
else:
    factor.sort()
    print(factor[K-1])