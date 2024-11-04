N = int(input())
array = list(map(int,input().split()))
array.sort()
count = 0
tcnt = 0
print(array)
for i in array:
    count += 1
    if count >= i:
        count = 0
        tcnt += 1
    #print(f'i = {i}, count = {count}')
    print(f'total count = {tcnt}')