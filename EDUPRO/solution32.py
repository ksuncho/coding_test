# https://codepass.co.kr/contest/450/problem/32?cursor=eyJwcm9ibGVtc2V0IjoiY180NTAiLCJmaWVsZCI6MCwiaWR4IjozMX0=
# solution.py

from typing import List
def init(N : int, mInfo:List[List[int]]):
    global wall, wallmap
    wall = [[0]*(N//2) for _ in range(N-2)]
    wallmap = [[0]*(N//2) for _ in range(N-2)]
    for i in range(N-2):
        for j in range(N//2):
            if i%2:
                if j ==(N//2-1): wall[i][j]=[0]*5 
                else: wall[i][j]=[mInfo[i][j*2+1],mInfo[i][j*2+3],mInfo[i+1][j*2+2],mInfo[i+2][j*2+1],mInfo[i+2][j*2+3]]                 
            else : wall[i][j]=[mInfo[i][j*2],mInfo[i][j*2+2],mInfo[i+1][j*2+1],mInfo[i+2][j*2],mInfo[i+2][j*2+2]]
                
    # print(mInfo)
    # for i in range(len(wall)):
    #     print(*wall[i])
def addRectTile(mID : int,  mTile:List[List[int]]) -> int:
    global wallmap, wall
    unpackedtile = [mTile[0][0],mTile[0][2],mTile[1][1],mTile[2][0],mTile[2][2]]
    candidate = []
    if len([i for i in unpackedtile if i>10]):
        candidate.append( [x+10 if x <10 else x-10 for x in unpackedtile])
    candidate.append([i+10 for i in unpackedtile])
    #print(candidate)
    
    for i in range(len(wallmap)):
        for j in range(len(wallmap[0])):
            for k in range(len(candidate)):
                if wall[i][j]==candidate[k]:
                    wallmap[i][j]=mID
                    if i%2: ans = i*10000+(j*2+1)
                    else: ans = i*10000+(j*2)
                    return ans                    
    return -1
   
def removeRectTile(mID : int) -> None:
    pass