# N = int(input())
# words = []
# for _ in range(N):
#     xx = input()    
#     words.append([xx,len(xx)])

# words = sorted(words,key=lambda x:(x[1],x[0]))
# for i in range(N):
#     if (i>0) and (words[i][0] == words[i-1][0]):
#         continue
#     else:
#         print(words[i][0])

import sys
N = int(sys.stdin.readline())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

words = set(words)
words = list(words)
words.sort()
words.sort(key=len)
for i in words:
    print(i)