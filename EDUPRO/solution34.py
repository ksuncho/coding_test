# solution.py
from collections import defaultdict

def init(n, k, mId, sId, eId, mInterval):
    global N, K, graph, MAP, trainlist
    N = n
    K = k
    graph = [[] for _ in range(N)]
    MAP = [[] for _ in range(N)]
    trainlist = set()
    for i in range(K):
        MAP[mId[i]] = (sId[i], eId[i], mInterval[i])
        for j in range(N):            
            if (eId[i]-sId[i])%mInterval[k]:
                graph[mId[j]].append()   
    #for i in range(N):
    #     trainlist.add(mId[i])
    # for i in range(N):
    #     sid, eid, step = MAP[mId[i]]
    #     graph[mId[i]].append()
    print(n, k, len(mId))
    return


def add(mId, sId, eId, mInterval):
	#graph[mId].append
	return


def remove(mId):
	return


def calculate(sId, eId):
	return 0