A, B = map(int,input().split())
C, D = map(int,input().split())

# 첫번째 바구니에 사과, 두번째에 오렌지 담는 경우
first_move_cnt = (C+B)

# 첫번째에 오렌지, 두번째에 사과 담는 경우
second_move_cnt = (D+A)

print(min(first_move_cnt, second_move_cnt))