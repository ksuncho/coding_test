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
DB = dict()
flag = 0

for k in range(len(SOR),-1,-1):
    for i in range(len(SOR)-k+1):
        # if len(SOR)-k-i < 0:
        #     break
        cnt = [0]*125
        template = SOR[i:k+i]        
        for word in template:
            cnt[ord(word)] += 1
        freqs = tuple(cnt[97:123])
        if freqs not in DB:
            DB[freqs] = 1
        
    for j in range(len(TAR)-k+1):
        # if len(TAR)-k-j < 0:
        #     break
        cnt = [0]*125
        key = TAR[j:k+j]        
        for word in key:
            cnt[ord(word)] += 1
        freqt = tuple(cnt[97:123])
        if freqt in DB:
            flag = 1          
            break            
    if flag:
        print(k)
        break