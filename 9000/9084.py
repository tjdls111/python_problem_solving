# import collections
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())
# directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


T=int(input())
for _ in range(T):
    N = int(input())
    coins= list(MIIS())
    target = int(input())

    dp = [0] * (target + 1)
    dp[0] =1

    # 각 동전보기
    for i in range(N):
        coin = coins[i]
        for j in range(coin, target+1): # 그 동전으로 다른 돈 만들 수 있을 때
            dp[j] += (dp[j-coin])


    print(dp[target])
