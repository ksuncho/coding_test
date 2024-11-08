from itertools import combinations
N, M = map(int, input().split())
data = list(map(int,input().split()))
comb = list(combinations(data,2))
count=0
for i in comb:
    if i[0]!=i[1]:
        count+=1

print(count)
