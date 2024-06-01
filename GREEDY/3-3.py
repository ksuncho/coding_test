M, N = map(int,input().split())
mat = []
for i in range(M):
    mat.append(min(list(map(int,input().split()))))


print(max(mat))