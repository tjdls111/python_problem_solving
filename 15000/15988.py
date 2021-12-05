import sys
input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

# 점화식 X(n) = X(n-1) + X(n-2) + X(n-3)  ( n>=4 )

# 미리 구해두기
dp = [0]*1000001
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009


T = int(input())

for _ in range(T):
    print(dp[int(input())])
