#https://school.programmers.co.kr/learn/courses/30/lessons/60061#
N = int(input())
build_frame=[]
for _ in range(N):
    build_frame.append(list(map(int,input().split(','))))
print(build_frame)

def possible(frame,result):
    x, y, t, op = frame 
    if op==1:   
        if t==0:
            if(y==0 or [x,y-1,0] in result) or ([x-1,y,1] in result):
                return True
            return False
        if t==1:
            if(y!=0) :
                if([x,y-1,0] in result) or ([x-1,y,1] in result) or ([x+1,y-1,0] in result):
                    return True
            return False
    else:
        if ([x+1,y-1,0] in result) or ([x-1,y+1,1] in result):
            return True
        return False

result=[]
for i in build_frame:
    x, y, t, op = i
    if op==1:
        if possible(i,result):
            result.append([x,y,t])
    elif op==0:
        if possible(i,result):
            result.remove([x,y,t])
    print(result)
result.sort()
print(result)