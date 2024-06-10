import sys
N, M = map(int, sys.stdin.readline().split())
pokedex = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    pokedex[name]=int(i)
bb = {v:k for k,v in pokedex.items()} 
for i in range(M):
    qq = sys.stdin.readline().rstrip()
    if not qq.isdigit():
        print(pokedex.get(qq)+1)
    else:
        print(bb.get(int(qq)-1))