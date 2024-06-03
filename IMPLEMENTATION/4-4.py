M, N = map(int, input().split())
A, B, d = map(int, input().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int,input().split())))
# M = 5
# N = 4
# A = 1
# B = 1
# d = 0
# #MAP = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# MAP = [[1,1,1,1,1],[1,0,0,0,1],[1,1,0,0,1],[1,1,1,1,1]]

#if 0
#My answer
def rotate(d):
    if d == 0:
        newd = 3        
    elif d == 1:
        newd = 0
    elif d == 2:
        newd = 1
    else:
        newd = 2
    return newd

def rotandgo(x,y,d):
    newx = x
    newy = y
    if d == 0:
        newd = 3
        newx = x - 1
    elif d == 1:
        newd = 0
        newy = y - 1
    elif d == 2:
        newd = 1
        newx = x + 1    
    else:
        newd = 2
        newy = y + 1
    return newx, newy, newd

def back(x,y,d):
    newx = x
    newy = y
    newd = d
    if d == 0:
        newy = y + 1
    elif d == 1:
        newx = x - 1
    elif d == 2:
        newy = y - 1    
    else:
        newx = x + 1
    return newx, newy, newd

def lookleft(x,y,d):
    newx = x
    newy = y
    newd = d
    if d == 0:
        newx = x - 1
    elif d == 1:
        newy = y - 1
    elif d == 2:
        newx = x + 1    
    else:
        newy = y + 1
    return newx, newy, newd

V = MAP
u_y = A
u_x = B
u_d = d
count = 0
while True:
    if ((u_x < 1)|(u_x > M-1)|(u_y <1)|(u_y > N-1)):
        break
    lx, ly, dd = lookleft(u_x,u_y,u_d)
    if V[u_y][u_x] == 0:
        V[u_y][u_x] = 1
        count += 1
    elif (V[ly][lx] == 0):
        (u_x, u_y, u_d) = rotandgo(u_x, u_y, u_d)
    elif ((MAP[u_y-1][u_x] | V[u_y-1][u_x]) & (MAP[u_y + 1][u_x] | V[u_y + 1][u_x]) \
        & (MAP[u_y][u_x -1] | V[u_y][u_x -1]) & (MAP[u_y][u_x + 1] | V[u_y][u_x + 1])):
        (u_x, u_y, u_d) = back(u_x, u_y, u_d)
        lx, ly, dd = lookleft(u_x,u_y,u_d)
        if MAP[ly][lx] == 1:
            break
    else:
        u_d = rotate(u_d)

    # print(f'LX:{lx},LY:{ly},V[{ly}][{lx}]:{V[ly][lx]},X:{u_x},Y:{u_y},DIR:{u_d}')
    # for i in range(N):            
    #     print(i,V[i])
    
print(count)

#else
#Book's answer
V = [[0] * M for _ in range(N)]
V[A][B] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnleft():
    global d
    d -= 1
    if d == -1:
        d = 3
    
count = 1
turn_time = 0
while True:
    turnleft()
    nx = A + dx[d]
    ny = B + dy[d]
    if V[nx][ny] == 0 and MAP[nx][ny] == 0:
        V[nx][ny] = 1
        A = nx
        B = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = A - dx[d]
        ny = B - dy[d]
        if MAP[nx][ny] == 0:
            A = nx
            B = ny
        else:
            break
        turn_time = 0

print(count)
#endif