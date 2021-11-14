import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()

visited = [[False] * (M) for _ in range(N)]
ans = 0

def dfs(curr_idx):
    global ans

    # 종료
    if curr_idx == N*M:
        ans += 1
        return

    i = curr_idx // M
    j = curr_idx % M
    if visited[i][j-1] and visited[i-1][j] and visited[i-1][j-1]: # 그 위치에 두면 2X2 사각형 생김. -> 안 두는 경우
        visited[i][j] = False
        dfs(curr_idx+1)

    else: # 그 위치에 둬도 ok -> 두는 경우, 안 두는 경우
        visited[i][j] = True
        dfs(curr_idx+1)

        visited[i][j] = False
        dfs(curr_idx+1)


dfs(0)
print(ans)
