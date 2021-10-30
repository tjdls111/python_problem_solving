import sys

input = sys.stdin.readline

dp = [False] * (10 ** 6 + 1)

# 어떤 수의 제곱이면 무조건 선공의 승리(선공이 바로 그 수 빼면 되니까)
for i in range(10 ** 3):
    dp[i * i] = True

for i in range(10 ** 6 + 1):
    if dp[i] == False:  # 후공이 승리하는 조건에다가, 제곱수 한 번 더 추가 되면 -> 선공의 승리
        j = 1
        while (j * j + i <= 10 ** 6):
            dp[i + j * j] = True
            j += 1

T = int(input())
for _ in range(T):
    N = int(input())
    if dp[N]:  # 선공 승리
        print("koosaga")
    else:  # 후공 승리
        print("cubelover")
