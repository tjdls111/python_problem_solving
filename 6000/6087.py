import collections
import sys

input = sys.stdin.readline
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

W, H = map(int, input().rstrip().split())
INF = H * W + 1
arr = list(input().rstrip() for _ in range(H))
visited = [[INF] * W for _ in range(H)]

# C 위치 두 개 찾기
c_index = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C':
            c_index.append((i, j))
start = c_index[0]
target = c_index[1]


def sol():
    dq = collections.deque()
    dq.append((0, -1, start[0], start[1]))  # 거울 개수, 방향, 인덱스
    visited[start[0]][start[1]] = 0  # 출발점 다시 안 오게

    while dq:
        mirror_cnt, direction, i, j = dq.popleft()

        if i == target[0] and j == target[1]:  # 정답..!
            return mirror_cnt

        if visited[i][j] < mirror_cnt:  # 더 적은 거울 수로 이미 방문했으면
            continue

        visited[i][j] = mirror_cnt  # 꺼낸 후에 방문 체크

        for k in range(4):
            ni = i + direct[k][0]
            nj = j + direct[k][1]

            # 범위, 방문 체크, 벽 X
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] != '*':

                # 직진이면
                if k == direction or direction == -1:  # direction -1은 맨 처음에 사 방향으로 가는 것
                    dq.appendleft((mirror_cnt, k, ni, nj))  # 맨 앞에 붙이기(처음으로 나오게)

                # 꺾어야 하면(거울 필요)
                else:
                    dq.append((mirror_cnt + 1, k, ni, nj))  # 맨 뒤에 붙이기 (나중에 나오도록)


print(sol())
