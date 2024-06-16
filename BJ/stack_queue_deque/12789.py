# 5 4 1 2 3
# 5->stack
# 4 ->stack
# 1 ->ouput
# 2 ->output
# 3 ->output
import sys
N = int(sys.stdin.readline().rstrip())
input = [int(x) for x in (sys.stdin.readline().split())]
stack = []
minx = min(input)
for i in input:
    if len(input)==0:
        break
    elif len(stack)==0:
        i = input.pop()
    elif input[-1] < stack[-1]:
        i = input.pop()
    else:
        i = stack.pop()
     
    if i <= minx:
        minx = i+1
    elif i > minx and len(input)==0:
        break
    else:
        stack.append(i)
    #print(f'i={i}, stack={stack}, input={input}')
sorted_stack = sorted(stack,reverse=True)
if (len(stack) == 0 and len(input) == 0) or (len(input)==0 and stack==sorted_stack):
    print('Nice')
else:
    print('Sad')