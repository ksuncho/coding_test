#최소 전력을 사용하는 기지국
# init(N, mPLimit)
#   3 <= N <=1000  N x N 지도
#   1000 <= mPLimit <=10000
#   1000의 배수
# addRigon(K,mID[],mFreq[],my[],mx[]):
#    K개의 기지국
#    각 기지국마다 고유의 ID와 주파수가짐
#    기지국 위치 (y,x)
# calculatePower()
    #  기지국과 연결시 필요한 최소 파워 계산
    #  동일 주파수가지는 기지국 간 power는 거리*10  거리 |Xa-Xb|+|Ya-Yb|
    #  서로 다른 주파수가지는 기지국 간 소모전력은 거리*10+1000