N = int(input())
#666
#1666 ...
#6666 ...
#10666 ...
#16660 ... 16666
finnum =[]
i = 0
while True:
    if len(finnum) == N:
        break
    x = str(i)
    if '666' in x:
        finnum.append(i)
    i+=1

print(finnum[N-1])