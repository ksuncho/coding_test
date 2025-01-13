# https://codepass.co.kr/contest/450/problem/6?cursor=eyJwcm9ibGVtc2V0IjoiY180NTAiLCJmaWVsZCI6MCwiaWR4Ijo1fQ==
import sys
if sys.platform == 'win32':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/06.txt')

T = int(input())
for ts in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ptrb = 0
    cnt = 0
    for ptra in range(len(A)):
        if A[ptra] <= B[ptrb]:
            continue
        else:
            cnt += ptrb
        for j in range(ptrb,len(B)):
            if A[ptra] <= B[j]:
                ptrb = j
                continue
            else:
                cnt +=1
        
    print(cnt)