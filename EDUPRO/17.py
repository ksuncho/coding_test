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
    scorelist[sid][pid]=score
    #print(pid,len(scorelist[sid]))
    #avgval[pid] = 0
    #sumval[pid] += score
    for ppid in (1,m+1):
        cnt = 0
        for ssid in (1,n+1):
            sscore = scorelist[ssid][ppid]
            if sscore < 1: continue
            cnt += 1         
            sumval[ppid] += sscore
        avgval[ppid] = int(sumval[ppid]/cnt+0.5)
    #print(pid, sumval[pid])
    pass

def clear(sid):
    removelist.append(sid)
    pass

def update(sid,pid,score):

    pass

def sumq(flag):
    sumpq = []
    print(scorelist)
    for sid in scorelist:
        if sid in removelist: continue
        # if int(flag) == 1:               
        #     heappush(sumpq, (sumval[scorelist[sid][1]],scorelist[sid][0]))   
        # else: heappush(sumpq, (-sumval[scorelist[sid][1]],-scorelist[sid][0]))  
        print(scorelist[sid][1],sumval)
    #print(abs(sumpq[0][0]))        
    pass

def avgq(flag):
    avgpq = []
    pass

n, m = map(int, input().split())
q = int(input())
#scorelist = defaultdict(list)
scorelist = [[0] * (m+1) for _ in range(n+1)]
#sumval = [[0] for _ in range(m+1)]
sumval = [0] * (m+1)
avgval = [0] * (m+1)
removelist = []
for _ in range(q):
    cmd, *val = input().split()
    if cmd == 'EVAL': eval(*val)
    if cmd == 'SUM': sumq(*val)
    if cmd == 'AVG': avgq(*val)
    if cmd == 'CLEAR': clear(*val)
    #print(scorelist)