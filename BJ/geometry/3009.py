# x1,y1 = map(int,input().split())
# x2,y2 = map(int,input().split())
# x3,y3 = map(int,input().split())
# minx = min(x1,x2,x3)
# maxx = max(x1,x2,x3)
# miny = min(y1,y2,y3)
# maxy = max(y1,y2,y3)
tri = []
for _ in range(3):
    tri.append(list(map(int,input().split())))
minx = min(tri[0][0],tri[1][0],tri[2][0])
maxx = max(tri[0][0],tri[1][0],tri[2][0])
miny = min(tri[0][1],tri[1][1],tri[2][1])
maxy = max(tri[0][1],tri[1][1],tri[2][1])
rect =[[minx,miny],[minx,maxy],[maxx,miny],[maxx,maxy]]
for x in rect:
    if x not in tri:
        print(x[0],x[1])