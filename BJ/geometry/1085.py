x, y, w, h = map(int,input().split())
A = w - x
B = h -y
minimum = min(x, y, A, B)
print(minimum)