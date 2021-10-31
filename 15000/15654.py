# 중복 X. 순열
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
com = [0] * M
visited = [0] * N

def dfs(depth):
    if depth == M:
        print(*com)
        return

    for i in range(N):
        if visited[i] == True: continue

        visited[i] =True
        com[depth] = arr[i]
        dfs(depth + 1)
        visited[i] = False


dfs(0)
