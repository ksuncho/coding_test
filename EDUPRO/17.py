import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/17.txt')
from collections import defaultdict
from heapq import heappush
input = sys.stdin.readline

def eval(sid,pid,score):
    global scorelist, avgval, sumval
    sid = int(sid)
    pid = int(pid)
    score = int(score)    
    scorelist[sid][pid]=score
    for ppid in range(1,m+1):
        cnt = 0
        for ssid in range(1,n+1):
            sscore = scorelist[ssid][ppid]
            if sid in removelist: continue
            if sscore < 1: continue
            cnt += 1         
            sumval[ppid] += sscore
        if cnt == 0: avgval[ppid] = 0
        else: avgval[ppid] = int(sumval[ppid]/cnt+0.5)
    #print(pid, scorelist[0][0])
    print(scorelist)
    print(sumval)
    print(avgval)
    pass

def clear(sid):
    removelist.append(sid)
    pass

def sumq(flag):
    sumpq = []
    for pid in range(1,m+1):
        if int(flag) == 1:               
            heappush(sumpq, (sumval[pid],pid))   
        else: heappush(sumpq, (-sumval[pid],-pid))  
    print(abs(sumpq[0][0]))        
    pass

def avgq(flag):
    avgpq = []
    for pid in range(1,m+1):
        if int(flag) == 1:               
            heappush(avgpq, (avgval[pid],pid))   
        else: heappush(avgpq, (-avgval[pid],-pid))  
    print(abs(avgpq[0][0]))        
    pass

n, m = map(int, input().split())
q = int(input())
scorelist = [[0] * (m+1) for _ in range(n+1)]
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