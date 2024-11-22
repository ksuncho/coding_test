from collections import deque
from itertools import permutations
n, m , k , x = map(int,input().split())
array = [[] for i in range(n)]
#print(array)

cities = set()
for _ in range(m):
    i,j=map(int,input().split())    
    array[i-1].append(j)    
    cities = cities | set((i,j))    
#print(array)
queue=deque()

def bfs (array,start,end,visited):
    queue.append(start)
    visited[start-1]=1
    cnt=0       
    while queue:
        v = queue.popleft()
        if v == end:
            cnt+=1
            break
        for i in array[v-1]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1]=1
                cnt+=1
                print(queue)        
    return cnt

combi = permutations(cities,2)
for start,end in list(combi):
    print(start,end) 
    if array[start-1]==[]:
        continue
    else:
        visited = [0]*len(cities)
        count = bfs(array,start,end,visited)
        #count = sum(visited)
        print(f'{start} {end} {visited} {count}')
        if count==k+1:
            print(f'find:{start} {end}!!')
        
    







