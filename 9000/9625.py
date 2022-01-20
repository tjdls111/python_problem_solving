import sys

input = sys.stdin.readline

K = int(input())

a_dp = [0]*(K+1)
b_dp = [0]*(K+1)

a_dp[0] = 1

for i in range(1, K+1):
    a_dp[i] = b_dp[i-1]
    b_dp[i] = a_dp[i-1] + b_dp[i-1]

print(a_dp[K], b_dp[K])
