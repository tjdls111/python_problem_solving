import sys

input = sys.stdin.readline

R, C, N = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(R))
dist = [(0, -1), (0, 1), (1, 0), (-1, 0)]

if N == 1:  # 그대로 출력
    for i in range(R):
        for j in range(C):
            print(board[i][j], end='')
        print()

# 전체 폭탄 있을 때
elif N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print('O', end='')
        print()

elif N % 4 == 3:
    # 초기 폭탄 폭발할 때 결과
    tmp_board = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                tmp_board[i][j] = '.'
                # 4방향에 폭탄 있으면 터지기
                for k in range(4):
                    ni = i + dist[k][0]
                    nj = j + dist[k][1]
                    if 0 <= ni < R and 0 <= nj < C:
                        tmp_board[ni][nj] = '.'
    for i in range(R):
        for j in range(C):
            print(tmp_board[i][j], end='')
        print()

elif N % 4 == 1:  # 나중에 설치된 폭탄 폭발
    # # 한 번 더 진행된 결과
    tmp_board = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                tmp_board[i][j] = '.'
                # 4방향에 폭탄 있으면 터지기
                for k in range(4):
                    ni = i + dist[k][0]
                    nj = j + dist[k][1]
                    if 0 <= ni < R and 0 <= nj < C:
                        tmp_board[ni][nj] = '.'

    board = tmp_board
    tmp_board = [['O'] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                tmp_board[i][j] = '.'
                # 4방향에 폭탄 있으면 터지기
                for k in range(4):
                    ni = i + dist[k][0]
                    nj = j + dist[k][1]
                    if 0 <= ni < R and 0 <= nj < C:
                        tmp_board[ni][nj] = '.'

    for i in range(R):
        for j in range(C):
            print(tmp_board[i][j], end='')
        print()
