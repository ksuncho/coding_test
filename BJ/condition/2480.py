A, B, C = map(int,input().split())
if (A==B and B==C):
    z = 10000 + A * 1000
elif (A==B and B!=C) or (A==C and B!=C):
    z = 1000 + A * 100
elif (B==C and B!=A):
    z = 1000 + B * 100
else:
    z = 100 * max(A,B,C)
print(z)