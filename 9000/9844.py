import sys
input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

h, w  = MIISS()
tiles = tuple(tuple(MIISS()) for _ in range(h))
dp = [[0]*w for _ in range(h)]

# 첫줄은 채우기
dp[0] = tiles[0]

# 만약에 w가 1이면
if w == 1:
    ans = 0
    for i in range(h):
        ans += tiles[i][0]
    print(ans)
else:
    # 최대 수
    for i in range(1, h):
        # 맨 앞
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + tiles[i][0]

        # 중간
        for j in range(1,w-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + tiles[i][j]

        # 맨 뒤
        dp[i][w-1] = max(dp[i-1][w-1], dp[i-1][w-2]) + tiles[i][w-1]

    print(max(dp[h-1]))