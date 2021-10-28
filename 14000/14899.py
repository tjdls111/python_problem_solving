import sys
from itertools import combinations, permutations

input = sys.stdin.readline

# 입력 받기
n = int(input())
board = []
for _ in range(n):
    board.append(tuple(map(int, input().split())))

# 한 팀에 가능한 조합 구하기
A = list(combinations(range(n), n // 2))
# print(a)

# 각각 경우에서 팀 능력치 차이 구하기
smallest = 987654321
for i in range(len(A)):
    a = A[i]
    a_total = 0

    b = set(range(n)) - set(a)
    a = list(a)
    b = list(b)
    b_total = 0

    # print('a, b:', a,b)

    for j in range(len(a)):
        for k in range(j + 1, len(a)):
            a_total += board[a[j]][a[k]]
            a_total += board[a[k]][a[j]]
            # print('a[j], a[k]:', a[j],a[k])
            # print(board[a[j]][a[k]])

    for j in range(len(b)):
        for k in range(j + 1, len(b)):
            b_total += board[b[j]][b[k]]
            b_total += board[b[k]][b[j]]
            # print('b[j], b[k]:', b[j],b[k])
            # print(board[b[j]][b[k]])

    smallest = min(smallest, abs(a_total - b_total))
    # print(a_total, b_total)
    if smallest == 0:
        break

# 팀 능력치 차이가 최소인 경우를 출력하기
print(smallest)