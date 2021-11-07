import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 ** 20 + 1)
MIIS = lambda: map(int, input().split())

N, S = MIIS()
arr = list(MIIS())
arr.sort()

cnt = 0


def dfs(depth: int, history: bool, total: int):
    global cnt

    if depth == N:  # 끝까지 다 봤고
        if history and total == S:  # 크기가 양수이고, 그 수열의 원소를 다 더한 값이 S가 되었으면
            cnt += 1
        return

    dfs(depth + 1, True, total + arr[depth])  # 포함
    dfs(depth + 1, history, total)  # 포함 X


dfs(0, False, 0)
print(cnt)
