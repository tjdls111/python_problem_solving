import collections
import sys

input = sys.stdin.readline

# 4방향
dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)

M, N, K = map(int, input().split())

arr = list([0] * (N) for _ in range(M))

# 직사각형 부분은 1로 바꾸기
for k in range(K):
    sj, si, ej, ei = map(int, input().split())
    if si > ei:
        si, ei = ei, si

    if sj > ej:
        sj, ej = ej, sj

    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = 1


def bfs(start_i, start_j):
    cnt = 1  # 해당 영역의 개수

    q = collections.deque()
    visited[start_i][start_j] = True
    q.append((start_i, start_j))

    while q:
        i, j = q.popleft()

        for k in range(4):  # 4방향 탐색
            ni, nj = i + dx[k], j + dy[k]

            if 0 <= ni < M and 0 <= nj < N:  # 범위
                if arr[ni][nj] == 0 and visited[ni][nj] == False:  # 방문
                    visited[ni][nj] = True
                    cnt += 1
                    q.append((ni, nj))

    return cnt


# BFS 탐색을 통해서 분리된 영역이 몇 개인지, 각 영역의 넓이 찾기
ans_cnt = 0
widths = []
visited = [[False] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and visited[i][j] == False:
            ans_cnt += 1
            widths.append(bfs(i, j))
print(ans_cnt)
print(*sorted(widths))  # 각 영역 넓이 - 오름차순으로
