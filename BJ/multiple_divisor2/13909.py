# 111111  6   
# 101010  3   c   i 
# 100011  3   0   0  0
# 100111  4   1   0  1
# 100101  3   0   1  1
# 100100  2   1   1  0
# 1  1   1*3
# 2  1
# 3  1
# 4  2   2*5
# 5  2
# 6  2
# 7  2
# 8  2
# 9  3   3*7
# 10 3
# 11 3
# 12 3
# 13 3
# 14 3
# 15 3   
# 16 4   4*9
# 25 5   5*11
# 36 6
import sys
N = int(sys.stdin.readline().rstrip())
# Memory excess(over?)
# window=[0]*(N+1)
# for i in range(1,N+1):
#     for j in range (i,N+1,i):
#         if window[j] == 0:
#             window[j]+=1
#         else:
#             window[j]-=1

print(int(N**0.5))