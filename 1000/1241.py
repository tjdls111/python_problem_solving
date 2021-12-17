import sys

input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))

max_int = max(arr)+1
origin_cnt = [0] * (max_int)
check = [0] * (max_int)
visited = [False] * max_int
for num in arr:
    origin_cnt[num] += 1

# 해당 수의 약수들의 개수 더하기
for i in range(N):
    tmp = arr[i]

    if visited[tmp]:  # 이미 그 수 탐색했다면
        continue

    else:  # 그 수 탐색한 적 없으면
        for j in range(tmp, max_int, tmp): # tmp가 j의 약수이면
            check[j] += origin_cnt[tmp]

    visited[tmp] = True


# 정답 출력
for num in arr:
    print(check[num] + - 1)  # 처음에 자기 자신 하나 추가되니까 1을 빼줌
