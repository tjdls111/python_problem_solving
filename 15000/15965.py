import sys

input = sys.stdin.readline

MAX_PRIME = 7368788

L = [0] * MAX_PRIME # 500,000번째 소수는 7,368,787

L[1] = 1
sosu = []
# 에라토스테네스의 체 -> 소수 구하기
for i in range(2, int(MAX_PRIME ** 0.5) + 1):
    if L[i] == 0:
        for j in range(i * 2, MAX_PRIME, i):
            L[j] = 1

K = int(input())
cnt = 0

for j in range(1, MAX_PRIME):
    if L[j] == 0:
        cnt += 1
        if cnt == K:
            print(j)
            break
