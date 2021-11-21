import sys

input = sys.stdin.readline
MIISS = lambda : map(int,input().strip().split())
T = int(input())

factorial = [0] * 31
factorial[1] = 1

# 팩토리얼 구해두기
for i in range(2, 31):
    factorial[i] = i * (factorial[i-1])

for t in range(T):
    N, M = MIISS()

    if N == M:
        print(1)

    else:
        # M 개 중 N개를 선택- 조합
        print(factorial[M]//((factorial[N])*(factorial[M-N])))