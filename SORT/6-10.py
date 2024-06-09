array=[]
N = int(input())
for i in range(N):
    array.append(int(input()))
#my answer
array.sort()
for i in list(reversed(array)):
    print(i, end=' ')
#books' answer
# array = sorted(array,reverse=True)
# for i in array:
#     print(i, end=' ')