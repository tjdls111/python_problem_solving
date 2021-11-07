import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


# 순서도 중요- 순열

def dfs(depth: int, before: int, history: str):
    if depth == 6:  # 6개 다 선택한 경우
        print(history)
        return

    for i in range(before + 1, k):  # 중복은 안되니까, 전에 뽑은 것 이후로 보기
        dfs(depth + 1, i, history + str(S[i]) + ' ')


while True:
    tmp = list(MIIS())
    if tmp[0] == 0:  # 입력의 마지막 줄
        break

    k = tmp[0]
    S = tmp[1:]

    dfs(0, -1, '')
    print()
