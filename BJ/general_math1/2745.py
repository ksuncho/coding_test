N, B = map(str,input().split())
B = int(B)

y = 0
l = len(N)-1
for i in range(l+1):
    if (ord(N[i]) >= 48) and (ord(N[i])<=57):         
            x = int(N[i])
    else:
            x = ord(N[i])-55
    y += x*B**(l-i)
print(y)