import sys
N, M = map(int, sys.stdin.readline().split())
notheard = set()
notseen = set()
for _ in range(N):
    notheard.add(sys.stdin.readline().rstrip())
for _ in range(M): 
    notseen.add(sys.stdin.readline().rstrip())
A = list(notheard.intersection(notseen))
A.sort()
print(len(A))
for name in A:
    print(name)
