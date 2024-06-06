N = 10
data = []
for i in range(N):
    x = int(input())%42
    if x not in data:
        data.append(x)
print(len(data))