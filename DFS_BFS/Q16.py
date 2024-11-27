#https://www.acmicpc.net/problem/14502
from itertools import combinations
n, m = map(int,input().split())
# maps = [[]*n for _ in range(m)]
# for i in range(m):
#     for j in list(map(int,input().split())):
#         maps[i].append(j)
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y):
    #print(x,y)
    if (x < 0 or x >=n) or (y <0 or y >=m):
        return False
    if maps[x][y]==0:
        maps[x][y]=2  
        for i in range(4):            
            nx = x+dx[i]
            ny = y+dy[i]
            #print(f'nx={nx},ny={ny}')
            dfs(nx,ny)
        return True
    return False

zeros = []
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            zeros.append((i,j))
appended_wall = combinations(zeros,3)
#print(list(appended_wall))
ans = 0
for x,y,z in appended_wall:
    #print(f'x={x}, y={y}, z={z}')
    maps[x[0]][x[1]]=1
    maps[y[0]][y[1]]=1
    maps[z[0]][z[1]]=1
    # for i in range(len(maps)):
    #    print(maps[i])
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==False:
                result+=1
                #print(dfs(i,j))
    ans = max(ans,result)
    maps[x[0]][x[1]]=0
    maps[y[0]][y[1]]=0
    maps[z[0]][z[1]]=0
# result = 0
# for i in range(n):
#     for j in range(m):
#         if maps[i][j]==False:
#             result+=1
#             print(dfs(i,j))    


# for i in range(len(maps)):
#     print(maps[i])
print(f'answer={ans}')