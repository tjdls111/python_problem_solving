N = int(input())
dp = ['a'] * (N + 2)  # 그 돌 개수가 될 때, 그게 가능한 경우의 수 & 그때 마지막 차례인 사람

if N==1:
    print('CY')
elif N==2:
    print('SK')
else:
    dp[1] = 'SK'
    dp[2] = 'CY'
    dp[3] = 'SK'

    for i in range(4, N + 1):
        if dp[i - 1] == 'SK':
            dp[i] = 'CY'
        else:
            dp[i] = 'SK'

    if dp[N]=='CY':
        print('SK')
    else:
        print('CY')