N = int(input())
min=10000

for i in range(N):
    for j in range(N):
        if (5*i + 3*j) == N:
            if i+j < min:
                min = i+j

if min == 10000:
    print(-1)
else:
    print(min)
            
