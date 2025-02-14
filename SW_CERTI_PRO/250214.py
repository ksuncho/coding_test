# 온라인 쇼핑
# Init ()
# 매 TC마다 물품 초기화
# Sell (mID, mCategory, mCompany, mPrice)
#  : mID, mCategory, mCompany, mPrice인 물품 판매 시작
#  : 1<mID<100000000, 1<=mCategory<=5, 1<=mCompany<=5, 0<=mPrice<=100000
# Discount (mCategory, mCompany, mAmount)
#  : mCategory, mCompany의 물품 가격을 mAmount만큼 할인, 가격이 0이하이면 물품 판매 종료
# Close (mID)
#  : mID인 물품 판매 종료
# Show (mHow, mValue) 
#  : mHow = 0 모든 물품중 가격이 가장 싼 다섯개의 물품 print
#  : mHow = 1 mValue 인 Category의 물품중 가격이 가장 싼 다섯개의 물품 print
#  : mHow = 1 mValue 인 Company의 물품중 가격이 가장 싼 다섯개의 물품 print
# Sell 50000번이하 호출
# Discount 10000번이하 호출
# Close 1000번 이하 호출
# Show 10000번이하 호출?
# mID를 key, [mCategory, mCompany, mAmount] 를 value로 dict itemlist
# (mCategory, mCompany)를 key, [mID, mPrice] 를 value로 defaultdict itemlistcc
# 모든 물품용 min heapq, 각 item별, 회사별, 10개의 min heapq 만들고, Sell이랑 Discount때 update
# Discount하는 항목이 많아지면 속도가 너무 느려짐, time limit이 4초였는데, 18번까지 4초내로 나오고 TLE, 25개 tc에 대해서는 119초!
# def RESULT(cnt, IDs):
#     self
from collections import defaultdict
from heapq import heappush, heappop

def init():
    global itemlist, itemlistcc, minpq, mincat1, mincat2, mincat3, mincat4, mincat5, mincom1, mincom2, mincom3, mincom4, mincom5
    # itemlist.clear()
    # itemlistcc.clear()
    # minpq.clear()
    # mincat1.clear()
    # mincat2.clear()
    # mincat3.clear()
    # mincat4.clear()
    # mincat5.clear()
    # mincom1.clear()
    # mincom2.clear()
    # mincom3.clear()
    # mincom4.clear()
    # mincom5.clear()
    itemlist = {}
    itemlistcc = defaultdict(list)
    minpq = []
    mincat1 = []
    mincat2 = []
    mincat3 = []
    mincat4 = []
    mincat5 = []
    mincom1 = []
    mincom2 = []
    mincom3 = []
    mincom4 = []
    mincom5 = []

def update(mID:int, mCategory:int, mCompany:int, mPrice:int):
    heappush(minpq, (mPrice, mID))
    if mCategory == 1: heappush(mincat1, (mPrice, mID))
    if mCategory == 2: heappush(mincat2, (mPrice, mID))
    if mCategory == 3: heappush(mincat3, (mPrice, mID))
    if mCategory == 4: heappush(mincat4, (mPrice, mID))
    if mCategory == 5: heappush(mincat5, (mPrice, mID))
    if mCompany == 1: heappush(mincom1, (mPrice, mID))
    if mCompany == 2: heappush(mincom2, (mPrice, mID))
    if mCompany == 3: heappush(mincom3, (mPrice, mID))
    if mCompany == 4: heappush(mincom4, (mPrice, mID))
    if mCompany == 5: heappush(mincom5, (mPrice, mID))

def Sell(mID:int, mCategory:int, mCompany:int, mPrice:int) -> int:
    itemlist[mID] = [mCategory, mCompany, mPrice]
    itemlistcc[(mCategory, mCompany)].append([mID, mPrice])
    update(mID, mCategory, mCompany, mPrice)
    return len(itemlistcc[(mCategory, mCompany)])

def Close(mID):
    if mID in itemlist:
        cat, com, price = itemlist[mID]
        itemlist.pop(mID)
        itemlistcc.pop((cat,com))
        return price
    return -1

def Discount(mCategory, mCompany, mAmount):
    deletelist = []
    for i, val in enumerate(itemlistcc[(mCategory, mCompany)]):        
        id, price = val
        itemlistcc[(mCategory, mCompany)][i][1] -= mAmount
        newprice = itemlistcc[(mCategory, mCompany)][i][1]
        if newprice <= 0:
            deletelist.append(id)
        else:
            itemlist[id][2] = newprice
    for i in deletelist:
        Close(i)
    return

def Show(mHow, mValue):
    cnt = 0
    tmp = []
    ids = []
    if mHow == 0:
        pq = minpq
    if mHow == 1:
        if mValue == 1: pq = mincat1
        if mValue == 2: pq = mincat2
        if mValue == 3: pq = mincat3
        if mValue == 4: pq = mincat4
        if mValue == 5: pq = mincat5
    if mHow == 2:
        if mValue == 1: pq = mincom1
        if mValue == 2: pq = mincom2
        if mValue == 3: pq = mincom3
        if mValue == 4: pq = mincom4
        if mValue == 5: pq = mincom5
    while pq:
        if cnt >= 5: break
        price, id = heappop(pq)
        if itemlist[id][2] == price:
            cnt +=1
            ids.append(id)
            tmp.append((price,id))
    for i in tmp:
        heappush(pq, i)
    return RETURN(cnt,ids)