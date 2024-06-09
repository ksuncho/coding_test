import sys
N = int(sys.stdin.readline().rstrip())
array =[0]*(10000 + 1)
for _i in range(N):
    array[(int(sys.stdin.readline().rstrip()))] +=1

for i in range(len(array)):
    if array[i]==0:
        continue
    else:
        for j in range(array[i]):
            print(i)