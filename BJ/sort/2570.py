N = int(input())
array=[]
for i in range(N):
    array.append(int(input()))
array = sorted(array)
for i in array:
    print(i)