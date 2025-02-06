import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/17.txt')
from heapq import heappush, heappop
input = sys.stdin.readline

# def eval(sid,pid,score):
#     global scorelist, avgval, sumval
#     sid = int(sid)
#     pid = int(pid)
#     score = int(score)    
#     scorelist[sid][pid]=score

#     for ppid in range(1,m+1):
#         cnt = 0
#         sumval[ppid] = 0
#         avgval[ppid] = 0
#         for ssid in range(1,n+1):
#             sscore = scorelist[ssid][ppid]
#             if sid in removelist: continue
#             if sscore < 1: continue
#             cnt += 1         
#             sumval[ppid] += sscore
#         if cnt == 0: avgval[ppid] = 0
#         else: avgval[ppid] = int(sumval[ppid]/cnt+0.5)
#         heappush(summaxpq, (-sumval[ppid],-ppid))
#         heappush(summinpq, (sumval[ppid],ppid))
#         heappush(avgmaxpq, (-avgval[ppid],-ppid))
#         heappush(avgminpq, (avgval[ppid],ppid)) 
#     # print(pid, scorelist[0][0])
#     # print(scorelist)
#     print(f'sumval={sumval}')
#     print(f'avgval={avgval}')
#     print(f'summaxpq={summaxpq}')
#     print(f'summinpq={summinpq}')
#     print(f'avgmaxpq={avgmaxpq}')
#     print(f'avgminpq={avgminpq}')
#     pass

# def clear(sid):
#     global summaxpq, summinpq, avgmaxpq, avgminpq
#     sid = int(sid)
#     removelist.append(sid)
#     cnt = 0
#     for ppid in range(1,m+1):
#         sscore = scorelist[sid][ppid]
#         if sscore < 1: continue
#         cnt += 1
#         if sid in removelist: 
#             sumval[ppid] -= sscore
#             cnt -= 1
#         if cnt == 0: avgval[ppid] = 0
#         else: avgval[ppid] = int(sumval[ppid]/cnt+0.5)
#         sumv, pid = heappop(summaxpq)
#         if pid == -ppid: 
#             heappush(summaxpq,(-sumval[ppid],-ppid))
#             break
#         else: heappush(summaxpq,(-sumv,-pid))
        
#         sumv, pid = heappop(summinpq)
#         if pid == -ppid: 
#             heappush(summinpq, (sumval[ppid],ppid))
#             break
#         else: heappush(summinpq,(sumv,pid))
        
#         avgv, pid = heappop(avgmaxpq)
#         if pid == -ppid: 
#             heappush(avgmaxpq,(-avgval[ppid],-ppid))
#             break
#         else: heappush(avgmaxpq,(-avgv,-pid))
        
#         avgv, pid = heappop(avgminpq)
#         if pid == -ppid: 
#             heappush(avgminpq, (avgval[ppid],ppid))
#             break
#         else: heappush(avgminpq,(avgv,pid))

# def sumq(flag):
#     if int(flag) == 1:
#         while summaxpq:
#             sumv, pid = heappop(summaxpq)
#             if sumval[-pid] == -sumv: 
#                 heappush(summaxpq,(sumv,pid))
#                 print(abs(summaxpq[0][1]))
#                 break
#     else: 
#         while summinpq:
#             sumv, pid = heappop(summinpq)
#             if sumval[pid] == sumv: 
#                 heappush(summinpq,(sumv,pid)) 
#                 print(abs(summinpq[0][1]))
#                 break

# def avgq(flag):
#     if int(flag) == 1:
#         while avgmaxpq:
#             avgv, pid = heappop(avgmaxpq)
#             if avgval[-pid] == -avgv: 
#                 heappush(avgmaxpq,(avgv,pid))         
#                 print(abs(avgmaxpq[0][1]))
#                 break
#     else:
#         while avgminpq:
#             avgv, pid = heappop(avgminpq)
#             if avgval[pid] == avgv: 
#                 heappush(avgminpq,(avgv,pid))   
#                 print(abs(avgminpq[0][1]))
#                 break

# n, m = map(int, input().split())
# q = int(input())
# scorelist = [[0] * (m+1) for _ in range(n+1)]
# sumval = [0] * (m+1)
# avgval = [0] * (m+1)
# removelist = []
# summaxpq = []
# summinpq = []
# avgmaxpq = []
# avgminpq = []
# for _ in range(q):
#     cmd, *val = input().split()
#     if cmd == 'EVAL': eval(*val)
#     if cmd == 'SUM': sumq(*val)
#     if cmd == 'AVG': avgq(*val)
#     if cmd == 'CLEAR': clear(*val)
#     print(scorelist)

class Player:
    def __init__(self):
        self.sum = 0
        self.avg = 0
        self.cnt = 0
    
    def update(self, dSc, dCnt):
        self.sum += dSc
        self.cnt += dCnt

        if self.cnt != 0 :
            self.avg = int(self.sum / self.cnt + 0.5)
        else: self.avg = 0
        #print(f'self.sum={self.sum}, self.avg={self.avg}, self.cnt={self.cnt}')

n, m = map(int, input().split())

scorelist = [{} for _ in range(n+1)]
playerlist = [Player() for _ in range(m+1)]

summaxpq = []
summinpq = []
avgmaxpq = []
avgminpq = []

def push(pid):
    #print(f'sum={playerlist[pid].sum},avg={playerlist[pid].avg},pid={pid}')
    heappush(summaxpq, (-playerlist[pid].sum, -pid))
    heappush(summinpq, (playerlist[pid].sum, pid))
    heappush(avgmaxpq, (-playerlist[pid].avg, -pid))
    heappush(avgminpq, (playerlist[pid].avg, pid)) 

