dp = [[[0 for col in range(101)] for row in range(101)] for depth in range(101)]
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a <= 50 or b <= 50 or c <= 50:
                dp[a][b][c]=1
            elif a > 70 or b > 70 or c > 70:
                dp[a][b][c]=dp[70][70][70]
            elif a < b and b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        i,j,k = map(int,(input().split()))
        if (i==-1 and j==-1 and k==-1):
            break
        print(f'w({i}, {j}, {k}) = {dp[i+50][j+50][k+50]}')