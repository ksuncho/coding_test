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
input = list(reversed(input))
minx = min(input)
x = input.pop()
cnt = 0
while True:
    if x <= minx:
        minx = x+1
    else:
        stack.append(x)
    if len(input)==0 or cnt >= 2*N:
        break
    else:
        if len(stack)!=0:
            if (input[-1] <= stack[-1]):                
                x = input.pop()                         
            else:            
                x = stack.pop()
        elif len(stack)==0:
            x = input.pop()
    cnt +=1
        
    #print(f'i={x}, stack={stack}, input={input}, minx={minx}')
sorted_stack = sorted(stack,reverse=True)
if len(input)!=0:
    print('Sad')    
elif (len(stack) == 0) or (stack==sorted_stack):
    print('Nice')
else:
    print('Sad')