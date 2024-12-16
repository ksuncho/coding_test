#NxN map에서 출발 도착 경로는 유일함을 보장
#재장전시간 가진 Tower, 타워 공격거리는 3
#도망자 최대 300
#행동주기 1-5
#도망자는 road로만 이동가능
#공격 준비 = 재장전시간 지남
#마지막 공격 대상이 아직 사정거리내에 있으면 공격 대상(mHP-1), tower는 0인 땅에만 지을 수 있음
#   1) 사정거리내 대상
#   2) 1)중 체력이 가장 적은 대상
#   3) 2)중 맵에 제일 먼저 나타난 대상
# initMap (N:int, mMap:list)  N: map size, mMap: N x N map, 0:빈땅, 1:road, 2:Start, 3:End
# addTower(mRow:int, mCol:int, mInterval:int) mRow:설치할 타워 row좌표, mCol:설치할 타워 column좌표
#                                             mInterval: 재장전 시간
# runSimulation(M:int, mHP:int, mRetTs:list , mRetHP:list ) M:도망자 # (1<=M<300)
#                                                           mInterval:도망자 행동주기 (1<=mInterval<=5)
#                                                           mRetTs: 도망자들이 죽거나 탈출한 tun을 저장할 배열
#                                                           mRetHP: 도망자들의 남아있는 체력
# exit조건: 모든 도망자가 map에서 사라지거나(죽거나) 탈출했을 때

from typing import List
CMD_ADD = 200
CMD_RUN = 300
mMaps = []
def initMap (N:int, mMap:list)-> None:
    global mMaps
    mMaps=mMap
    pass

def addTower(mRow:int, mCol:int, mInterval:int):    
    mMaps[mRow][mCol]=mInterval
    return

def runSimulation(M:int, mHP:int, mRetTs:list , mRetHP:list ) -> None:
    if all(mRetHP)==True or all(mRetHP)==True:
        return
    pass
