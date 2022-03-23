import sys

input = sys.stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))


def sol(n):
    global arr
    if n == 1:
        return arr[0][0]

    tmp_arr = [[0] * (n // 2) for _ in range(n // 2)]

    for i in range(n // 2):
        for j in range(n // 2):
            # 2X2 칸 중에 두 번째로 큰 수 구하기
            tmp = []
            for ii in range(i * 2, i * 2 + 2):
                for jj in range(j * 2, j * 2 + 2):
                    tmp.append(arr[ii][jj])
            tmp.sort()
            tmp_arr[i][j] = tmp[2]
    arr = tmp_arr
    return sol(n // 2)


print(sol(N))
