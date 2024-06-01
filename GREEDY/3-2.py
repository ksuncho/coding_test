N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[N-1]
second = data[N-2]
total = 0
while True:
    for _ in range(K):
        total += first
        M -= 1
        if M == 0:
            break
    total += second
    M -= 1
    if M == 0:
        break

print(total)

