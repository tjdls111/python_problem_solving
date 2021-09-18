N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

ans = 0
the_money_left = K
for i in range(N):
    temp = the_money_left // coins[i]
    the_money_left -= coins[i] * temp
    ans += temp
print(ans)
