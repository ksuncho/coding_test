from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
A = [int(x) for x in sys.stdin.readline().split()]
B = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline().rstrip())
C = [int(x) for x in sys.stdin.readline().split()]
X = deque()

for i, xi in enumerate(B):
    if A[i]==0:
        X.append(xi)

for i in C:
    X.insert(0,i)
    print(X.pop(),end=' ')


    