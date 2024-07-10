N, W, H = map(int,input().split())
card = [[0]*W for x in range(H)]
def foldc(startx,y,c):
    for i in range(y,H):
        for j in range(startx,startx+c):
            card[i][j] = card[i][2*startx-j]

def foldr(x,starty,c):
    for j in range(x,W):
        for i in range(starty,starty+c):
            card[i][j] = card[2*starty-i][j]

def unfoldc(endx,y,c):
    for i in range(y,H):
        for j in range(endx-c,endx):            
            card[i][j] = card[i][2*endx-j-1]

def unfoldr(x,endy,c):
    for j in range(x,W):
        for i in range(endy-c,endy):
            card[i][j] = card[2*endy-i-1][j]
            # if i == -1:
            #     print(endy,c)
               
def printcard():
    for c in card:
        print(*c)

plan = []
sr=0
sc=0
for i in range(N):
    d, c = map(int, input().split())
    if d == 0:
        #foldc(sc,sr,c)
        sc += c
    else:
        #foldr(sc,sr,c)
        sr += c
    plan.append([d,c])
#    print(f'sc={sc},sr={sr},c={c}')
#print(plan)
xh,yh,xt,yt = map(int,input().split())
card[yh-1][xh-1]=1
for i in range(N):
    p = plan.pop()
#    print(f'sc={sc},sr={sr},c={p[1]}')
    if p[0] == 0:
        unfoldc(sc,sr,p[1])
        sc -= p[1]
    else:
        unfoldr(sc,sr,p[1])
        sr -= p[1]    
#    printcard()
count=0
exitcon=0
for i in range(H):
    for j in range(W):
        if card[i][j]==1:
            count+=1
            if i == (yt - 1) and j == (xt - 1):
                print(count)
                exitcon = 1
                break
        if exitcon==1:
            break
        if (i == H-1) and (j == W-1):
            print(0)