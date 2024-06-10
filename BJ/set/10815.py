import sys
N = int(sys.stdin.readline())
cards = set(int(x) for x in sys.stdin.readline().split())
M = int(sys.stdin.readline())
array = [int(x) for x in sys.stdin.readline().split()]
for i in array:
    if i in cards:
        print(1,end=' ')
    else:
        print(0,end=' ')