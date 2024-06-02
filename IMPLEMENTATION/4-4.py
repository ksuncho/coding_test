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
        newy = y+ 1
    return newd, newx, newy

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

if __name__ == '__main__':
    # M, N = map(int, input().split())
    # A, B, d = map(int, input().split())
    # MAP = []
    # for i in range(N):
    #     MAP.append(list(map(int,input().split())))
    M = 4
    N = 4
    A = 1
    B = 1
    d = 0
    MAP = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
  #  print(MAP)
    u_y = A
    u_x = B
    u_d = d
    count = 1
    #while True:
    MAP[u_y][u_x] = 1
    for _ in range(10):
        if ((u_x < 1)|(u_x > M-1)|(u_y <1)|(u_y > N-1)|count>10):
            break
        lx, ly, dd = lookleft(u_x,u_y,u_d)
        if (MAP[ly][lx] == 0):
            (u_x, u_y, u_d) = rotandgo(u_x, u_y, u_d)
            MAP[u_y][u_x] = 1
            count += 1
        elif ((MAP[u_y-1][u_x] == 1) & (MAP[u_y + 1][u_x] == 1) & (MAP[u_y][u_x -1] == 1) & (MAP[u_y][u_x + 1] == 1)):
            (u_x, u_y, u_d) = back(u_x, u_y, u_d)
            lx, ly, dd = lookleft(u_x,u_y,u_d)
            if MAP[ly][lx] == 1:
                break
        else:
            u_d = rotate(u_d)

        print(f'LX:{lx},LY:{ly},MAP[{lx}][{ly}]:{MAP[ly][lx]},X:{u_x},Y:{u_y},DIR:{u_d}')
        for i in range(N):            
            print(MAP[i])
        
    print(count)
    # print(MAP)
