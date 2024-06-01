N, K = map(int, input().split())
count = 0
while True:
    if ((N<K) | (N%K != 0)):
        N -=1             
    else:
        N = (N)//K   
    count +=1
    if N == 1:
        break

print(count)