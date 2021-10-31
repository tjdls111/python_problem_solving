# 중복 X. 조합.
# 중복되는 결과는 X.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
p = [0] * M
visited = [0] * N
res = set()


def dfs(depth, before):
    if depth == M:
        tmp = ' '.join(map(str, p[::]))
        if tmp not in res:
            print(tmp)
            res.add(tmp)
        return

    for i in range(before,N):
        if visited[i] == True: continue

        visited[i] = True
        p[depth] = arr[i]
        dfs(depth + 1, i)
        visited[i] = False


dfs(0, 0 )
