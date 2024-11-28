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
    
def dfs(x,y):
    #print(x,y)
    if (x < 0 or x >=n) or (y <0 or y >=m):
        return False
    if maps[x][y]==0:
        maps[x][y]=2  
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)        
        return True
    return False

zeros = []
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            zeros.append((i,j))
appended_wall = combinations(zeros,3)
#print(list(appended_wall))
ans = m*n

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
            if dfs(i,j)==True:
                result+=1
                #print(dfs(i,j))
    ans = min(ans,result)
    print(f'x={x}, y={y}, z={z}, ans={ans}')
    maps[x[0]][x[1]]=0
    maps[y[0]][y[1]]=0
    maps[z[0]][z[1]]=0
# result = 0
# for i in range(n):
#     for j in range(m):
#         if maps[i][j]==False:
#             result+=1
#             print(dfs(i,j))    


for i in range(len(maps)):
    print(maps[i])
print(f'answer={ans}')