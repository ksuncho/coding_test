import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    print(' '*(T-i-1)+'*'*(i+1))