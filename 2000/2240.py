import sys

input = sys.stdin.readline
MIISS = lambda: map(int, input().strip().split())

T, W = MIISS()
arr = [0]+list(int(input()) for _ in range(T)) # 세로: 몇번 이동했나, 가로: 초 -> 그때까지 먹은 자두의 수를 저장함.
dp = [[0] * (T+1) for _ in range(W+1)]

for j in range(1,T+1):

    if arr[j] == 1: # 1번 나무에서 자두 떨어질 때
        dp[0][j] = dp[0][j-1] + 1 # 한번도 이동 안했을 때는 1번 나무 고정 -> 자두 추가

        for i in range(1, W):
            tmp = 1 if i%2==0 else 0 # 짝수번째로 이동했으면-> 안 움직이고도 1번 나무 자두 먹을 수 있음
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + tmp
            dp[i+1][j] = max(dp[i-1][j-1], dp[i][j-1])

        tmp = 1 if W%2==0 else 0 # 최대 이동 횟수인 경우 처리(최대 이동 횟수가 짝수이면-> 1번에 있으니까 그때 자두 먹을 수 있음)
        dp[W][j] = max(dp[W][j-1], dp[W-1][j-1]) + tmp

    elif arr[j] == 2: # 2번 나무에서 떨어질 때
        dp[0][j] = dp[0][j-1] # 한번도 이동 안했을 때는 1번 나무 고정 -> 자두 못 먹음

        for i in range(1, W):
            tmp = 1 if i%2 else 0 # 홀수 번째로 이동했으면-> 안 움직이고도 1번 나무 자두 먹을 수 있음
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + tmp
            dp[i+1][j] = max(dp[i-1][j-1], dp[i][j-1])

        tmp = 1 if W%2 else 0 # 최대 이동 횟수인 경우 처리(최대 이동 횟수가 홀수이면-> 2번에 있으니까 그때 자두 먹을 수 있음)
        dp[W][j] = max(dp[W][j-1], dp[W-1][j-1]) + tmp


ans = 0
for i in range(W+1):
    ans = max(ans, dp[i][-1])

print(ans)