# https://codepass.co.kr/contest/450/problem/32?cursor=eyJwcm9ibGVtc2V0IjoiY180NTAiLCJmaWVsZCI6MCwiaWR4IjozMX0=
# solution.py

from typing import List
def init(N : int, mInfo:List[List[int]]):
    global wall
    wall = [[0]*(N//2) for _ in range(N-2)]
    for i in range(N-2):
        for j in range(N//2):
            if i//2:
                if j==(N//2-1): wall[i][j]=[0,0,0,0,0] 
                else: wall[i][j]=[mInfo[i][j*2+1],mInfo[i][j*2+3],mInfo[i+1][j*2+2],mInfo[i+2][j*2+1],mInfo[i+2][j*2+3]]                 
            else : wall[i][j]=[mInfo[i][j*2],mInfo[i][j*2+2],mInfo[i+1][j*2+1],mInfo[i+2][j*2],mInfo[i+2][j*2+2]]
                
    print(mInfo)
    for i in range(len(wall)):
        print(*wall[i])
def addRectTile(mID : int,  mTile:List[List[int]]) -> int:
    # global wallmap
    # wallmap = [[0]*N for _ in range(N)]
    # if
    return 0
    pass
   
def removeRectTile(mID : int) -> None:
    pass