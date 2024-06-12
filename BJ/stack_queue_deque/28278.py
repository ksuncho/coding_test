import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    commands = [int(x) for x in sys.stdin.readline().split()]
    #print(commands,len(commands),commands[0])
    if len(commands) == 2 and commands[0] ==1:
        stack.append(commands[-1])
    elif commands[0] ==2 :
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] ==3:
        print(len(stack))
    elif commands[0] == 4:
        if (len(stack))==0:
            print(1)
        else:
            print(0)
    elif  commands[0] == 5:
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
    #print(f'stack:{stack}')
