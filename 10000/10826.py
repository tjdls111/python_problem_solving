import sys

input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

n = int(input())
if n >= 2:
    fibo = [0] * (n+1)

    fibo[1] = 1

    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]

    print(fibo[n])
elif n == 1:
    print(1)
elif n == 0:
    print(0)