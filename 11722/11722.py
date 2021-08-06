n = int(input())
l = list(map(int,input().split()))
l.insert(0,0)
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i):
        if l[i] < l[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp)+1)
        

