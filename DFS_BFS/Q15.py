from collections import deque
from itertools import permutations
n, m , k , x = map(int,input().split())
array = dict()
cities = set()
for _ in range(m):
    i,j=map(int,input().split())
    array[i]=j
    cities = cities | set((i,j))
print(cities)
queue=deque()
combi = permutations(cities,2)
for start,end in list(combi):
    print(start,end)

def bfs (array,start,visited):
    queue.append(start)
    visited[start]=True        
    while queue:
        v = queue.popleft()
        for i in array.keys:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
