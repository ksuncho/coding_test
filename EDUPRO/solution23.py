# solution.py
from heapq import heappop, heappush

def init() -> None:
    global life, time, lifepq, timepq, seq, sq, blocks
    life = [0] * 30001   # 남은수명
    time = [0] * 30001   # 반감기 cycle
    lifepq = []          # 남은수명, id
    timepq = []          # 다음 반감기 시간, id
    seq = [0] * 1000001
    sq = 1000
    blocks = [0]*1001

    return

def updatelife(tStamp):
    while timepq:
        halftime, id = timepq[0]
        if halftime > tStamp: break

        heappop(timepq)
        
        lifespan = life[id]
        halfcycle = time[id]

        seq[lifespan] -= 1
        blocks[lifespan//sq] -=1

        lifespan >>= 1
        life[id] = lifespan   # lifepq에서 수명줄어든 id를 pop하지지 않고 life list에만 update --> lazy update??                             

        if lifespan <= 99: continue
        heappush(lifepq, (lifespan, id))
        heappush(timepq, (halftime + halfcycle, id))
        seq[lifespan] += 1
        blocks[lifespan//sq] +=1
    return

def addBacteria(tStamp, mID, mLifeSpan, mHalfTime) -> None:
    updatelife(tStamp)
    life[mID]=mLifeSpan
    time[mID]=mHalfTime
    heappush(lifepq,(mLifeSpan, mID))
    heappush(timepq,(tStamp+mHalfTime, mID))
    seq[mLifeSpan] += 1
    blocks[mLifeSpan//sq] +=1
    # print(tStamp, life[0:10])
    # print(tStamp, lifepq)
    # print(tStamp, timepq)
    return

def getMinLifeSpan(tStamp) -> int:
    updatelife(tStamp)
    #print(lifepq)
    #print(tStamp, life[0:10])
    while lifepq:
        tmp, id = lifepq[0]
        if tmp != life[id] or tmp <= 99: heappop(lifepq)    # lazy update
        else: return lifepq[0][1]
    return -1

def getCount(tStamp, mMinSpan, mMaxSpan) -> int:
    updatelife(tStamp)
    res = 0
    # if mMinSpan == 4512 and mMaxSpan == 8715:
    #     print(tStamp, life[0:10])
    #     print(tStamp, time[0:10])
    while mMinSpan <= mMaxSpan and mMinSpan % sq:
        res += seq[mMinSpan]
        mMinSpan += 1
        
    while mMinSpan <= mMaxSpan and (mMaxSpan+1) % sq:
        res += seq[mMaxSpan]
        mMaxSpan -= 1
    
    while mMinSpan <= mMaxSpan:
        res += blocks[mMinSpan//sq]
        mMinSpan += sq

    return res