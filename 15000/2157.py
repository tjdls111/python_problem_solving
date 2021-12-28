import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list([0] * (N + 1) for _ in range(N + 1))

# 세로: 거기에 도착할 때까지, 가로: 몇 개를 거쳐서 갔는지. 그때까지 젤 큰 기내식 점수 합을 저장
dp = list([0] * (N + 1) for _ in range(N + 1))



for i in range(K):
    a, b, c = map(int, input().split())
    if a > b: # 서 -> 동으로 가는 노선이면 어차피 안 타니까.. 받지 말기
        continue
    arr[a][b] = max(c, arr[a][b]) # 같은 도시 쌍에 항로가 여러 개 있을 수도 있는데, 제일 맛있는 기내식 점수를 보자!


# 1번 도시에서 출발하는 노선들!
for i in range(1, N+1):
    if arr[1][i]:
        dp[i][1] = max(dp[i][1], arr[1][i])


for a in range(1, N+1): # 출발점
    for b in range(1, N+1): # 도착점
        for i in range(M-1): # 도착점까지 갈 때, 몇 개 걸쳐서 갔는지.

            if arr[a][b] and dp[a][i]: # 교통 편이 있고, 그게 전꺼랑 연결된다면
                dp[b][i+1] = max(dp[a][i] + arr[a][b], dp[b][i+1])

print(max(dp[N]))