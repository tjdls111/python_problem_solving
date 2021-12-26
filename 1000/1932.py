import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())

n = int(input())
dp = [[0] * n for  _ in range(n)] # 세로: 위에서부터 몇 층 내려왔는지, 가로: 지금 위치

arr = tuple(tuple(MIISS()) for _ in range(n))

dp[0][0] = arr[0][0]

for i in range(1, n): # 층
    dp[i][0] = dp[i-1][0] + arr[i][0]

    for j in range(1, i): # 위치
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

    dp[i][i] = dp[i-1][i-1] + arr[i][i]

print(max(dp[n-1]))

