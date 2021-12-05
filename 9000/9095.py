import sys

input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

dp = [0] * 11
dp[1] = 1 # 1을 만드는 방법은 한 가지
dp[2] = 2 # 2를 만드는 방법은 두 가지(1+1, 2)
dp[3] = 4 # 3을 만드는 방법은 세 가지(1+1+1, 1+2, 2+1, 3)

for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 1, 2, 3을 더해서 그 수를 만드는 경우를 다 보니까

T = int(input())

for i in range(T):
    n = int(input())
    print(dp[n])
