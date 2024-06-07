N = int(input())
# 1  1/1 1,1 2  1
# 2  1/2 1,2 3  2
# 3  2/1 2,1 3
# 4  3/1 3,1 4  3
# 5  2/2 2,2 4
# 6  1/3 1,3 4
# 7  1/4 1,4 5  4
# 8  2/3 2,3 5
# 9  3/2 3,2 5
# 10 4/1 4,1 5

count = 0
#print(N,end=',')
num = N
while True:
    if num <= 0:
        break
    else: 
        count +=1
        num -= count
#print(count,end=',')
for i in range(1,count):
    N -= i

#print(N)

if count%2:
    print(f'{count-N+1}/{N}')
else:
    print(f'{N}/{count-N+1}')
      
