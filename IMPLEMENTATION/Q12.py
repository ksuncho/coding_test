#https://school.programmers.co.kr/learn/courses/30/lessons/60061#
N = int(input())
build_frame=[]
for _ in range(N):
    build_frame.append(list(map(int,input().split(','))))
print(build_frame)

def possible(result):
    for frame in result:
        x, y, t = frame
        if t==0:
            if y==0 or ([x,y-1,0] in result) or ([x-1,y,1] in result) or ([x,y,1] in result):
                continue
            return False
        elif t==1:
            if([x,y-1,0] in result)  or ([x+1,y-1,0] in result) or (([x-1,y,1] in result) and ([x+1,y,1] in result)):
                continue
            return False
    return True

result=[]
for i in build_frame:
    x, y, t, op = i
    if op==1:
        result.append([x, y, t])
        if not possible(result):
            result.remove([x, y, t])
    if op==0:
        result.remove([x, y, t])
        if not possible(result):
            result.append([x, y, t])
    #print(result)
result.sort()
print(result)