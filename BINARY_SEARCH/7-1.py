def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1

import sys
N, target = sys.stdin.readline().split()
N = int(N)
array = sys.stdin.readline().split()
print(sequential_search(N, target, array))
        