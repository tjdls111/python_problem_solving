# 중복 X. 조합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
com = [0] * M
visited = [0] * N

def dfs(depth, before):
    if depth == M:
        print(*com)
        return

    for i in range(before, N):
        if visited[i] == True: continue

        visited[i] =True
        com[depth] = arr[i]
        dfs(depth + 1, i)
        visited[i] = False


dfs(0,0)
