#https://www.acmicpc.net/problem/18405
from collections import deque
n, k = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
s, x, y = map(int,input().split())

def dfs(x,y,v,r):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if r==0:
        return False
    aa=array[x][y]
    #print(f'x={x},y={y},v={v},r={r},array[x][y]={aa}')
    if array[x][y]==0:
        array[x][y]=v
        dfs(x-1,y,v,r-1)
        dfs(x,y-1,v,r-1)
        dfs(x+1,y,v,r-1)
        dfs(x,y+1,v,r-1)
        # for i in range(n):
        #     print(array[i])
        return True
    return True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,v,r):
    if x<0 or x>=n or y<0 or y>=n:
        return
    queue=deque()
    queue.append((x,y))
    while queue:
        i = queue.popleft()
        r -= 1
        print(r,i)
        if i[0]<0 or i[0]>=n or i[1]<0 or i[1]>=n:
            break
        if r < 0:
            break
        if array[i[0]][i[1]]==0:
            array[i[0]][i[1]]=v
            for k in range(4):
                queue.append((i[0]+dx[k],i[1]+dy[k]))            
    return

virus = []
for i in range(n):
    for j in range(n):
        if array[i][j]!=0:
            virus.append((i,j,array[i][j]))
virus.sort(key=lambda x:x[2])
#print(virus)
for _ in range(s,0,-1):
    for i in virus:
        queue=deque()
        for k in range(4):
            nx = i[0]+dx[k]
            ny = i[1]+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                break
            if array[nx][ny]==0:
                array[nx][ny]=i[2]            
                queue.append((nx,ny))  


print(array[x-1][y-1])