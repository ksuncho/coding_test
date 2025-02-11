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

def go(k):
    pass

def turn(dir):
    pass

def bfs():
    cnt = 0
    queue.append((sr,sc,sd))
    visited[sr][sc]=1
    while queue:
        r, c, d = queue.popleft()
        if d == 1:  # east
            for i in range(1,4):
                nr = r
                nc = c + i
        elif d == 2: # west
            for i in range(1,4):
                nr = r
                nc = c - i
        elif d == 3: # south
            for i in range(1,4):
                nr = r + i
                nc = c
        else: # north
            for i in range(1,4):
                nr = r - i
                nc = c
        cnt += 1
        if nr == er and nc == ec: return cnt
        if 0 < nc or nc >= N or 0 < nr or nr >= M: continue
        if visited[nr][nc] == 1: continue
        queue.append((nr,nc,sd))
        visited[nr][nc]=1
    return -1
print(MAPS)
print(bfs())


