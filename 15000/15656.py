# 중복 순열
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

p = [0] * M


def dfs(depth):
    if depth == M:
        print(*p)
        return

    for i in range(N):
        p[depth] = arr[i]
        dfs(depth + 1)


dfs(0)
