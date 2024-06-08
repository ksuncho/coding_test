a, b, c = map(int, input().split())
maxside = 0
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            sides = [i,j,k]
            sides.sort()
            if (sides[2] >= sum(sides[0:2])):
                continue
            else:
                if maxside <= sum(sides):
                    maxside = sum(sides)
print(maxside)