from itertools import chain
import copy
def rot(key,m,dir):
    ans=copy.deepcopy(key)
    if dir!=0:
        for i in range(m):
            for j in range(m):
                if dir==1:                    
                    ans[i][j]=key[m-j-1][i]
                    #print(key[j][m-i-1])
                elif dir==2:
                    ans[i][j]=key[m-j-1][m-i-1]
                else:
                    ans[i][j]=key[j][m-i-1]
    #print(key,ans)            
    return ans
m,n = map(int,input().split())
key = []
lock = []
for i in range(m):
    key.append([int(i) for i in input().split()])
for i in range(n):
    lock.append([int(i) for i in input().split()])

def shift(key,m,n,sftx,sfty):
    ans = [[0]*n for i in range(n)]    
    for i in range(n):
        for j in range(n):
            if (0<=i+sfty<n) and (0<j+sftx<n):
                ans[i+sfty][j+sftx]=key[i][j]            
    return ans
res = copy.deepcopy(lock)
output = 0
for dir in range(4):
    key_rot = rot(key,m,dir)
    for sfty in range(-m+1,m):
        for sftx in range(-m+1,m):
            key_sft = shift(key_rot,m,n,sftx,sfty)
            #print(f'dir:{dir},sftx:{sftx},sfty:{sfty}')
            for i in range(n):
                for j in range(n):
                    res[i][j]=lock[i][j]^key_sft[i][j]
            if set(chain.from_iterable(res)) == {1}:
                output=1 
                break
            #print(key,key_rot,key_sft,res)
if output:
    print('true')
else:
    print('false')
# print(key)
# key_rot = rot(key,3,1)
# print(key_rot)