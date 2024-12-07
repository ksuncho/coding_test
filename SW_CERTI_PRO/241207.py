#최소 전력을 사용하는 기지국
#(0) init(N, mPLimit)
#   3 <= N <=1000  N x N 지도
#   1000 <= mPLimit <=10000
#   1000의 배수
#(1) addRegion(K,mID[],mFreq[],my[],mx[]):
#    K개의 기지국과의 연결중 최소 전력소모
#    각 기지국마다 고유의 ID와 주파수가짐
#    기지국 위치 (y,x)
#(2) calculatePower(mID,numR)
#  기지국과 연결시 필요한 최소 파워 계산
#  동일 주파수가지는 기지국 간 power는 거리*10  거리 |Xa-Xb|+|Ya-Yb|
#  서로 다른 주파수가지는 기지국 간 소모전력은 거리*10+1000
CMD - 0: init, 1: addRegion, 2: calPower
25,100           #T,MARK
14               #Q (횟수?)
0 300 4000       #CMD, N, mPLimit
1 6              #CMD, K
1 1000 189 89    #mID[0],mFreq[0],my[0],mx[0]
2 1000 200 129    #mID[1],mFreq[1],my[1],mx[1]
3 1000 100 109    #mID[1],mFreq[1],my[1],mx[1]
4 1000 150 189    #mID[1],mFreq[1],my[1],mx[1]
5 1000 20 259     #mID[1],mFreq[1],my[1],mx[1]
6 1000 170 139    #mID[1],mFreq[1],my[1],mx[1]
3 1 3 4450        #CMD, base, #of connection, minPower
