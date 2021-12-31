import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 200001  # 중복 검사
history = {} # 경로(어떤 위치: 그 전 위치)


def sol():
    dq = deque()

    dq.append((N, 0, -1))

    if N == 0:  # N이 0이면 -1로는 가면 안되고, *2해도 어차피 0이니까, +1로만 갈 수 있어서 따로 해줌
        dq.append((1, 1, 0))  # 아래에서 0 < tmp 조건이 있어서 미리 먼저 빼둠
        history[1] = 0

    while dq:
        tmp, cnt, before = dq.popleft()

        if tmp == K:  # 수빈이가 동생을 찾은 경우 !
            history[tmp] = before
            return cnt

        if visited[tmp] == True:
            continue

        visited[tmp] = True  # 이제 방문했다고 체크하기
        history[tmp] = before

        if 100000 >= tmp > 0:  # N이 0인 경우는 위에서 처리. N 말고 tmp가 0이면 고려하지 않아야 함. (tmp가 0인 건 1에서 -1로 온 경우 뿐인데, 0이 갈 길은 +1뿐.. 그럼 어차피 자기가 왔던 길을 가는 거니까)
            dq.append((tmp - 1, cnt + 1, tmp))  # 앞으로 걷기
            dq.append((tmp + 1, cnt + 1, tmp))  # 뒤로 걷기
            dq.append((tmp * 2, cnt + 1, tmp))  # 순간이동


print(sol())

# 경로 - 동생 위치부터 거꾸로 찾아간다
ans = [str(K)]
tmp = K
while True:
    if history.get(tmp)==-1:
        break

    ans.append(str(history[tmp]))
    tmp = history[tmp]

print(' '.join(ans[::-1]))