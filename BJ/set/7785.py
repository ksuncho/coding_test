import sys
N = int(sys.stdin.readline().rstrip())
check = set()
for _ in range(N):
    name, attend = sys.stdin.readline().split()
    if attend == 'enter':
        check.add(name)
    else:
        check.remove(name)
check =sorted(list(check), reverse=True)
for i in check:
    print(i)
