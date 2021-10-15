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
    return cost


N = int(input())
M = int(input())

parent = list(range(N + 1))

vertex = []

# 인접 리스트
for _ in range(M):
    s, e, c = map(int, input().split())

    vertex.append((s, e, c))

# 비용 적게 드는 순서대로 정렬
vertex.sort(key=lambda x: x[2])
print(kruskal())
