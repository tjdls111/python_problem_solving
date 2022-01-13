import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

num, target, c = MIIS()


def fpow(target, n):
    if n == 1:
        return target % c
    else:
        x = fpow(target, n // 2) % c

        if n % 2:  # 홀수
            return (((x * x) % c) * target) % c
        else:  # 짝수
            return (x * x) % c


print(fpow(num, target)%c)
