N=int(input())
arr = list([51]*(N+1) for _ in range(N+1))


for i in range(1,N+1): # 자기 자신으로 가는 비용은 0으로 초기화
    arr[i][i] = 0 

while True:
    a, b = map(int,input().split())
    if a == -1 and b == -1:
        break
    # a <-> b 친구일 때 비용 1로
    arr[a][b] = 1
    arr[b][a] = 1


# 플로이드 와셜
for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# 연결되지 않은 부분이면 -1로
for i in range(1,N+1):
    for j in range(N+1):
        if arr[i][j] == 51:
            arr[i][j] = -1

# print(arr)

# 각 회원의 점수
score = []
for i in range(1,N+1):
    person_scores = arr[i]
    score.append(max(person_scores))
# print(score)

# 가장 낮은 점수
min_score= min(score)

# 회장 후보
candidates = []
for i in range(N):
    if min_score == score[i]:
        candidates.append(i+1)
print(min_score, len(candidates))
print(*candidates)