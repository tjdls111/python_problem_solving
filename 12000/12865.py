import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, K = MIIS()
arr = list(tuple(MIIS()) for _ in range(N))

dp = [[0] * (K + 1) for _ in range(N)]

# 첫번째 물품까지 넣는다고 했을 때, 가능한 최대 가치
if arr[0][0] <= K:
    for i in range(arr[0][0], K + 1):
        dp[0][i] = arr[0][1]

# 두번째 물품부터 마지막 물품까지 보기
for i in range(1, N):
    for j in range(1, K+1): # 무게 j까지일 때 최대 가치
        weight, value = arr[i]
        if j >= weight:  # 넣을 수 있는 물품이라면
            dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight]) # 그 물건 안 넣는 것, 다른 거 빼고 그 물건 넣는 것 중 가치 높은 걸로
        else:  # 물건 아예 못 넣으면
            dp[i][j] = dp[i - 1][j]

print(dp[N-1][K])
