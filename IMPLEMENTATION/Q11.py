def rot(dir):
    if dir!=3:
        new_dir=dir+1
    else:
        new_dir=0
    return new_dir

# def forward(x,y,dir):
#     dx

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
K = int(input())
array = [[0]*N for _ in range(N)]

for _ in range(K):
    i, j = map(int,input().split())
    array[i][j]=1
L = int(input())
dir = 0
x=0
y=0
cnt=0
flag=0
for _ in range(L):
    d, c = map(str,input().split())
    d = int(d)
    for _ in range(d):            
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx <0 or nx>N or ny <0 or ny>N:
            flag=1
            break
        else:
            x = nx
            y = ny
            cnt +=1
            print(x,y,dir,cnt)
        if flag:
            break
    if c == 'D':
        dir = rot(dir)
    

print(cnt)    
    
