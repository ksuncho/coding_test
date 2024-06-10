import sys
N, M = map(int, sys.stdin.readline().split())
A = set(int(x) for x in sys.stdin.readline().split())
B = set(int(x) for x in sys.stdin.readline().split())
print(len(A.difference(B))+len(B.difference(A)))