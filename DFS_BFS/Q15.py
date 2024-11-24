#https://www.acmicpc.net/problem/18352
from collections import deque
n, m , k , x = map(int,input().split())
array = [[] for i in range(n+1)]

for _ in range(m):
    i,j=map(int,input().split())    
    array[i].append(j)    

def bfs (array,start,visited):
    queue=deque([start])
    while queue:
        v = queue.popleft()
        for i in array[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i]=visited[v]+1
                #print(i,queue)     
    #return visited
    return

distance = [-1]*(n+1)
distance[x]=0
bfs(array,x,distance)
check = False
for end in range(1,n+1):    
    if distance[end]==k:
        print(f'{end}')
        check = True

if check is False:
    print(-1)
        
    







