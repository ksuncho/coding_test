T = int(input())
for _ in range(T):
    C = int(input())
    for i in [25, 10, 5, 1]:
        if C == 0:
            print(C, end=' ')
        else:
            print(C//i,end=' ')
            C = C % i