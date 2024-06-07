N = 100
board = [[0] * N for _ in range(N)]
M = int(input())
for _ in range(M):
    x, y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            board[i][j] = 1
print(sum(sum(board,[])))