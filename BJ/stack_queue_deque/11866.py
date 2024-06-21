import sys
N, K = map(int,sys.stdin.readline().split())
from collections import deque
queue = deque([x for x in range(1,N+1)])
array = []
i = 1
print('<',end='')
while True:
    if (len(queue)==0):
        print('>',end='')   
        break
    else:
        x=queue.popleft()        
        if i == K:
            if len(queue)==0:
                print(x, end='')
            else:
                print(x,end=', ')   
            array.append(x)
            i = 1         
        else:     
            queue.append(x)
            i +=1

