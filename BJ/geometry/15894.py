# 1    4
# 2    8   4 - 1 + 1 + 3   4 * 3 - 2 * 2 * 1
# 3    12  8 - 2 + 1 + 5   4 * 6 - 2 * 2 * (1 + 2)
# 4                        4 * 10- 2 * 2 * (1 + 2 + 3)
N = int(input())
def sigma(x):
    result = 0
    for i in range(1,x+1):
        result +=i
    return result

#print((4*sigma(N)-2*2*sigma(N-1)))   <-- timeout
print(4*N)