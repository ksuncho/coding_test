import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/17.txt')
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

def eval(sid,pid,score):
    global scorelist, avgval, sumval
    sid = int(sid)
    pid = int(pid)
    score = int(score)    
    scorelist[sid][pid]=score

    for ppid in range(1,m+1):
        cnt = 0
        sumval[ppid] = 0
        avgval[ppid] = 0
        for ssid in range(1,n+1):
            sscore = scorelist[ssid][ppid]
            if sid in removelist: continue
            if sscore < 1: continue
            cnt += 1         
            sumval[ppid] += sscore
        if cnt == 0: avgval[ppid] = 0
        else: avgval[ppid] = int(sumval[ppid]/cnt+0.5)
        heappush(summaxpq, (-sumval[ppid],-ppid))
        heappush(summinpq, (sumval[ppid],ppid))
        heappush(avgmaxpq, (-avgval[ppid],-ppid))
        heappush(avgminpq, (avgval[ppid],ppid)) 
    # print(pid, scorelist[0][0])
    # print(scorelist)
    # print(f'sumval={sumval}')
    # print(f'avgval={avgval}')
    # print(f'summaxpq={summaxpq}')
    # print(f'summinpq={summinpq}')
    # print(f'avgmaxpq={avgmaxpq}')
    # print(f'avgminpq={avgminpq}')
    pass

def clear(sid):
    global summaxpq, summinpq, avgmaxpq, avgminpq
    sid = int(sid)
    removelist.append(sid)
    cnt = 0
    for ppid in range(1,m+1):
        sscore = scorelist[sid][ppid]
        if sscore < 1: continue
        cnt += 1
        if sid in removelist: 
            sumval[ppid] -= sscore
            cnt -= 1
        if cnt == 0: avgval[ppid] = 0
        else: avgval[ppid] = int(sumval[ppid]/cnt+0.5)
        sumv, pid = heappop(summaxpq)
        if pid == -ppid: 
            heappush(summaxpq,(-sumval[ppid],-ppid))
            break
        else: heappush(summaxpq,(-sumv,-pid))
        
        sumv, pid = heappop(summinpq)
        if pid == -ppid: 
            heappush(summinpq, (sumval[ppid],ppid))
            break
        else: heappush(summinpq,(sumv,pid))
        
        avgv, pid = heappop(avgmaxpq)
        if pid == -ppid: 
            heappush(avgmaxpq,(-avgval[ppid],-ppid))
            break
        else: heappush(avgmaxpq,(-avgv,-pid))
        
        avgv, pid = heappop(avgminpq)
        if pid == -ppid: 
            heappush(avgminpq, (avgval[ppid],ppid))
            break
        else: heappush(avgminpq,(avgv,pid))

def sumq(flag):
    if int(flag) == 1:
        while summaxpq:
            sumv, pid = heappop(summaxpq)
            if sumval[-pid] == -sumv: 
                heappush(summaxpq,(sumv,pid))
                print(abs(summaxpq[0][1]))
                break
    else: 
        while summinpq:
            sumv, pid = heappop(summinpq)
            if sumval[pid] == sumv: 
                heappush(summinpq,(sumv,pid)) 
                print(abs(summinpq[0][1]))
                break

def avgq(flag):
    if int(flag) == 1:
        while avgmaxpq:
            avgv, pid = heappop(avgmaxpq)
            if avgval[-pid] == -avgv: 
                heappush(avgmaxpq,(avgv,pid))         
                print(abs(avgmaxpq[0][1]))
                break
    else:
        while avgminpq:
            avgv, pid = heappop(avgminpq)
            if avgval[pid] == avgv: 
                heappush(avgminpq,(avgv,pid))   
                print(abs(avgminpq[0][1]))
                break

n, m = map(int, input().split())
q = int(input())
scorelist = [[0] * (m+1) for _ in range(n+1)]
sumval = [0] * (m+1)
avgval = [0] * (m+1)
removelist = []
summaxpq = []
summinpq = []
avgmaxpq = []
avgminpq = []
for _ in range(q):
    cmd, *val = input().split()
    if cmd == 'EVAL': eval(*val)
    if cmd == 'SUM': sumq(*val)
    if cmd == 'AVG': avgq(*val)
    if cmd == 'CLEAR': clear(*val)
    #print(scorelist)