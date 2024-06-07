N, B = map(int,input().split())
result=[]
def tran(x,B):
    if x in range(10):
        y = str(x)
    else:
        y = chr(x+55)
    return y
while True:
    if N < B:
        result.append(tran(N,B))
        break
    else:
        result.append(tran(N%B,B))
        N = N // B
for i in result[::-1]:
    print(i,end='')