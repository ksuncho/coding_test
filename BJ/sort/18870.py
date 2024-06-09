import sys
N = int(sys.stdin.readline())
array = [x for x in map(int,sys.stdin.readline().split())]
s_array = set(array)
s_array = list(s_array)
s_array.sort()
# for dot in array:
#     print(s_array.index(dot),end=' ')
dic = {s_array[i]: i for i in range(len(s_array))}
for i in array:
    print(dic[i],end=' ')