from collections import deque
N, M = map(int, input().split())
graph = []
# for _ in range(N):
#     graph.append(list(map(int,input())))
file = open('D:/MM/python/coding_test/coding_test/DFS_BFS/5-11_data.txt','r')
lines = file.readlines()
for line in lines:
    graph.append(list(map(int,line.rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:            
        [x,y] = queue.popleft()        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (nx<0) or (nx>=N) or (ny<0) or (ny>=M):
                continue 
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y]+1
    return graph[N-1][M-1]
          
print(bfs(0,0))






