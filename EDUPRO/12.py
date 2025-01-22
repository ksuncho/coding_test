import sys
import string
from collections import defaultdict

if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/12.txt')

input = sys.stdin.readline

SA = input().strip()
SB = input().strip()
# TAR = SB
# SOR = SA
# if len(SA) > len(SB):
#     TAR = SA
#     SOR = SB
# DB = set()
# flag = 0

# cnts = [0]*26
# cntt = [0]*26
# for word in SOR:
#     cnts[ord(word)-ord('a')] += 1

# for word in TAR:
#     cntt[ord(word)-ord('a')] += 1

# for k in range(len(SOR),-1,-1):    
#     for i in range(k-len(SOR),-1):
#         #cnts[ord(SOR[i])-ord('a')] -= 1
#         print(f'first i:{i},k:{k},{SOR[i]}')
#     for i in range(len(SOR)-k):
#         #cnts[ord(SOR[i])-ord('a')] -= 1
#         print(f'second i:{i},k:{k},{SOR[i]}')
#     freqs = tuple(cnts)
#     if freqs not in DB:
#         DB.add(freqs)
        
#     for j in range(k-len(TAR),-1):      
#         print(f'first j:{j},k:{k},{TAR[j]}')
#         #if j > 0: cntt[ord(TAR[j])-ord('a')] -= 1
#     for j in range(len(TAR)-k):
#         print(f'second j:{j},k:{k},{TAR[j]}')
#     freqt = tuple(cntt)
#     if freqt in DB:
#         flag = 1          
#         break            
#     if flag:
#         print(k)
#         break

DB = set()
flag = 0
maxl = min(len(SA),len(SB))
for k in range(maxl, -1, -1):
    cnt = [0]*26
    for i in range(len(SA)):
        cnt[ord(SA[i])-ord('a')] += 1
        if i >= k: cnt[ord(SA[i-k])-ord('a')] -= 1
        if i >= k-1: DB.add(tuple(cnt))

    cnt = [0]*26
    for i in range(len(SB)):
        cnt[ord(SB[i])-ord('a')] += 1
        if i >= k: cnt[ord(SB[i-k])-ord('a')] -= 1
        if i >= k-1: 
            if tuple(cnt) in DB:
                flag = 1          
                break            
    if flag:
        print(k)
        break       