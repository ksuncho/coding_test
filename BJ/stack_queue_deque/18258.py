from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(N):
    command = [x for x in sys.stdin.readline().split()]
    if (len(command) == 2):
        x = int(command[1])
    if command[0] == 'push':
        queue.append(x)
    elif command[0] == 'front':
        if (len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if (len(queue)==0):
            print(-1)
        else:
            print(queue[-1])
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue)==0:   
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if (len(queue)==0):
            print(-1)
        else:
            print(queue.popleft())
    