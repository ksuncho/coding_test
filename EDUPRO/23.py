## main.py
import sys
from solution23 import init, addBacteria, getMinLifeSpan, getCount

CMD_INIT = 0
CMD_ADD = 1
CMD_MINSPAN = 2
CMD_GET = 3


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            okay = True

        elif cmd == CMD_ADD:
            mTime = int(next(input_iter))
            mID = int(next(input_iter))
            mMaxSpan = int(next(input_iter))
            mHalfTime = int(next(input_iter))
            addBacteria(mTime, mID, mMaxSpan, mHalfTime)

        elif cmd == CMD_MINSPAN:
            mTime = int(next(input_iter))
            ans = int(next(input_iter))
            ret = getMinLifeSpan(mTime)
            if ret != ans:
                print(f'ret:{ret}, ans:{ans}')
                okay = False

        elif cmd == CMD_GET:
            mTime = int(next(input_iter))
            mMinSpan = int(next(input_iter))
            mMaxSpan = int(next(input_iter))
            ans = int(next(input_iter))
            ret = getCount(mTime, mMinSpan, mMaxSpan)
            if ret != ans:
                print(f'mTime:{mTime}, {mMinSpan}, {mMaxSpan}, ret:{ret}, ans:{ans}')
                okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/sample_input23.txt', 'r')
    input = sys.stdin.readline

    T, MARK = map(int, input().split())
    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)
