import sys
N, M = map(int,sys.stdin.readline().split())
# List runtime 3724ms
# S = []
# for _ in range(N):
#     S.append(sys.stdin.readline())
# Set runtime 116ms
S = set()
for _ in range(N):
    S.add(sys.stdin.readline())
inv = []
count = 0
for _ in range(M):
    inp = sys.stdin.readline()
    if inp in S:
        count +=1
print(count)