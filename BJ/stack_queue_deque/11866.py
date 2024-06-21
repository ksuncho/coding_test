N, K = map(int,input().split())
from collections import deque
queue = deque([x for x in range(N)])
i = 0
while True:
    if (len(queue)==0):
        break
    else:
        x = queue.pop()
        if i >= K:
            print(x)            
            i ==0
        else:     
            queue.append(x)
            i +=1
