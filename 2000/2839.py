import sys

input = sys.stdin.readline


N = int(input())

dp = [0] * 5001 # 각 kg 옮길 때 봉지 사용할 수 있는 방법의 수

# 3, 5kg를 옮길 때 봉지 사용할 수 있는 방법은 1개씩
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    if dp[i-5] and dp[i-3]: # 5, 3 kg 둘 다 사용 가능하면
        dp[i] = min(dp[i-5], dp[i-3]) + 1  # 5kg 봉지 사용하는 것, 3kg 봉지 사용하는 것 중 개수 적은 걸로
    elif dp[i-5]: # 5kg 봉지만 사용해서 옮길 수 있으면
        dp[i] = dp[i-5]+1
    elif dp[i-3]: # 3kg 봉지만 사용해서 옮길 수 있으면
        dp[i] = dp[i-3]+1

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])