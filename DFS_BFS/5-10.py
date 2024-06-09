N, M = map(int, input().split())
graph = []
#if 1
# for _ in range(N):
#    graph.append(list(map(int,input())))
#else
import sys
file = open('D:/MM/python/coding_test/coding_test/DFS_BFS/5-10_data.txt','r')
lines = file.readlines()
for line in lines:
    graph.append(list(map(int,line.rstrip())))
#endif
def dfs(x, y):
    if (x < 0) or (x>=N) or (y<0) or(y>=M):
        return False
    else:
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result+=1
print(result)
