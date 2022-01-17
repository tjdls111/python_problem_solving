'''
TITLE: 지름길
LINK: https://www.acmicpc.net/problem/1446
'''

import sys

input = sys.stdin.readline
INF = int(1e9)
MIIS = lambda: map(int, input().split())

N, D = MIIS()
shortcuts = list(list(MIIS()) for _ in range(N))
shortcuts.sort()

dp = [INF] * (D + 1)
dp[0] = 0

shortcuts_idx = 0

for i in range(D + 1):

    # 한 칸씩 가는 경우(지름길 거치지 않고)
    dp[i] = min(dp[i], dp[i - 1] + 1)

    # 해당 지점에서 출발하는 지름길이 있으면
    while shortcuts_idx < N and i == shortcuts[shortcuts_idx][0]:
        start, end, cost = shortcuts[shortcuts_idx]
        if end <= D:  # 그게 목표 지점 이하일 때만 봐줌(역주행 X)
            dp[end] = min(dp[end], dp[start] + cost)

        shortcuts_idx += 1

print(dp[D])