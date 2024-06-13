import sys
K = int(sys.stdin.readline().rstrip())
array=[]
for _ in range(K):
    input = int(sys.stdin.readline().rstrip())
    if input != 0:
        array.append(input)
    else:
        array.pop()
print(sum(array))