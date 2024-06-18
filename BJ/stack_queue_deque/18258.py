from collections import deque
N = int(input())
queue = deque()
for _ in range(N):
    command, input = input().strip()
    input = int(input)
    if command == 'push':
        queue.append(input)
    if command == 'front':
        print(queue[0])
    if command == 'back':
        print(queue[-1])
    if 