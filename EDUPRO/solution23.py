# solution.py
from heapq import heappop, heappush

def init() -> None:
    global life, time, lifepq, timepq, seq, sq, blocks
    life = [0] * 30001   # 남은수명
    time = [0] * 30001   # 반감기 시간
    lifepq = []          # 남은수명, id
    timepq = []          # 다음 반감기 시간, id
    seq = [0] * 1000001
    sq = 1000
    blocks = [0]*1001

    return

def updatelife(tStamp):
    halftime, _ = timepq[0]
    if halftime > tStamp: return
    for id, lifespan in enumerate(life):
        life[id] = lifespan << 1        

    while lifepq:
        lifespan, mID = heappop(lifepq)
        halftime, _ = heappop(timepq)

        seq[lifespan] -= 1
        blocks[lifespan//sq] -=1

        if lifespan < 99: continue
        heappush(lifepq, (lifespan,mID))
        heappush(timepq, (time[mID] + halftime, mID))

        seq[lifespan] += 1
        blocks[lifespan//sq] +=1

def addBacteria(tStamp, mID, mLifeSpan, mHalfTime) -> None:
    updatelife(tStamp, mHalfTime)
    life[mID]=mLifeSpan
    time[mID]=mHalfTime
    lifepq.heappush((mLifeSpan,mID))
    timepq.heappush((mHalfTime, mID))
    seq[mLifeSpan] += 1
    blocks[mLifeSpan//sq] +=1
    return

def getMinLifeSpan(tStamp) -> int:
    
    return 0

def getCount(tStamp, mMinSpan, mMaxSpan) -> int:
    return 0