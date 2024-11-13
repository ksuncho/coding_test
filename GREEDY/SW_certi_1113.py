from itertools import combinations
n, m = map(int,input().split())
material = list(map(int,input().split()))
combi = list(combinations(material,m))
array = []
for i in combi:
    i = list(i)
    if i not in array:
        array.append(i)
print(array)
print(len(array))