import sys, math

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

memo = [0] * 10001
idx = 1
for i in range(1, 10001):
    if memo[i]:
        continue
    else:
        now = idx + idx*idx
        after = min((idx+1) + (idx+1)*(idx+1), 10001)
        for j in range(now, after):
            memo[j] = idx
        idx += 1

T = int(input())
for _ in range(T):
    d = int(input())
    print(memo[d])
