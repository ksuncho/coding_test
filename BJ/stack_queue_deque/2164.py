import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
array = [x for x in range(1,N+1)]
queue=deque(array)
i = 0
while True:
    if len(queue)==1:
        print(queue[0])
        break
    else:
        x = queue.popleft()        
        if i%2==0:
            pass
        else:
            queue.append(x)
    i+=1