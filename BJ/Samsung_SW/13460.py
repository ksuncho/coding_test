from collections import deque
# table = [['#','#','#','#','#'],
#          ['#','.','.','B','#'],
#          ['#','.','#','.','#'],
#          ['#','R','O','.','#'],
#          ['#','#','#','#','#']]
N = 7
M = 7
table = []
with open('D:/MM/python/coding_test/coding_test/BJ/Samsung_SW/test.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        temp = [i for i in line]
        table.append(temp)
print(table)

#d = [ l ,u, r, d]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(rx,ry,bx,by,tx,ty,dir):
    queue = deque([[rx,ry,bx,by,dir]])
    cnt=0
    while queue and cnt<10:
        print(queue)
        rxx, ryy, bxx, byy, d = queue.popleft()
        while True:
            nrx = rxx + dx[d]
            nry = ryy + dy[d]
            nbx = bxx + dx[d]
            nby = byy + dy[d]
            if ((nrx == nbx) and (nry == nby)) \
                or ((table[nry][nrx] == '#') and (table[nby][nbx] == '#')) \
                or (nrx == tx) and (nry == ty):
                break
            if table[nry][nrx] == '#':
                bxx = nbx
                byy = nby
                continue
            if table[nby][nbx] == '#':
                rxx = nrx
                ryy = nry
                continue
            bxx = nbx
            byy = nby                
            rxx = nrx
            ryy = nry
        if (rxx == tx) and (ryy == ty):
            break
        if (rxx + dx[d] == tx) and (ryy + dy[d] == ty):
            cnt +=1
            break
        for i in [j for j in range(4) if j!=d]:
            queue.append([rxx,ryy,bxx,byy,i])
        cnt += 1        
    return cnt

tx, ty, rx, ry, bx, by = 0, 0, 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 'O':
            tx = j
            ty = i            
        if table[i][j] == 'R':
            rx = j
            ry = i
        if table[i][j] == 'B':
            bx = j
            by = i
print(rx,ry,bx,by,tx,ty)
d0 = bfs(rx,ry,bx,by,tx,ty,0)
d1 = bfs(rx,ry,bx,by,tx,ty,1)
d2 = bfs(rx,ry,bx,by,tx,ty,2)
d3 = bfs(rx,ry,bx,by,tx,ty,3)

if min(d0,d1,d2,d3) >= 10:
    print(-1)
else:
    print(min(d0,d1,d2,d3))

        
