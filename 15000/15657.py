# 중복 조합

import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()
arr = sorted(list(MIIS()))
p = [0] * M


def dfs(depth, before):
    if depth == M:
        print(*p)
        return

    for i in range(before, N):
        p[depth] = arr[i]
        dfs(depth + 1, i)


dfs(0, 0)
