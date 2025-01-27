import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/17.txt')
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

def eval(sid,pid,score):
    global scorelist
    sid = int(sid)
    pid = int(pid)
    score = int(score)    
    scorelist[sid]=[pid,score]
    avgval[pid] += score/len(scorelist[sid])
    sumval[pid] += score
    pass

def clear(sid):
    pass

def update(sid,pid,score):

    pass

def sumq(flag):
    sumpq = []
    avgpq = []
    if int(flag) == 1: 
        for sid in range(scorelist):            
            heappush(sumpq, (scorelist[sid][1],scorelist[sid][0]))
    pass

def avgq(flag):
    pass

n, m = map(int, input().split())
q = int(input())
scorelist = defaultdict(list)
sumval = [0]*m
avgval = [0]*m

for _ in range(q):
    cmd, *val = input().split()
    if cmd == 'EVAL': eval(*val)
    if cmd == 'SUM': sumq(*val)
    if cmd == 'AVG': avgq(*val)
    if cmd == 'CLEAR': clear(*val)
    print(scorelist)