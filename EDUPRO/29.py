import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/29.txt')

from collections import deque

dr = (-3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3)
dc = (0, 0, 0, 1, 2, 3, -1, -2, -3, 0, 0, 0)
MAPS = []
M, N = map(int, input().split())
for _ in range(M):
    MAPS.append(list(map(int,input().split())))

sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())
queue = deque()
visited = [[0]*N for _ in range(M)]

def bfs():
    queue.append((sr,sc,sd))
    visited[sr][sc]=1
    while queue:
        r, c, d = queue.popleft()
        for i in range(12):
            nr = r + dr[i]
            nc = c + dc[i]
print(MAPS)