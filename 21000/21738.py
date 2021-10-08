import collections
import sys

input = sys.stdin.readline

N, S, P = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


# P부터 가장 가까운 지지대 얼음 2개 찾자!
def bfs():
    jijidae = 0
    connect = 0
    q = collections.deque()
    q.append((P, 0))  # 펭귄 있는 곳부터 시작(얼음 번호, 거리)

    while q:
        start, step = q.popleft()
        if visited[start] == True:  # 방문 했으면 가지 말기
            continue
        visited[start] = True  # 방문 체크

        if 1 <= start <= S:  # 지지대라면
            jijidae += 1
            connect += step  # 지지대까지 연결된 길만큼 connect에 더하기

        if jijidae == 2:  # 지지대가 2개 되었으면(펭귄 최소한 안 떨어짐)
            return connect

        for v in adj[start]:  # 거기 연결된 얼음들
            q.append((v, step + 1))

must = bfs()
print(N - must - 1)  # 최대로 깰 수 있는 얼음은 전체 - 지지대 역할 하는 얼음 & 펭귄-지지대 연결하는 얼음 - 펭귄 서있는 얼음
