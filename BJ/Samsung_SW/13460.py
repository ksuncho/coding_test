from collections import deque
table = [['#','#','#','#','#'],
         ['#','.','.','B','#'],
         ['#','.','#','.','#'],
         ['#','R','O','.','#'],
         ['#','#','#','#','#']]
#d = [ l ,u, r, d]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(rx,ry,bx,by,tx,ty):
    queue = deque([[rx,ry,bx,by,0]])
    cnt=0
    while queue and cnt<=10:
        print(queue)
        rxx, ryy, bxx, byy, d = queue.popleft()
        while True:
            nrx = rxx + dx[d]
            nry = ryy + dy[d]
            nbx = bxx + dx[d]
            nby = byy + dy[d]
            if ((nrx == nbx) and (nry == nby)) \
                or ((table[nry][nrx] == '#') and (table[nby][nbx] == '#')):
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
        for i in range(4):
            queue.append([rxx,ryy,bxx,byy,i])
        cnt += 1        
    return cnt

tx, ty, rx, ry, bx, by = 0, 0, 0, 0, 0, 0
for i in range(5):
    for j in range(5):
        if table[i][j] == 'O':
            tx = j
            ty = i            
        if table[i][j] == 'R':
            rx = j
            ry = i
        if table[i][j] == 'B':
            bx = j
            by = i

print(bfs(rx,ry,bx,by,tx,ty))

        
