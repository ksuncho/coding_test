N = 9
max1 = 0
row = 1
col = 1
for i in range(N):
    x1 = [y for y in map(int, input().split())]        
    if max1 < max(x1):
        max1 = max(x1)
        row = i + 1
        col = x1.index(max1) + 1
print(max1)
print(row, col)