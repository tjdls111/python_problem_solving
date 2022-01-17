'''
title: 그대, 그머가 되어
link: https://www.acmicpc.net/problem/14496
'''

import sys, collections
input = sys.stdin.readline
INF = int(1e9)
MIIS = lambda: map(int, input().split())

start, target = MIIS()
N, M = MIIS()

if start == target:
    print(0)
else:
    distance = [INF]*(N+1) # 출발점 start에서 다른 정점들로 갈 때의 최소 거리
    visited = [False]*(N+1)
    arr = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = MIIS()
        arr[a].append(b)
        arr[b].append(a)

    q = collections.deque()
    distance[start]=0
    q.append(start)

    while q:
        tmp = q.popleft()

        if visited[tmp]==True:
            continue
        # 거기에 연결된 정점들
        for spot in arr[tmp]:
            distance[spot] = min(distance[spot], distance[tmp]+1)
            q.append(spot)

        visited[tmp] = True

    if distance[target] == INF:
        print(-1)
    else:
        print(distance[target])