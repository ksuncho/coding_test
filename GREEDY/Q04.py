from itertools import combinations
N = int(input())
array = list(map(int,input().split()))
# combi = []
# total = []
# for i in range(1,N+1):
#     combi = list(combinations(array,i))
#     for j in combi:
#         if sum(j) not in total:
#             total.append(sum(j))
# total.sort()
# for i in range(1,len(total)+1):
#     if i not in total:
#         print(i)
#         break
array.sort()
target = 1
for i in array:
    if target < i:
        break
    target+=i11
print(target)

