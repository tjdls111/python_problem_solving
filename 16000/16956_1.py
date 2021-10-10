import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = list(list(input()) for _ in range(R))

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cnt = 0

# 모든 늑대를 쭉 보면서 체크
def sol():
    for ii in range(R):
        for jj in range(C):
            if arr[ii][jj] == 'W':  # 늑대
                # 바로 사방에 양이 있으면 => 0 출력
                for k in range(4):
                    ni = ii + directions[k][0]
                    nj = jj + directions[k][1]

                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 'S':
                        return False
            elif arr[ii][jj] == 'S':
                for k in range(4):
                    ni = ii + directions[k][0]
                    nj = jj + directions[k][1]

                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == '.':
                        arr[ni][nj] = 'D'
    return True

ans = sol()
if ans == False:
    print(0)
else:
    print(1)
    for a in arr:
        print(''.join(a).strip())