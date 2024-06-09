N, M = map(int,input().split())
board = []
#for _ in range(N):
#    board.append(list(input()))
import sys
f1 = open('D:/MM/python/coding_test/coding_test/BJ/bruteforce/1018.txt','r')
Lines = f1.readlines()
for line in Lines:
    board.append(list(map(str,line.rstrip())))

count = 0
for i in range(N):
    for j in range(M):
        if board[0][0]=='W':
            if ((i+j)%2==1) and (board[i][j]!='B'):
                count +=1
            elif ((i+j)%2==0) and (board[i][j]!='W'):
                count +=1
        else:
            if ((i+j)%2==1) and (board[i][j]!='W'):
                count +=1
            elif ((i+j)%2==0) and (board[i][j]!='B'):
                count +=1

print(count)