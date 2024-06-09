result = int(input())
N = int(input())
shoppinglist = []
for i in range(N):
    shoppinglist.append(list(map(int,input().split())))
sum = 0
for x in shoppinglist:
    sum += x[0] * x[1]
if sum == result:
    print('Yes')
else:
    print('No')