import sys
N = int(sys.stdin.readline().rstrip())
array =[]
for i in range(N):
    array.append(int(sys.stdin.readline().rstrip()))
array = sorted(array)
for i in array:
    print(i)