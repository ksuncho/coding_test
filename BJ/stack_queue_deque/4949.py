import sys
# my 1st answer
# while True:
#     essay = sys.stdin.readline().rstrip()
#     if essay == '.':
#         break
#     stack=[]
#     cnt = 0
#     for w in essay:
#         w = str(w)
#         cnt+=1
#         if w == '.':
#             break
#         elif w == '(':
#             stack.append(w)
#         elif len(stack)!=0 and w == ')' and stack[-1]=='(':
#             stack.pop()
#         elif w == '[':
#             stack.append(w)
#         elif len(stack)!=0 and w == ']' and stack[-1]=='[':
#             stack.pop()
#     if len(stack) == 0:
#         print('yes')
#     else:
#         print('no')

while True:
    essay = sys.stdin.readline().rstrip()
    if essay == '.':
        break
    stack=[]
    cnt = 0
    for w in essay:
        w = str(w)
        if w == '.':
            break
        elif w in ['(','[']:
            stack.append(w)
        elif w == ')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(w)
        elif w == ']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(w)
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
            


