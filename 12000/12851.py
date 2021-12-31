import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 200001  # 중복 검사


def sol():
    find_method_cnt = 0
    short_time = -1

    dq = deque()

    dq.append((N, 0))
    if N == 0:  # N이 0이면 -1로는 가면 안되고, *2해도 어차피 0이니까, +1로만 갈 수 있어서 따로 해줌
        dq.append((N + 1, 1))  # 아래에서 0 < tmp 조건이 있어서 미리 먼저 빼둠

    while dq:
        tmp, cnt = dq.popleft()

        visited[tmp] = True  # 이제 방문했다고 체크하기

        if tmp == K:  # 수빈이가 동생을 찾은 경우 !
            if short_time == -1:  # 맨 처음 찾은 것이면
                short_time = cnt

            if short_time == cnt:  # 최소 시간으로 찾았으면
                find_method_cnt += 1
                continue

            else:  # 더 이상 봐도 찾는 시간 더 오래 걸리는 것만 나올 것이니까.
                break

        if 100000 >= tmp > 0:  # N이 0인 경우는 위에서 처리. N 말고 tmp가 0이면 고려하지 않아야 함. (tmp가 0인 건 1에서 -1로 온 경우 뿐인데, 0이 갈 길은 +1뿐.. 그럼 어차피 자기가 왔던 길을 가는 거니까)
            if visited[tmp - 1] == False:
                dq.append((tmp - 1, cnt + 1))  # 앞으로 걷기
            if visited[tmp + 1] == False:
                dq.append((tmp + 1, cnt + 1))  # 뒤로 걷기
            if visited[tmp * 2] == False:
                dq.append((tmp * 2, cnt + 1))  # 순간이동

    return short_time, find_method_cnt


fast_time, find_cnt = sol()
print(fast_time)
print(find_cnt)
