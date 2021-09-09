R, C, T = map(int, input().split())
arr = list(list(input()) for _ in range(R))


# visited = list([0] * C for _ in range(R))


# 가희 위치 찾기
def find_G():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'G':
                return (i, j)


i, j = find_G()
arr[i][j] = '.'  # 가희 위치 길로 만들기
# print(i,j)
# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 탐색
max_ate = 0


def dfs(y, x, t, ate):
    global max_ate
    if t == T:  # 시간 다 되었으면
        max_ate = max(max_ate, ate)  # 최대값으로 갱신
        return

    for k in range(4):
        ny = y + directions[k][0]
        nx = x + directions[k][1]
        if 0 <= ny < R and 0 <= nx < C:  # 범위 내
            if arr[ny][nx] == '#':  # 장애물이면 갈 수 없음
                continue
            elif arr[ny][nx] == 'S':  # 고구마이면
                # visited[ny][nx] = 1
                arr[ny][nx] = '.'  # 고구마 사라짐
                dfs(ny, nx, t + 1, ate + 1)
                arr[ny][nx] = 'S'  # 돌아오면 고구마 복구
                # visited[ny][nx] = 0

            elif arr[ny][nx] == '.':  # 그냥 길이면
                # visited[ny][nx] = 1
                dfs(ny, nx, t + 1, ate)
                # visited[ny][nx] = 0


dfs(i, j, 0, 0)
print(max_ate)
