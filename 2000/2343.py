import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, M = MIIS()
lectures = list(MIIS())


def check(volume):  # volume 크기를 가진 블루레이 M개로 강의 모두 담을 수 있는지
    blueray_cnt = 1
    one_blueray_length = 0
    for lecture in lectures:
        if one_blueray_length + lecture > volume:
            blueray_cnt += 1
            one_blueray_length = lecture
            if blueray_cnt > M: # 블루레이가 더 필요함 = 불가능
                return False
        else:
            one_blueray_length += lecture
    if blueray_cnt > M: # 블루레이가 더 필요함 = 불가능
        return False

    return True


left = 1
right = max(lectures) * N + 1
ans = 0

while left <= right:
    mid = (left + right) // 2  # 블루레이 용량

    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(max(ans, max(lectures)))
