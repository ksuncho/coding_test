A, B = map(str,input().split())
A = int(A[-1::-1])
B = int(B[-1::-1])
if A > B:
    print(A)
else:
    print(B)