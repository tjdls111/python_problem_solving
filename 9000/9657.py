N = int(input())

dp = [0] * 1001  # 그 돌 개수가 될 때, 그게 가능한 사람
# 1: 상근, 2: 창영


dp[1] = 1
dp[2] = 2
dp[3] = 1
dp[4] = 1
for i in range(5, N + 1):
    if dp[i - 1] == 2 or dp[i - 3] == 2 or dp[i - 4] == 2:
        dp[i] = 1
    else:
        dp[i] = 2

if dp[N] == 2:
    print('CY')
else:
    print('SK')