'''
같은 크기의 서로 다른 N개의 재료중 M개를 섞어서 그릇을 만듬
N개의 재료중 일부는 같은 재질이어서 
1<=N<=12, 1<=M<=N, 1<=Ai<=26
A A B C C 중 2개를 골라서 그릇을 만들 경우
AB, BC, AC, AA, CC의 다섯가지 조합가능
'''
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