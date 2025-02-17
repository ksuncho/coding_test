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
ndir = 0

def go(k, r, c, d):
    global nc, nr
    if d == 1:  # east
        nr = r
        nc = c + k
    elif d == 2: # west
        nr = r
        nc = c - k
    elif d == 3: # south
        nr = r + k
        nc = c
    else: # north
        nr = r - k
        nc = c
    return nr, nc


def turn(dir):
    global ndir
    ndir += dir
    if ndir > 3: ndir = 0
    if ndir < 0: ndir = 3
    return ndir

def bfs():
    cnt = 0
    queue.append((sr,sc,sd))
    visited[sr][sc]=1
    while queue:
        r, c, d = queue.popleft()
        for k in range(1,4):
            for d in [1,-1]:
                ndir = turn(d)
                nr, nc = go(k, r, c, ndir)
        cnt += 1
        if nr == er and nc == ec: return cnt
        if 0 < nc or nc >= N or 0 < nr or nr >= M: continue
        if visited[nr][nc] == 1: continue
        queue.append((nr,nc,sd))
        visited[nr][nc]=1
    return -1
print(MAPS)
print(bfs())


