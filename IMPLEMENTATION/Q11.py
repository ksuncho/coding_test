#https://www.acmicpc.net/problem/3190
from collections import deque

def rot_right(dir):
    if dir!=3:
        new_dir=dir+1
    else:
        new_dir=0
    return new_dir

def rot_left(dir):
    if dir!=0:
        new_dir=dir-1
    else:
        new_dir=3
    return new_dir

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
K = int(input())
array = [[0]*N for _ in range(N)]

for _ in range(K):
    i, j = map(int,input().split())
    array[i-1][j-1]=1
print(array)
L = int(input())
cmds = dict()
for _ in range(L):
    d, c = map(str,input().split())
    cmds[int(d)]=c

dir = 0
x=0
y=0
cnt=0
flag=0
snake = deque()

while True:
    nx = x + dx[dir]
    ny = y + dy[dir]        
    if nx <0 or nx>=N or ny <0 or ny>=N or (nx,ny) in snake :        
        break
    else:
        snake.append((x,y))
        if array[ny][nx] != 1:
            snake.popleft()
            array[ny][nx]=0
        x = nx
        y = ny
        cnt +=1
        print(x,y,dir,cnt,snake)
    if cnt in cmds:
        if cmds[cnt] == 'D':
            dir = rot_right(dir)
        if cmds[cnt] == 'L':
            dir = rot_left(dir)  

print(cnt+1)    

# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# k = int(input())
# maps = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(k):#사과의 위치
#     x,y = map(int,input().split())
#     maps[x][y] = 2
# info = {}
# l = int(input())
# for _ in range(l):# 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
#     sec, direct = input().split()
#     info[int(sec)] = direct
# time = 0
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# x, y = 1, 1
# maps[y][x] = 1
# d = 0
# snakes = deque([(1, 1)])

# while True:
#     nx, ny = x+dx[d], y+dy[d]
#     # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
#     if nx<=0 or ny<=0 or nx>n or ny>n or (nx,ny) in snakes:
#         break
#     # 사과를 먹지 못하면 꼬리 없애기
#     if maps[ny][nx]!=2:
#         a,b = snakes.popleft()
#         maps[b][a]=0
#     x, y = nx, ny
#     print(x,y,d,time,snakes)
#     maps[y][x] = 1
#     snakes.append((nx, ny))
#     time+=1

	
#     # 시간에 해당하는 방향전환 정보가 있을 경우
#     if time in info.keys():
#         if info[time] == "D":
#             d = (d+1)%4
#         else:
#             nd = 3 if d==0 else d-1
#             d = nd
# print(time+1)
