import sys
N = int(sys.stdin.readline().rstrip())
#if 1
# MEM 31120KB	RUNTIME 1332ms
for i in range(N):
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)
#else
# MEM 213448KB	RUNTIME 2356ms
A = []
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))    
for i in range(N):
   print(A[i][0]+A[i][1])
#endif