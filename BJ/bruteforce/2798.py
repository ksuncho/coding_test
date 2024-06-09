N, M = map(int,input().split())
max = 0
card = set([x for x in map(int,input().split())])
for x in card:
    for y in card.difference({x}):
        for z in card.difference({x,y}):
            sum =x+y+z
            if (sum <= M) and (sum > max):
                max = sum
print(max)
                        
