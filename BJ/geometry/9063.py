N = int(input())
points = []
minx = 10000
maxx = -10000
miny = 10000
maxy = -10000
for _ in range(N):
    x,y = map(int,input().split())
    if x >= maxx:
        maxx = x
    if x <= minx:
        minx = x
    if y >= maxy:
        maxy = y
    if y <= miny:
        miny = y
print((maxx-minx)*(maxy-miny))