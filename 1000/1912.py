import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())

N = int(input())
dp = list(MIISS())  # 그 인덱스까지의 최대 연속 합

for i in range(1, N):
    dp[i] = max(dp[i], dp[i] + dp[i - 1])  # 그 지점의 숫자만 or 그 지점 숫자 + 그 이전의 최대 연속 합

print(max(dp))
