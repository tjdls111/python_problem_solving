import collections
import sys

input = sys.stdin.readline


def bfs():
    q = collections.deque()
    q.append(1)  # 시작 정점 1
    visited[1] = 1

    while q:
        x = q.popleft()
        for y in abj[x]:
            if visited[y] != 0: continue
            visited[y] = visited[x] + 1
            children[x].append(y)
            q.append(y)

N = int(input())
abj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    abj[a].append(b)
    abj[b].append(a)

children = collections.defaultdict(list)
visited = [0] * (N + 1)

res = list(map(int, input().split()))

if res[0] != 1:  # 시작 정점이 1이 아니면
    print(0)
else:
    bfs()

    q = collections.deque()
    q.append(1)
    idx = 1

    while q:
        tmp = q.popleft()

        a = set(children[tmp])

        len_a = len(a)
        b = res[idx:idx + len_a]
        q.extend(b)
        b= set(b)
        idx += len_a

        if a != b:
            print(0)
            break
    else:
        print(1)