def eval(sid, pid, score):
    if pid in scorelist[sid]:
        playerlist[pid].update(score - scorelist[sid][pid], 0)
    else:
        playerlist[pid].update(score, 1)
    scorelist[sid][pid] = score
    push(pid)

def clearf(sid):
    for pid, score in scorelist[sid].items():
        #print(f'pid={pid}, score={score}')
        playerlist[pid].update(-score, -1)
        push(pid)        
    scorelist[sid].clear()

def sumq(flag):
    pq = summaxpq if flag else summinpq
    while pq:
        sumv, pid = map(abs, pq[0])
        if playerlist[pid].sum == sumv: 
            print(pid)
            return
        heappop(pq)
    
def avgq(flag):
    pq = avgmaxpq if flag else avgminpq
    while pq:
        avgv, pid = map(abs, pq[0])
        if playerlist[pid].avg == avgv: 
            print(pid)
            return
        heappop(pq)

for i in range(1, m+1): push(i)

for _ in range(int(input())):
    cmd, *val = input().split()
    #print(cmd, *val)
    val = map(int, val)
    if cmd == 'EVAL': eval(*val)
    if cmd == 'CLEAR': clearf(*val)
    if cmd == 'SUM': sumq(*val)
    if cmd == 'AVG': avgq(*val)    
    # print(scorelist)
    # print(summaxpq)
    # print(summinpq)
    # print(avgmaxpq)
    # print(avgminpq)

# class Player:
#     def __init__(self):
#         self.sum = 0                    # 플레이어 총 점수
#         self.avg = 0                    # 플레이어의 평균 점수
#         self.cnt = 0                    # 플레이어를 평가한 스카우터 수
    
#     # Player의 정보를 업데이트하는 함수
#     # case 1) 스카우터가 플레이어를 처음 평가하는 경우      (dSc >= 1, dCnt = 1)
#     # case 2) 스카우터가 플레이어를 재평가하는 경우         (dSc < 0 or dSc > 0, dCnt = 0)
#     # case 3) 스카우터가 플레이어의 정보를 삭제하는 경우    (dSc < 0, dCnt = -1)
#     def update(self, dSc, dCnt):
#         self.sum += dSc             # dSc 만큼 총합에 더해줌
#         self.cnt += dCnt            # dCnt 만큼 스카우터 수 변동

#         if self.cnt: self.avg = int(self.sum / self.cnt + 0.5)  # 소수점 첫번째 자리에서 반올림
#         else: self.avg = 0                                      # 플레이어를 평가한 스카우터가 없는 경우
#         print(f'self.sum={self.sum}, self.avg={self.avg}, self.cnt={self.cnt}')

# N, M = map(int, input().split())        # 스카우터 수, 플레이어 수

# S = [{} for _ in range(N + 1)]          # 스카우터 정보 리스트
# P = [Player() for _ in range(M + 1)]    # 플레이어 정보 리스트

# minSum = []                 # (sum, pid)
# maxSum = []                 # (-sum, -pid)
# minAvg = []                 # (avg, pid)
# maxAvg = []                 # (-avg, -pid)

# def push(pid):
#     print(f'sum={P[pid].sum},avg={P[pid].avg},pid={pid}')
#     heappush(minSum, (P[pid].sum, pid))
#     heappush(maxSum, (-P[pid].sum, -pid))
#     heappush(minAvg, (P[pid].avg, pid))
#     heappush(maxAvg, (-P[pid].avg, -pid))

# def evaluate(sid, pid, score):
#     # sid가 pid를 평가한 적이 있는 경우
#     if pid in S[sid]:
#         P[pid].update(score - S[sid][pid], 0)
#     # sid가 pid를 처음 평가하는 경우
#     else:
#         P[pid].update(score, 1)    
#     S[sid][pid] = score         # 현재 정보를 스카우터 정보에 업데이트
#     push(pid)                   # 업데이트 된 정보를 랭크에 push

# def clearFunc(sid):
#     for pid, score in S[sid].items():   # sid가 평가했던 pid들의 모든 정보 삭제
#         print(f'pid={pid}, score={score}')
#         P[pid].update(-score, -1)
#         push(pid)                       # 업데이트 된 정보를 랭크에 push
#     S[sid].clear()                      # sid의 모든 정보 삭제

# def printSum(flag):
#     pq = maxSum if flag else minSum 
#     while pq:
#         s, pid = map(abs, pq[0])        # top 정보 가져오기
#         if P[pid].sum == s:             # 유효한 데이터인지 확인 
#             print(pid)
#             return
#         heappop(pq)

# def printAvg(flag):
#     pq = maxAvg if flag else minAvg 
#     while pq:
#         a, pid = map(abs, pq[0])        # top 정보 가져오기
#         if P[pid].avg == a:             # 유효한 데이터인지 확인 
#             print(pid)
#             return
#         heappop(pq)

# # 랭크를 0점의 플레이어들로 초기화
# for i in range(1, M + 1): push(i)       # 1 ~ M 플레이어들 랭크 초기화

# for _ in range(int(input())):
#     cmd, *val = input().split()
#     val = map(int, val)
#     if cmd == "EVAL": evaluate(*val)
#     if cmd == "CLEAR": clearFunc(*val)
#     if cmd == "SUM": printSum(*val)
#     if cmd == "AVG": printAvg(*val)
#     print(S)
#     print(maxSum)
#     print(minSum)
#     print(maxAvg)
#     print(minAvg)