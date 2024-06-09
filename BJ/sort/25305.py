n, k = map(int,input().split())
array = [x for x in map(int,input().split())]
array = sorted(array,reverse=True)
print(array[k-1])