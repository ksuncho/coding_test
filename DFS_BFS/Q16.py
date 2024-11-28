#https://www.acmicpc.net/problem/14502
from itertools import combinations
import copy
n, m = map(int,input().split())
omaps = []
for i in range(n):
    omaps.append(list(map(int,input().split())))

virus=[(i,j) for i in range(n) for j in range(m) if omaps[i][j]==2]
    
def dfs(maps,x,y):
    #print(x,y)
    if (x < 0 or x >=n) or (y <0 or y >=m):
        return False
    if maps[x][y]==0:
        maps[x][y]=2  
        dfs(maps,x+1,y)
        dfs(maps,x,y+1)
        dfs(maps,x-1,y)
        dfs(maps,x,y-1)        
        return True
    return False

# for i in range(len(omaps)):
#     print(omaps[i])
zeros = []
for i in range(n):
    for j in range(m):
        if omaps[i][j]==0:
            zeros.append((i,j))
appended_wall = combinations(zeros,3)
#appended_wall = [((0, 4), (1, 3), (3, 3))]
#print(list(appended_wall))
ans = 0
for x,y,z in appended_wall:
    #print(f'x={x}, y={y}, z={z}')
    maps=copy.deepcopy(omaps)
    maps[x[0]][x[1]]=1
    maps[y[0]][y[1]]=1
    maps[z[0]][z[1]]=1
    # for i in range(len(maps)):
    #    print(maps[i])
    result = 0
    flag=0
    for i,j in virus:
        #print(f'virus loc:{i},{j}')
        dfs(maps,i+1,j)
        dfs(maps,i,j+1)
        dfs(maps,i-1,j)
        dfs(maps,i,j-1)        
    # for i in range(len(maps)):
    #     print(maps[i])
    for i in range(n):
        for j in range(m):
            if maps[i][j]==0:
                result+=1
    ans = max(ans,result)

print(ans)