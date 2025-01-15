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
cnts = dict()
cntt = dict()

for word in string.ascii_lowercase:
    cntt[word]=0
#for k in range(len(SOR),-1,-1):
#cnt = [0]*26
for k in range(2,1,-1):
    print(k)
    for word in string.ascii_lowercase:
        cnts[word]=0
    for i in range(len(SOR)):
        if len(SOR)-k-i < 0:
            break
        template = SOR[i:k+i]        
        for word in template:
            cnts[word] += 1
        freqs = tuple(cnts.values())
        if freqs not in DB:
            DB[freqs] = 1        
    print(cnts)

    flag = 0
    for word in string.ascii_lowercase:
        cntt[word]=0
    for j in range(len(TAR)):
        if len(TAR)-k-j < 0:
            break
        key = TAR[j:k+j]        
        for word in key:
            cntt[word] += 1
        freqt = tuple(cntt.values())
        if freqt in DB:
            flag = 1
            print(f'{k} break!!!!')
            break            
    if flag:
         break      

#print(SOR)
#print(k)
#print(DB)
