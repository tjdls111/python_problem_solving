# 중복 조합

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
com = [0] * M


def dfs(depth, before):
    if depth == M:
        print(*com)
        return

    for i in range(before, N + 1):
        com[depth] = i
        dfs(depth + 1, i)


dfs(0, 1)
