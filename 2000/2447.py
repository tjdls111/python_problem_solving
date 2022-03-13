import sys

input = sys.stdin.readline

N = int(input())


def sol(i, j, n):
    if (i // n) % 3 == 1 and (j // n) % 3 == 1:
        return ' '

    if n == 1:
        return '*'

    return sol(i, j, n // 3)


for i in range(N):
    for j in range(N):
        print(sol(i, j, N), end='')
    print()
