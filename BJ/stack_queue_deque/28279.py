from collections import deque
import sys
lst = deque()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    cmd = list(map(int,sys.stdin.readline().split()))   
    if cmd[0] == 1:
        lst.appendleft(cmd[1])
    elif cmd[0] == 2:
        lst.append(cmd[1])    
    elif cmd[0] == 5:
        print(len(lst))
    elif cmd[0] == 6:
        if len(lst)==0:
            print(1)
        else:
            print(0)
    else:
        if len(lst)==0:
            print(-1)
        else:
            if cmd[0] == 3:    
                print(lst.popleft())
            elif cmd[0] == 4:
                print(lst.pop())
            elif cmd[0] == 7:
                print(lst[0])
            elif cmd[0] == 8:
                print(lst[-1])
    #print(f'command:{cmd[0]}')

# 1
# 8
# 3
# 3
# 3
# 2
# 8