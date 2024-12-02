#https://www.acmicpc.net/problem/18405
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
    print(f'x={x},y={y},v={v},r={r},array[x][y]={aa}')
    if array[x][y]==0:
        array[x][y]=v
        dfs(x-1,y,v,r-1)
        dfs(x,y-1,v,r-1)
        dfs(x+1,y,v,r-1)
        dfs(x,y+1,v,r-1)
        for i in range(n):
            print(array[i])
        return True
    return True
virus = []
for i in range(n):
    for j in range(n):
        if array[i][j]!=0:
            virus.append((i,j,array[i][j]))
for minute in range(s,0,-1):
    for i in virus:
        dfs(i[0],i[1]+1,i[2],1)
        dfs(i[0],i[1]-1,i[2],1)
        dfs(i[0]+1,i[1],i[2],1)
        dfs(i[0],i[1]+1,i[2],1)
        print(i)

for i in range(n):
    print(array[i])