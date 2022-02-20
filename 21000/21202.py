import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())
connect = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 양방향
    connect[a].append(b)
    connect[b].append(a)

island_army = [0] + list(int(input()) for _ in range(N))
visited = [False] * (N + 1)

q = []
spanning_army_cnt = island_army[1]
visited[1] = True
for idx in connect[1]:
    q.append((island_army[idx], idx))
    visited[idx] = True

heapq.heapify(q)

while q and q[0][0] < spanning_army_cnt:
    cnt, idx = heapq.heappop(q)
    # 연결된 섬들을 대결 후보에 넣기
    for i in connect[idx]:
        if visited[i] == False:
            heapq.heappush(q, (island_army[i], i))
            visited[i] = True
    spanning_army_cnt += cnt

print(spanning_army_cnt)
