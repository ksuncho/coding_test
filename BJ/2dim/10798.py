N = 5
X = []
max_col = 0
for i in range(N):
    X.append([x for x in input()])
    if max_col < len(X[i]):
        max_col = len(X[i])
for j in range(max_col): 
    for i in range(N):
        if j < len(X[i]):
            print(X[i][j], end='')
        else:
            pass