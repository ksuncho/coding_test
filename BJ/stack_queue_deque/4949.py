import sys
while True:
    essay = sys.stdin.readline().rstrip()
    if essay == '.':
        break
    stack=[]
    cnt = 0
    for w in essay:
        w = str(w)
        cnt+=1
        if w == '.':
            break
        elif w == '(':
            stack.append(w)
        elif len(stack)!=0 and w == ')' and stack[-1]=='(':
            stack.pop()
        elif w == '[':
            stack.append(w)
        elif len(stack)!=0 and w == ']' and stack[-1]=='[':
            stack.pop()
    #print(f'stack1:{stack1}')
    #print(f'stack2:{stack2}')
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
            


