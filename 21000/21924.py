import sys

input = sys.stdin.readline


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    parent[find_parent(y)] = find_parent(x)


def kruskal():
    cnt = 0
    cost = 0

    for s, e, c in vertex:
        if find_parent(s) == find_parent(e):
            continue

        union(s, e)
        cnt += 1
        cost += c
        if cnt == N-1:
            return cost

    return -1

N, M = map(int, input().split())

parent = list(range(N + 1))

vertex = []

for _ in range(M):
    s, e, c = map(int, input().split())
    vertex.append((s, e, c))

# 모든 건물을 연결하는 도로를 만드는 비용 (같은 쌍 건물 연결하는 두 도로는 안 주어짐)
total = sum(x[2] for x in vertex)

# 비용 적게 드는 순서대로 정렬
vertex.sort(key=lambda x: x[2])

# 크루스칼로 최소 비용 신장 트리일 때 비용 구하기
ans = kruskal()
if ans == -1:
    print(-1)
else:
    print(total - ans)
