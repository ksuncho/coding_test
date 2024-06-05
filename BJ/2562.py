maxx = 0
for i in range(9):
    data = int(input())
    if data > maxx:
        maxx = data
        idx = i+1
print(maxx,idx,sep="\n")        