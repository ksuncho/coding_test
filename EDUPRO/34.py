import sys

from solution34 import init, add, remove, calculate
import time

CMD_INIT = 100
CMD_ADD = 200
CMD_REMOVE = 300
CMD_CALC = 400

# def pp(string, end="\n"):
# 	if tc == 3 and q == 10:
# 		print(string end=)

# def ppp(string, end="\n"):
# 	if tc == 3 and q == 10:
# 		print(string end=)

def run():
	q = int(sys.stdin.readline())
	okay = False

	mIdArr = []
	sIdArr = []
	eIdArr = []
	mIntervalArr = []

	for i in range(q):
		inputarray = sys.stdin.readline().split()
		cmd = int(inputarray[0])

		if cmd == CMD_INIT:
			inputarray = sys.stdin.readline().split()
			n = int(inputarray[1])
			k = int(inputarray[3])
			for _ in range(k):
				tinfo = sys.stdin.readline().split()
				mIdArr.append(int(tinfo[1]))
				sIdArr.append(int(tinfo[3]))
				eIdArr.append(int(tinfo[5]))
				mIntervalArr.append(int(tinfo[7]))

			init(n, k, mIdArr, sIdArr, eIdArr, mIntervalArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = sys.stdin.readline().split()
			mId = int(inputarray[1])
			sId = int(inputarray[3])
			eId = int(inputarray[5])
			mInterval = int(inputarray[7])
			add(mId, sId, eId, mInterval)
		elif cmd == CMD_REMOVE:
			inputarray = sys.stdin.readline().split()
			mId = int(inputarray[1])
			remove(mId)
		elif cmd == CMD_CALC:
			inputarray = sys.stdin.readline().split()
			sId = int(inputarray[1])
			eId = int(inputarray[3])
			ans = int(sys.stdin.readline().split()[1])
			ret = calculate(sId, eId)
			if ans != ret:
				print(f'sId={sId},eId={eId}||ret={ret},ans={ans}')
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('C:/Users/User/momo/python/coding_test/EDUPRO/sample_input34.txt', 'r')
	inputarray = sys.stdin.readline().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)