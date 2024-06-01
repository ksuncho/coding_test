cur = str(input())
curx = cur[0]
cury = int(cur[1])
change = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
curx = change.get(curx)
move = [[2,1], [-2,1], [2, -1], [-2, -1], [1,2], [-1, 2], [1, -2], [-1, -2]]
count = 0
for i in move:
    newx = curx + i[0]
    newy = cury + i[1]
    if ( (newx >= 1) & (newx <= 8) & (newy >= 1) & (newy <= 8)):
        count +=1

print(count)