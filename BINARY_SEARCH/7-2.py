def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (end + start)//2
    if array[middle] < target:
        return binary_search(array,target,middle+1,end)
    elif array[middle] > target:
        return binary_search(array,target,start,middle-1)
    else:
        return middle
    
import sys
n, target = list(map(int,sys.stdin.readline().split()))
array = list(map(int,sys.stdin.readline().split()))
result = binary_search(array, target, 0, n-1 )
if result == None:
    print("Can't find the target")
else:
    print(result+1)