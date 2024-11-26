#https://www.acmicpc.net/problem/14502
n, m = map(int,input().split())
maps = [[]*n for _ in range(m)]
for i in range(m):
    for j in list(map(int,input().split())):
        maps[i].append(j)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
    
def dfs(maps,x,y):
    print(x,y)
    if maps[y][x]==1:
        return
    flag=0
    while True:
        for i in range(4):            
            nx = x+dx[i]
            ny = y+dy[i]
            print(f'nx={nx},ny={ny}')
            if (nx < 0 or nx >=n) or (ny <0 or ny >=m):
                flag=1
                break        
            if maps[y][x]==0 and maps[ny][nx]==2:
                maps[y][x]=2                
                dfs(maps,nx,ny)
        if flag==1:
            break
    return
      
print(dfs(maps,0,0))    
print(maps)