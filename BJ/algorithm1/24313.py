a1,a0 = map(int,input().split())
c = int(input())
n = int(input())
flag = 1
for i in range(n,101):
    if a1*i+a0 <= c*i:
        continue
    else:
        flag = 0
print(flag)