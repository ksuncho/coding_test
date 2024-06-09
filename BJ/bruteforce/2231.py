N = input()
min = 1000000
count = 0
#       100*x + 10*y + z
#       (101)*x + (11)*y + 2*z
# 256  = x+x//10**2+(x//10%10)+x%10
# 4256 = x+x//10**3+(x//100%10)+(x//10%10)+x%10
#1000000 = 

for x in range(1,int(N)+1):
    y = x
    base = len(str(x))    
    if base > 1: 
        for i in range(base):
            if i ==0:
                y+=x%10
            elif i == (base-1):
                y+= x//10**i
            else:
                y+= (x//(10**i))%10
    else:
        y += x
    if y == int(N):
        if min > x:
            min = x
        count+=1
if count==0:
    print(0)
else:
    print(min)