from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
A = [int(x) for x in sys.stdin.readline().spllit()]
B = [int(x) for x in sys.stdin.readline().spllit()]
M = int(sys.stdin.readline().rstrip())
C = [int(x) for x in sys.stdin.readline().spllit()]
queuestack = deque(B)
cnt=0
for i in C:
    if A[cnt] == 0:
        queuestack.popleft()
        queuestack.append(i)
    else:
        queuestack.append(i)
        cnt +=1