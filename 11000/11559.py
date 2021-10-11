import collections
import sys

input = sys.stdin.readline


# 그 위치부터 봐서 같은 색 뿌요 개수 세기
def bfs(i, j, type):
    visited = [[False] * 6 for _ in range(12)]
    cnt = 1
    q = collections.deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        ii, jj = q.popleft()
        for k in range(4):
            ni = ii + directions[k][0]
            nj = jj + directions[k][1]
            if 0 <= ni < 12 and 0 <= nj < 6 and visited[ni][nj] == False and arr[ni][nj] == type:
                cnt += 1
                q.append((ni, nj))
                visited[ni][nj] = True
    return cnt


# 터뜨리기
def boom(i, j, type):
    q = collections.deque()
    q.append((i, j))
    while q:
        ii, jj = q.popleft()
        for k in range(4):
            ni = ii + directions[k][0]
            nj = jj + directions[k][1]
            if 0 <= ni < 12 and 0 <= nj < 6 and arr[ni][nj] == type:
                q.append((ni, nj))
                # 터뜨리기(점으로 만들기)
                arr[ni][nj] = '.'


# 뿌요 아래로 이동시키기
def move():
    for j in range(6):
        blank = 11
        bbuyo = 11
        while blank >= 0  and bbuyo >= 0:
            if arr[blank][j] == '.':
                while bbuyo >= 0 and arr[bbuyo][j] == '.':
                    bbuyo -= 1
                if blank > bbuyo and bbuyo != -1:
                    arr[blank][j], arr[bbuyo][j] = arr[bbuyo][j], arr[blank][j]
                else:
                    bbuyo -= 1
            else:
                blank -= 1



directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arr = list(list(input().strip()) for _ in range(12))
ans = 0

# 쭉 보면서 터질 그룹들이 있는지 판단하기
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                cnt = bfs(i, j, arr[i][j])
                if cnt >= 4:  # 터뜨릴 수 있으면 터뜨리기
                    boom(i, j, arr[i][j])
                    flag = True


    move()
    if flag == False:
        break
    elif flag == True:
        ans += 1

print(ans)
