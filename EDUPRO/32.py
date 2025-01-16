# https://codepass.co.kr/contest/450/problem/32?cursor=eyJwcm9ibGVtc2V0IjoiY180NTAiLCJmaWVsZCI6MCwiaWR4IjozMX0=
# Main.py

import sys

from solution32 import init, addRectTile, removeRectTile

CMD_INIT = 0
CMD_ADD = 1
CMD_REMOVE = 2

MAX_N = 999

dy = (0, 0, 1, 2, 2)
dx = (0, 2, 1, 0, 2)
Shape = (1, 2, 3, 4, 5, 11, 12, 13, 14, 15)

mInfo = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
mData = [[0 for _ in range(3)] for _ in range(3)]

mSeed = 0

N = 0


def pseudo_rand():
    global mSeed
    mSeed = mSeed * 214013 + 2531011
    mSeed = mSeed & 0xffffffff
    return (mSeed >> 16) & 0x7fff


def make_info():
    global N, mInfo, Shape
    for y in range(0, N, 2):
        for x in range(0, N, 2):
            mInfo[y][x] = Shape[pseudo_rand() % 10]
            if y + 1 < N and x + 1 < N:
                mInfo[y + 1][x + 1] = Shape[pseudo_rand() % 10]


def make_info_1():
    global N, mInfo
    for y in range(0, N):
        input_iter = iter(input().split())
        for x in range(0, N):
            mInfo[y][x] = int(next(input_iter))


def run():
    global mSeed, mInfo, mData, N
    mid = 0
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    sample_1 = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mSeed = int(next(input_iter))
            if sample_1 == 1:
                make_info_1()
            else:
                make_info()
            mid = 0
            init(N, mInfo)
            okay = True
        elif cmd == CMD_ADD:
            mid = mid + 1
            for i in range(0, 5):
                mData[dy[i]][dx[i]] = int(next(input_iter))
            ret = addRectTile(mid, mData)
            ans = int(next(input_iter))
            if ret != ans:
                print(f'ret:{ret}, ans:{ans}')
                okay = False
        elif cmd == CMD_REMOVE:
            id = int(next(input_iter))
            removeRectTile(id)
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/sample_input32.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)