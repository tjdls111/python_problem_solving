import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())

dp = [[0] * 100_001 for _ in range(4)]

dp[1][1] = 1
dp[2][2] = 1
dp[1][3], dp[2][3], dp[3][3] = 1, 1, 1

for i in range(4, 100_001):
    dp[1][i] = (dp[2][i - 1] + dp[3][i - 1]) % 1_000_000_009
    dp[2][i] = (dp[1][i - 2] + dp[3][i - 2]) % 1_000_000_009
    dp[3][i] = (dp[1][i - 3] + dp[2][i - 3]) % 1_000_000_009

T = int(input())
for _ in range(T):
    tmp = int(input())
    print((dp[1][tmp] + dp[2][tmp] + dp[3][tmp])% 1_000_000_009)
