import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N = int(input())
arr = [0] + list(MIIS())

dp = [0] * (N + 1)

for i in range(N + 1):
    dp[i] = arr[i]

    for j in range(i):
        dp[i] = max(dp[i], dp[i - j] + arr[j])  # 바로 j개 카드 세트 사는 것, 다른 세트들 더해서 사는 것

print(dp[N])