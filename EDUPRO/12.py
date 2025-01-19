import sys
import string
from collections import defaultdict

if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/12.txt')

input = sys.stdin.readline

SA = input().strip()
SB = input().strip()
TAR = SB
SOR = SA
if len(SA) > len(SB):
    TAR = SA
    SOR = SB
DB = set()
flag = 0

cnt = [0]*26
for word in SOR:
    cnt[ord(word)-ord('a')] += 1

for k in range(len(SOR),-1,-1):
    for i in range(len(SOR)-k+1):
        cnt[ord(SOR[i-k])-ord('a')] -= 1
        freqs = tuple(cnt)
        if freqs not in DB:
            DB.add(freqs)
        
    for j in range(len(TAR)-k+1):
        # if len(TAR)-k-j < 0:
        #     break
        cnt = [0]*26
        key = TAR[j:k+j]        
        for word in key:
            cnt[ord(word)-ord('a')] += 1
        freqt = tuple(cnt)
        if freqt in DB:
            flag = 1          
            break            
    if flag:
        print(k)
        break