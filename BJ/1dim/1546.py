N = int(input())
data = [x for x in map(int,input().split())]
M = max(data)
data = [x/M*100 for x in data]
print(sum(data)/N)