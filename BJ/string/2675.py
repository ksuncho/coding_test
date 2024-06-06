T = int(input())
for i in range(T):
    R, S = map(str,input().split())
    for l in S:
        print(l*int(R),end='')
    print('')