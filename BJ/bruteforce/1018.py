N, M = map(int,input().split())
board = []
for _ in range(N):
   board.append(list(input()))
# import sys
# f1 = open('D:/MM/python/coding_test/coding_test/BJ/bruteforce/1018.txt','r')
# Lines = f1.readlines()
# for line in Lines:
#     board.append(list(map(str,line.rstrip())))


count = 0
min = 65
for x in range(N-8+1):
    for y in range(M-8+1):        
        for c in [['W','B'],['B','W']]:
            count = 0
            for i in range(8):
                for j in range(8):               
                    if ((i+j)%2==1) and (board[x+i][y+j]!=c[0]):
                        count +=1
                    elif ((i+j)%2==0) and (board[x+i][y+j]!=c[1]):
                        count +=1
            if min > count:
                min = count        

print(min)