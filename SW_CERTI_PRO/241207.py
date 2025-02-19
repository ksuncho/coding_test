#최소 전력을 사용하는 기지국
#(0) init(N, mPLimit)
#   3 <= N <=1000  N x N 지도
#   1000 <= mPLimit <=10000
#   1000의 배수
#(1) addRegion(K,mID[],mFreq[],my[],mx[]):
#    K개의 기지국과의 연결중 최소 전력소모
#    각 기지국마다 고유의 ID와 주파수가짐
#    기지국 위치 (y,x)
#(2) calculatePower(mID,numR)
#  기지국과 연결시 필요한 최소 파워 계산
#  동일 주파수가지는 기지국 간 power는 거리*10  거리 |Xa-Xb|+|Ya-Yb|
#  서로 다른 주파수가지는 기지국 간 소모전력은 거리*10+1000
# CMD - 0: init, 1: addRegion, 2: calPower
# 25,100           #T,MARK
# 14               #Q (횟수?)
# 0 300 4000       #CMD, N, mPLimit
# 1 6              #CMD, K
# 1 1000 189 89    #mID[0],mFreq[0],my[0],mx[0]
# 2 1000 200 129    #mID[1],mFreq[1],my[1],mx[1]
# 3 1000 100 109    #mID[1],mFreq[1],my[1],mx[1]
# 4 1000 150 189    #mID[1],mFreq[1],my[1],mx[1]
# 5 1000 20 259     #mID[1],mFreq[1],my[1],mx[1]
# 6 1000 170 139    #mID[1],mFreq[1],my[1],mx[1]
# 3 1 3 4450        #CMD, base, #of connection, minPower
# 현재 있는 기지국간 연결시 최소 소모전력

# 전체 공간을 100개의 서브공간으로 (sqrt를 역산해서 구함 100*100=10000)으로 나누어서 addRadio가 호출되면
# 해당되는 서브공간에 배치(vector에 저장)을 하고 이후에 getMinPower에서는 자신이 속한 서브공간에 있는 
# 기기들을 우선순위로 파워 합산 <-- 1st for loop
# 자신의 공간에서 mCount를 만족할 수 있으니 4방향으로 뻗어나가면서 mCount채워나가면서 검색<-- 2nd for loop
# 두번째 loop에서 if(count_power[i-1]>=mCount) break; 가 이중 loop두이에 있는 건 바깥공간을 모두 검색한
# 다음 체크해야만 해서임 Limit는 최대 파워값이고 이건 최소값을 찾는거라 mCount가 채워져야함

# 해당 무선통신기가 속한 bucket을 1차적으로 확인한 후, 겉껍질을 차례대로 순회하는데 i번째 겉껍질에 속한 기기와
# 통신하기위해 최소 1000*(i-1)만큼 파워가 필요하다는 사실을 이용해서 break
# 첫번째 loop에서 if(Limit<power)조건에 의해 무조건 mCount가 채워지지 않아야
from heapq import heappop, heappush
 
 
class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5
 
 
class Item:
    def __init__(self, idx, ca, co, pr):
        self.idx = idx
        self.ca = ca
        self.co = co
        self.pr = pr
        self.alive = True
         
    def add(self, am):
        self.pr -= am
        return self.pr > 0
     
    def __lt__(self, o):
        return self.pr < o.pr if self.pr != o.pr else self.idx < o.idx
         
buc = [[list() for _ in range(6)] for __ in range(6)]
 
 
cdb = dict()
 
 
base = [[0 for _ in range(6)] for __ in range(6)]
buc_len = [[0 for _ in range(6)] for __ in range(6)]
 
 
def init() -> None:
    for i in range(1, 6):
        for j in range(1, 6):
            buc[i][j].clear()
            base[i][j] = buc_len[i][j] = 0
             
    cdb.clear()
 
 
def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    p = Item(mID, mCategory, mCompany, mPrice - base[mCategory][mCompany])
    heappush(buc[mCategory][mCompany], p)
     
    cdb[mID] = p
    buc_len[mCategory][mCompany] += 1
 
 
    return buc_len[mCategory][mCompany]
 
 
def closeSale(mID : int) -> int:
    try:
        p = cdb[mID]
    except KeyError:
        return -1
 
 
    if not p.alive:
        return -1
     
    p.alive = False
    buc_len[p.ca][p.co] -= 1
     
    return p.pr + base[p.ca][p.co]
 
 
def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    base[mCategory][mCompany] -= mAmount
     
    while len(buc[mCategory][mCompany]) > 0:
        p = buc[mCategory][mCompany][0]
        if not p.alive:
            heappop(buc[mCategory][mCompany])
            continue
        
        if p.pr + base[mCategory][mCompany] <= 0:
            heappop(buc[mCategory][mCompany])
            p.alive = False
            buc_len[mCategory][mCompany] -= 1
            continue
 
 
        break
                
    return buc_len[mCategory][mCompany]
     
def show(mHow : int, mCode : int) -> RESULT:
    con = list()
    if mHow == 0:
        for i in range(1, 6):
            for j in range(1, 6):
                bck = []
                c = 0
                while c <= 5 and len(buc[i][j]) > 0:
                    p = heappop(buc[i][j])
                    if not p.alive:
                        continue
                    c += 1
                    con.append((p.pr + base[i][j], p.idx))
                    bck.append(p)
                for p in bck:
                    heappush(buc[i][j], p)
                 
    elif mHow == 1:
        for i in range(1, 6):
            bck = []
            c = 0
            while c <= 5 and len(buc[mCode][i]) > 0:
                p = heappop(buc[mCode][i])
                if not p.alive:
                    continue
                c += 1
                con.append((p.pr + base[mCode][i], p.idx))
                bck.append(p)
            for p in bck:
                heappush(buc[mCode][i], p)
    else:
        for i in range(1, 6):
            bck = []
            c = 0
            while c <= 5 and len(buc[i][mCode]) > 0:
                p = heappop(buc[i][mCode])
                if not p.alive:
                    continue
                c += 1
                con.append((p.pr + base[i][mCode], p.idx))
                bck.append(p)
            for p in bck:
                heappush(buc[i][mCode], p)
 
 
    con.sort()
 
 
    IDs = [0 for _ in range(5)]
    cnt = min(5, len(con))
     
    for i in range(cnt):
        IDs[i] = heappop(con)[1]
 
 
    return RESULT(cnt, IDs)