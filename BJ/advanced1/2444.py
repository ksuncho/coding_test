N = int(input())
half = (2*N-1)//2
for i in range(2*N-1):
    if i <= half:
        print(' '*((half)-i)+'*'*(2*i+1))
    else:
        print(' '*(i-(half))+'*'*(2*N-1-(i-(half))*2))