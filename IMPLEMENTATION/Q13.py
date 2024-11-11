from itertools import combinations
N, M = map(int,input().split())
house = []
chicken = []
maps = []
for i in range(N):
    maps.append(list(map(int,input().split())))
    for j,value in enumerate(maps[i]):
        if value == 1:
            house.append((i,j))
        elif value == 2:
            chicken.append((i,j))

picked_chicken = list(combinations(chicken,M))
chicken_distance = 99999
city_chicken_distance = 0
min_distance = 99999
for combi in picked_chicken:
    for h in house:
        for c in combi:
            distance=(abs(h[0]-c[0])+abs(h[1]-c[1]))
            chicken_distance = min(distance,chicken_distance)
            #print(f'HOUSE {h}, CHICKEN {c}, chicken_distance {chicken_distance}')
        city_chicken_distance+=chicken_distance
        chicken_distance = 99999
    #print(f'city_chicken_distance {city_chicken_distance}')
    min_distance=min(city_chicken_distance,min_distance)
    city_chicken_distance=0

print(min_distance)

# print(picked_chichen)
# print(picked_chichen[0])
# print(picked_chichen[0][0])



