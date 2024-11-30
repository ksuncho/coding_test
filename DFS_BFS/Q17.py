#https://www.acmicpc.net/problem/18405
n, k = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
s, x, y = map(int,input().split())

def dfs(x,y,v,r):
    print(f'x={x},y={y},v={v},r={r}')
    if 0<x or x>=n or 0 < y or y>=n:
        return False
    if r == 0:
        return
    if array[x][y]==0:
        array[x][y]==v
        dfs(x-1,y,v,r-1)
        dfs(x,y-1,v,r-1)
        dfs(x+1,y,v,r-1)
        dfs(x,y+1,v,r-1)
        return True
    return False
virus = []
for i in range(n):
    for j in range(n):
        if array[i][j]!=0:
            virus.append((i,j,array[i][j]))
for i in virus:
    dfs(i[0]-1,i[1],i[2],s)
    dfs(i[0],i[1]-1,i[2],s)
    dfs(i[0]+1,i[1],i[2],s)
    dfs(i[0],i[1]+1,i[2],s)
    print(i)

for i in range(n):
    print(array[i])