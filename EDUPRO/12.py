import sys
import string

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
cnt = dict()

for end in range(len(SOR),0,-1):
    for start in range(len(SOR)):
        if start > end:
            break
        template = SOR[start:end]
        for word in string.ascii_lowercase:
            cnt[word]=0
        for word in template:
            cnt[word] += 1
        freq = tuple(cnt.values())
        DB[freq] = 1

    

print(SOR)
print(cnt.values())
