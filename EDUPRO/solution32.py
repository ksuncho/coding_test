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
    for i in range(len(wall)):
        print(*wall[i])
def addRectTile(mID : int,  mTile:List[List[int]]) -> int:
    global wallmap, wall
    unpackedtile = [mTile[0][0],mTile[0][2],mTile[1][1],mTile[2][0],mTile[2][2]]
    candidate = []
    if len([i for i in unpackedtile if i>10]):
        candidate.append( [x+10 if x <10 else x-10 for x in unpackedtile])
        for j in range(1,6):
            candidate.append( [x+10 if x <10 else 10+j for x in unpackedtile])
    else: candidate.append([i+10 for i in unpackedtile])
    #print(unpackedtile,candidate)
    
    for i in range(len(wallmap)):
        for j in range(len(wallmap[0])):
            for k in range(len(candidate)):
                if wallmap[i][j]!=0: continue
                if wall[i][j]==candidate[k]:
                    wallmap[i][j]=mID
                    if i+1 < len(wallmap): wallmap[i+1][j]=mID
                    if j+1 < len(wallmap[0]): wallmap[i][j+1]=mID
                    if i-1 >= 0: wallmap[i-1][j]=mID
                    if j-1 >= 0: wallmap[i][j-1]=mID
                    if i%2: ans = i*10000+(j*2+1)
                    else: ans = i*10000+(j*2)
                    print(f'matched!! i:{i} j:{j} k:{k}')
                    for i in range(len(wallmap)):
                        print(*wallmap[i])
                    return ans                    
    return -1
   
def removeRectTile(mID : int) -> None:
    pass