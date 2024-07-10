import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
# lst = list(map(int,sys.stdin.readline().split()))
# ballon = deque(lst)
# ballon_idx = deque([i for i in range(1,N+1)])

# for i in range(N):
#     x=ballon.popleft()
#     y=ballon_idx.popleft()
#     print(y,end=' ')
#     if x > 0:
#         ballon.rotate(-x+1)
#         ballon_idx.rotate(-x+1)
#     else:
#         ballon.rotate(-x)
#         ballon_idx.rotate(-x)
ballon = deque(enumerate(map(int,sys.stdin.readline().split())))
while ballon:
    i, x = ballon.popleft()
    print(i+1,end=' ')
    if x > 0:
        ballon.rotate(-x+1)
    else:
        ballon.rotate(-x)
