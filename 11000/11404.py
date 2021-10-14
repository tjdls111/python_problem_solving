import sys

input = sys.stdin.readline


def FW():
    for k in range(1, N + 1):  # 경유지
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


INF = 100 * 100000 + 1

N = int(input())
M = int(input())

distance = [[INF] * (N + 1) for _ in range(N + 1)]

# 초기화(자기 자신으로 갈 때 0)
for i in range(1, N + 1):
    distance[i][i] = 0

for _ in range(M):
    s, e, cost = map(int, input().strip().split())
    distance[s][e] = min(distance[s][e], cost)

FW()

for i in range(1, N + 1):
    for j in range(1, N + 1):
        tmp = distance[i][j]
        if tmp == 10000001:
            tmp = 0
        print(tmp, end=' ')
    print()
