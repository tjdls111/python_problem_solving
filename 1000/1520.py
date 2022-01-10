import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MIIS = lambda: map(int, input().strip().split())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

M, N = MIIS()
sejun_map = tuple(tuple(MIIS()) for _ in range(M))

dp = list([-1] * N for _ in range(M)) # dp[x][y]에서는 목표지점까지 몇 개의 경로로 도달할 수 있는지

def dfs(i, j):
    if i == M-1 and j == N-1: # 목표 지점
        return 1

    if dp[i][j] != -1 : # 방문한 적 있으면
        return dp[i][j] # 거기에서 목표 지점까지 가는 경우의 수 리턴

    # 방문 안했으면
    dp[i][j] = 0
    for k in range(4): # 4 방향
        ni, nj = i + directions[k][0], j + directions[k][1]
        if 0 <= ni < M and 0 <= nj < N:  # 범위 체크
            if sejun_map[i][j] > sejun_map[ni][nj]:  # 가려고 하는 곳이 지금 있는 곳보다 더 낮으면
                dp[i][j] += dfs(ni, nj)

    return dp[i][j] # 거기에서 목표 지점까지 몇 개 경로로 가는지

dfs(0,0)
print(dp[0][0])