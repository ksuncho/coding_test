#https://www.acmicpc.net/problem/18405
n, k = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
s, x, y = map(int,input().split())

def dfs(x,y,v):    
    if 0<x or x>=n or 0 < y or y>=n:
        return False
    if array[x][y]==0:
        array[x][y]==v
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for i in range(n):
    print(array[i])