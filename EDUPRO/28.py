import sys
from collections import deque
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/28.txt')

input = sys.stdin.readline

M, N = map(int,input().split())
K = int(input())
BUS = []
queue = deque()
visited = [0] * (K+1)
cnt = 0

def checkBus(x1,y1,x2,y2,sx,sy,dx,dy):
    return x1 <= dx and x2 >=sx and y1 <= dy and y2 >=sy

def push(bus,cnt):
    if visited[bus[0]]: return
    queue.append((bus,cnt))
    visited[bus[0]]=1
    return checkBus(bus[1],bus[2],bus[3],bus[4],Dx,Dy,Dx,Dy)

def bfs():
    for businfo in BUS:
        _, x1, y1, x2, y2 = businfo
        if checkBus(x1, y1, x2, y2,Sx,Sy,Sx,Sy):
            if push(businfo,1): return 1
    while queue:
        bus, cnt = queue.popleft()
        
        for nextBus in BUS:
            _, x1, y1, x2, y2 = nextBus
            if checkBus(x1, y1, x2, y2,bus[1],bus[2],bus[3],bus[4]):
                if push(nextBus,cnt+1): return cnt+1
    return -1
        

for _ in range(K):
    bus, x1, y1, x2, y2 = map(int,input().split())
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    BUS.append((bus,x1,y1,x2,y2))

Sx, Sy, Dx, Dy = map(int,input().split())
print(bfs())
