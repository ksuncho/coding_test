import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
lst = list(map(int,sys.stdin.readline().split()))
ballon = deque(lst)

# for i in range(N):
#     x=ballon[0]
#     print(lst.index(x)+1,end=' ')
#     ballon.rotate(-x)
#     ballon.remove(x)

for i in range(N):
    x=ballon.popleft()
    print(lst.index(x)+1,end=' ')
    ballon.rotate(-x+1)
    print(ballon)
 
    