import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().strip().split())

n, goal = MIIS()
coins = list(int(input()) for _ in range(n))

dp = [0]*(goal+1)
dp[0] = 1  # 동전 0원을 써서, 0원을 만드는 경우의 수 1개(디폴트로 해두기)

for i in range(n):
    coin = coins[i]  # 동전 단위

    for j in range(coin, goal+1):
        dp[j] += dp[j-coin]  # 그 동전 단위를 써서 만들기!!

print(dp[goal])