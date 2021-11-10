import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(int(input()) for _ in range(N))

if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1] + arr[2])
else:
    dp = [0] * (N + 2)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    # 1칸 전(그 전엔 무조건 3칸 전)에서 왔는지, 2칸 전에서 왔는지
    for i in range(3, N + 1):
        dp[i] = max(arr[i - 1] + dp[i - 3], dp[i - 2]) + arr[i]

    print(dp[N])
