#https://www.acmicpc.net/problem/18406
N = str(input())
data = [int(i) for i in N]
length = len(data)
#print(length)
if sum(data[0:length//2])==sum(data[length//2:length]):
    print('LUCKY')
else:
    print('READY')