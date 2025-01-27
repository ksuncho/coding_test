import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/17.txt')
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

def eval(sid,pid,score):
    global scorelist, avgval, sumval
    sid = int(sid)
    pid = int(pid)
    score = int(score)    
    scorelist[sid]=[pid,score]
    #print(pid,len(scorelist[sid]))
    #avgval[pid] = 0
    #sumval[pid] += score
    for id in scorelist:
        x, y = scorelist[id]
        sumval[x] += y
        #avgval[i[0]] += 1
        #print(i)
    print(pid, avgval[pid])
    pass

def clear(sid):
    removelist.append(sid)
    pass

def update(sid,pid,score):

    pass

def sumq(flag):
    sumpq = []
    avgpq = []

    if int(flag) == 1: 
        for sid in scorelist:            
            heappush(sumpq, (scorelist[sid][1],scorelist[sid][0]))
    pass

def avgq(flag):
    pass

n, m = map(int, input().split())
q = int(input())
scorelist = defaultdict(list)
sumval = [[0] for _ in range(m+1)]
avgval = [[0] for _ in range(m+1)]
removelist = []
for _ in range(q):
    cmd, *val = input().split()
    if cmd == 'EVAL': eval(*val)
    if cmd == 'SUM': sumq(*val)
    if cmd == 'AVG': avgq(*val)
    if cmd == 'CLEAR': clear(*val)
    print(scorelist)