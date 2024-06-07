N = int(input())
data = [x for x in map(int, input().split())]
count=0
for i in data:
    datax = [x for x in range(1,i+1) if i%x ==0]
    if datax == [1,i]:
        count+=1
print(count)