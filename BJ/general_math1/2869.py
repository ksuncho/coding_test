A, B, V = map(int, input().split())
x = (V-B)/(A-B)
y = (V-B)//(A-B)
if x > y:
    print(y+1)
else:
    print(y)
