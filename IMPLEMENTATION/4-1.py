MP = int(input())
PLAN = list(map(str ,input().split()))
cur_x = 1
cur_y = 1

def switch (key):
    move = {'R':[0,1], 'L':[0,-1], 'U':[-1,0], 'D':[1,0]}.get(key, "알 수 없는")
    return move

for p in PLAN:  
    new_x = cur_x + switch(p)[1]
    new_y = cur_y + switch(p)[0]  
    if ((new_x < 1) | (new_x > MP) | (new_y < 1) | (new_y > MP)):
        continue
    else: 
        cur_x = new_x
        cur_y = new_y
print(f"{cur_y} {cur_x}")