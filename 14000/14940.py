import collections
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = MIIS()
arr = list(list(MIIS()) for _ in range(n))


# 출발점 찾기
def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j


start_i, start_j = find_start()

# 출발점에서 다른 곳까지 가는 거리들을 계산
visited = [[-1] * m for _ in range(n)]

q = collections.deque()
q.append((start_i, start_j))
visited[start_i][start_j] = 0

while q:
    i, j = q.popleft()

    for k in range(4):
        ni, nj = i + directions[k][0], j + directions[k][1]
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:  # 방문하지 않은 곳
            if arr[ni][nj] == 1:  # 갈 수 있는 땅이면
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
            elif arr[ni][nj] == 0: # 갈 수 없는 땅이라도 방문 체크
                visited[ni][nj] = 0

# 출력
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:  # 원래 갈 수 없는 땅인 위치는 항상 0 출력
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
