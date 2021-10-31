# 중복 순열
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
com = [0] * M


def dfs(depth):
    if depth == M:
        print(*com)
        return

    for i in range(1, N + 1):
        com[depth] = i
        dfs(depth + 1)


dfs(0)
