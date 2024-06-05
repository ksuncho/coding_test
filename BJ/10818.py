import sys
N = int(input())
data = [x for x in map(int,sys.stdin.readline().split())]
print(min(data),max(data))