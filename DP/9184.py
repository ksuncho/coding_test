a = int(input())
b = int(input())
c = int(input())

dp = 1000 * [[],[],[])
dp[0][0][0] = 1

if a <= 0 or b <= 0 or c <= 0:
    dp[a][b][c]
elif a > 20 or b > 20 or c > 20:
    return dp[20]
elif a < b and b < c:
    return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
else:
    return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

print(w(a,b,c))