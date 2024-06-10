import sys
S = sys.stdin.readline().rstrip()
subsets = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        subsets.add(S[i:j+1])
print(len(subsets))
    