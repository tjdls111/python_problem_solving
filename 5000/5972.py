'''
title: 택배 배송
link: https://www.acmicpc.net/problem/5972
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
MIIS = lambda: map(int, input().split())

N, M  = MIIS()
distance= [INF] * (N+1)
visited = [False] * (N+1)

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b,c = MIIS()
    arr[a].append([b, c])
    arr[b].append([a, c])

# 출발점은 헛간 1
distance[1] = 0
q = []
heapq.heappush(q, (0, 1)) # 처음 출발점에서 그 정점까지의 cost, 그 정점

while q:
    dist, idx = heapq.heappop(q) # 거리 짧은 헛간부터 보기

    if visited[idx] == True: # 그 헛간 방문 안했으면
        continue

    for spot, cost in arr[idx]: # 그 헛간과 연결된 길들을 보기
        distance[spot] = min(distance[spot], distance[idx] + cost) # 그 헛간 지나가는 것, 안 지나가는 것
        heapq.heappush(q, (distance[spot], spot))

    visited[idx] =True # 그 헛간 방문 체크

print(distance[N])