import collections
import sys

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)

distance = [987654321] * (N + 1)
visited = [False] * (N + 1)


def dijk(start):
    q = collections.deque()
    q.append(start)
    distance[start] = 0
    visited[start]=True

    while q: # 모든 노드 간 거리는 다 1. 시작점과 가까운 곳일 수록 거리도 가까운 거니까 그냥 deque으로 함.
        start = q.popleft()
        for node in adj[start]:
            if visited[node] == False:
                visited[node] = True
                q.append(node)
                distance[node] = min(distance[node], distance[start] + 1)


dijk(X)

# 최단 거리가 K인 도시 찾기 -> 오름차순 출력
flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        flag = True

if flag == False:
    print(-1)
