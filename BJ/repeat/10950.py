T = int(input())
case = []
for i in range(T):
    case.append(list(map(int,input().split())))
for x in case:
    print(x[0]+x[1])