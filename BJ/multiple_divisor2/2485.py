#1, 3, 7, 13
#  2  4  6
#1, 3,(5), 7,(9),(11), 13

#2, 6, 12, 18
#  4  6   6
#2,(4),6,(8),(10),12,(14),(16),18

import sys
N = int(sys.stdin.readline().rstrip())
pos = []
for _ in range(N):
    pos.append(int(sys.stdin.readline().rstrip()))

diff = set()
for i in range(1,N):
    diff.add(pos[i]-pos[i-1])

def gcd (a,b):
    while b > 0:
       a, b = b, a%b
    return a
    
diff = list(diff)
while True:
    if len(diff)==1:
        break
    else:
        x = diff.pop()
        y = diff.pop()
        diff.append(gcd(x,y))

   
print((max(pos)-min(pos))//diff[0]-len(pos)+1)