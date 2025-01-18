import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/04.txt')

input = sys.stdin.readline

from collections import deque
q = deque()
N = int(input())

def insert(pos,value):
    if pos: q.append(value)
    else:   q.appendleft(value)

def erase(pos, value):
    global q
    temp = deque()
    cnt = 0
    if pos:
        while q:            
            a = q.pop()
            if a >= value and cnt < 3: cnt+=1
            else: temp.appendleft(a)
    else:
        while q:            
            a = q.popleft()
            if a >= value and cnt < 3: cnt+=1
            else: temp.append(a)
    q = temp

def sortq(value):
    global q
    q = list(q)
    q.sort(key=lambda x:(abs(x-value),x))
    q = deque(q)

def printq(pos):
    if pos: 
        q.reverse()
        print(*q)
        q.reverse()
    else: print(*q)

for _ in range(N):
    cmd, *val = list(map(int,input().split()))
    if cmd == 1: insert(*val)
    if cmd == 2: erase(*val)
    if cmd == 3: sortq(*val)
    if cmd == 4: printq(*val)