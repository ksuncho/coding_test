while True:
    sides = [x for x in map(int,input().split())]
    if (sides[0] == 0) and (sides[1] == 0) and (sides[2]==0):
        break
    else:
        sides.sort()
        if sides[2] >= sum(sides[0:2]):
            print('Invalid')     
        else:
            sides = set(sides)
            if len(sides) == 1:
                print('Equilateral')
            elif len(sides) == 2:
                print('Isosceles')
            else:
                print('Scalene')