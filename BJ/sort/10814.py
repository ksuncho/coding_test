import sys
N = int(sys.stdin.readline())
member = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    member.append([int(age),str(name)])

member = sorted(member,key=lambda x:x[0])
for mem in member:
    print(mem[0],mem[1])
