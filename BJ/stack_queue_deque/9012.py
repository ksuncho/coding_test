import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    input = [str(x) for x in sys.stdin.readline().rstrip()]
    
    stack = []
    for PS in input:
        if PS == '(':
            stack.append(PS)
        elif PS == ')':
            if len(stack)>0:
                stack.pop()
            else:
                stack.append(PS)
                break
    if len(stack)!=0:
        print('NO')
    else:
        print('YES')

