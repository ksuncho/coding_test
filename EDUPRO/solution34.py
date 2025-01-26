# solution.py
from collections import defaultdict, deque

def init(n, k, mId, sId, eId, mInterval):
    global N, K, graph, MAP, trainlist, Vcnt
    N = n
    K = k
    graph = defaultdict(list)
    MAP = dict()
    trainlist = set()
    for i in range(K):
        MAP[mId[i]]=(mId[i], sId[i], eId[i], mInterval[i])
        trainlist.add(mId[i])
        for j in range(i):
            tId , start, end, interval = MAP[mId[j]]
            for k in range(start, end+1, interval):
                if k >= sId[i] and k <= eId[i] and (k-sId[i])%mInterval[i]== 0:
                    graph[tId].append(mId[i])
                    graph[mId[i]].append(tId)
                    break
            #print(i,j,mId[i], sId[i], eId[i], mInterval[i],tId , start, end)
    #print(n, k, len(mId))
    #print(graph)
    return


def add(mId, sId, eId, mInterval):
    MAP[mId] = (mId, sId, eId, mInterval)
    trainlist.add(mId)
    for tinfo in MAP:
        tId , start, end, interval = MAP[tinfo][0], MAP[tinfo][1], MAP[tinfo][2], MAP[tinfo][3]
        if mId == tId:continue
        for k in range(sId, eId+1, mInterval):
            if k >= start and k <= end and (k-start)%interval == 0:
                graph[mId].append(tId)
                graph[tId].append(mId)
                break
        #print(MAP[tinfo])
    #print(graph)
    return


def remove(mId):
    trainlist.remove(mId)
    return

# def bfs():


def calculate(sId, eId):
    global visited, strain, etrain, que
    strain = []
    etrain = []
    for tinfo in MAP:
        tId , start, end, interval = MAP[tinfo][0], MAP[tinfo][1], MAP[tinfo][2], MAP[tinfo][3]
        if sId >= start and sId <= end and (sId-start)%interval==0: strain.append(tId)
        if eId >= start and eId <= end and (eId-start)%interval==0: etrain.append(tId)
    #print(sId, eId, strain ,etrain)


    res = []
    for i in strain:
        if i in etrain: return 0
        visited = set()
        que = deque()
        que.append((0,i))
        visited.add(i)

        while que:
            (cost, tid) = que.popleft()        
            if tid not in trainlist: continue            
            if tid in etrain:
                res.append(cost)
                break
            for i in graph[tid]:
                if i in visited: continue
                que.append((cost+1,i))
                visited.add(i)
            #print(que)        
    for i in res:
        return min(res)
    return -1
            
#    return res