import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
L = list(list(input()) for _ in range(N))

ans = []
for i in range(N - 7):
    for j in range(M - 7):  # 8*8 칸 고르기
        count = 0
        # 맨 윗 왼쪽이 검정인 경우
        for ii in range(i, i + 8):
            for jj in range(j, j + 8):
                if (ii) % 2 == 0 and (jj) % 2 == 0:
                    if not L[ii][jj] == 'B':
                        count += 1
                elif (ii) % 2 == 0 and (jj) % 2 == 1:
                    if not L[ii][jj] == 'W':
                        count += 1
                elif (ii) % 2 == 1 and (jj) % 2 == 0:
                    if not L[ii][jj] == 'W':
                        count += 1
                elif (ii) % 2 == 1 and (jj) % 2 == 1:
                    if not L[ii][jj] == 'B':
                        count += 1

        ans.append(count)

        count = 0
        # 맨 위 왼쪽이 하양인 경우
        for ii in range(i, i + 8):
            for jj in range(j, j + 8):
                if (ii) % 2 == 0 and (jj) % 2 == 0:
                    if not L[ii][jj] == 'W':
                        count += 1
                elif (ii) % 2 == 0 and (jj) % 2 == 1:
                    if not L[ii][jj] == 'B':
                        count += 1
                elif (ii) % 2 == 1 and (jj) % 2 == 0:
                    if not L[ii][jj] == 'B':
                        count += 1
                elif (ii) % 2 == 1 and (jj) % 2 == 1:
                    if not L[ii][jj] == 'W':
                        count += 1

        ans.append(count)

# print(ans)
print(min(ans))
