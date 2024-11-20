from collections import deque
from itertools import combinations
n, m , k , x = map(int,input().split())
array = dict()
cities = set()
for _ in range(m):
    i,j=map(int,input().split())
    array[i]=j
    cities = cities | set((i,j))
print(cities)
queue=deque()
combi = combinations(cities,2)
for i in list(combi):
    print(i)
def bfs (x,visited,array):
    if not visited[x]:
        queue.append((x,array[x]))
        while True:
            if len(queue)==0:
                return 
            else:
                queue.popleft()
    return