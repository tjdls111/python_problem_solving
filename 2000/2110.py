import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = list(int(input()) for _ in range(N))
houses.sort()


def check_wifi_cnt(mid):
    """
    공유기 간격을 최대 mid로 했을 때, 필요한 공유기 개수
    """
    cnt = 0
    before_wifi_idx = houses[0]
    for i in range(1, N):
        if (houses[i] - before_wifi_idx) >= mid:
            cnt += 1  # 와이파이 설치
            before_wifi_idx = houses[i]

    return (cnt + 1)


left = 0
right = houses[N - 1]

cnt = 0  # 공유기 간 거리 제한
ans = 0
while left <= right:
    mid = (left + right) // 2  # 가장 인접한 두 공유기 사이의 최대 거리- 이것보다는 멀어야..
    tmp_cnt = check_wifi_cnt(mid)

    if tmp_cnt >= C:  # 공유기가 존재하는 것보다 많이 필요하면
        left = mid + 1  # 가장 인접한 두 공유기 사이의 최대 거리 넓히기
        ans = max(ans, mid) # 정답될 수 있음

    else:  # 공유기가 충분하면
        right = mid - 1  # 가장 인접한 두 공유기 사이의 최대 거리 줄이기

# 가장 인접한 두 공유기 사이의 최대 거리 구하기
print(ans)
