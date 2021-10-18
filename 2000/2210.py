import sys

input = sys.stdin.readline

# 4방향
dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)

arr = list(list(input().split()) for _ in range(5))

ans = set()  # 중복 제거하려고


def dfs(i, j, cnt, curr_num):  # 좌표, 몇 번 이동했는지, 그때까지 만든 수
    if cnt == 6:
        ans.add(curr_num)
        return

    # 4방향으로 이동
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]

        # 범위
        if ni < 0 or nj < 0 or ni >= 5 or nj >= 5:
            continue

        dfs(ni, nj, cnt + 1, curr_num + arr[ni][nj])


# 쭉 보면서
for i in range(5):
    for j in range(5):
        dfs(i, j, 1, arr[i][j])

print(len(ans))
