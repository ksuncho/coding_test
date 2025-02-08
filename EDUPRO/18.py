import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/18.txt')

input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush, nlargest

devlist = defaultdict(list)
minsalpq = []
maxcomppq = []

def push(pid,salary,avg):
    heappush(minsalpq, (salary,pid))
    heappush(maxcomppq, (-avg,-pid))

def register(pid, salary, C, J, P):
    devlist[pid]=[salary,C,J,P]
    push(pid, salary, (C + J + P)/3)

def cancel(pid):
    devlist[pid].clear()

def update(pid,flag,X):
    if len(devlist[pid])==0: return
    devlist[pid][flag+1]=X
    salary, C, J, P = devlist[pid]
    push(pid, salary, (C + J + P)/3)

def hire_min():    
    while minsalpq:
        salary, pid = heappop(minsalpq)
        if len(devlist[pid])==0: continue
        if salary == devlist[pid][0]:
            print(pid)
            cancel(pid)
            break

def hire_max():
    cnt = 0
    while maxcomppq:
        avg, pid = map(abs, heappop(maxcomppq))
        if len(devlist[pid])==0: continue
        if avg == (devlist[pid][1] + devlist[pid][2] + devlist[pid][3])/3:
            print(pid, end=' ')
            cancel(pid)
            cnt += 1
        if cnt == 3:
            print()
            break
        #print(avg,pid)
        #print(devlist)

for _ in range(int(input())):
    cmd, *val = input().split()
    val = map(int, val)
    if cmd == 'register': register(*val)
    if cmd == 'cancel': cancel(*val)
    if cmd == 'update': update(*val)
    if cmd == 'hire_min': hire_min(*val)
    if cmd == 'hire_max': hire_max(*val)