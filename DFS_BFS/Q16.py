#https://www.acmicpc.net/problem/14502
n, m = map(int,input().split())
maps = [[]*n for _ in range(m)]
for i in range(m):
    for j in list(map(int,input().split())):
        maps[i].append(j)

print(maps)