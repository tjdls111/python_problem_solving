# 입력받기
n = int(input())
bricks = [[]]
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append([a, b, c, i + 1])  # 밑면 넓이, 높이, 무게, 들어온 순서

# 밑면 기준으로 정렬
bricks.sort(reverse=True)
bricks.pop()  # 맨처음에 만든 빈 리스트를 빼줌.
# print(bricks)
dy = list([''] * 2 for _ in range(n))
dy[0] = [bricks[0][1], str(bricks[0][3])]  # 높이, 뭘 쌓은 건지

res = bricks[0][1]
res_idx = 0
for i in range(1, n):  # i번째가 젤 위 벽돌이라고 치고
    highest = 0  # 높이
    highest_inx = -1
    for j in range(i - 1, -1, -1):
        # 무게 체크 & 높이 체크
        if bricks[j][2] > bricks[i][2] and dy[j][0] > highest:
            highest = dy[j][0]
            highest_inx = dy[j][1]

    if highest_inx == -1:
        dy[i][1] = str(bricks[i][3])
    else:
        dy[i][1] = str(bricks[i][3]) + ' ' + str(highest_inx)

    dy[i][0] = highest + bricks[i][1]
    # print(dy)

    if dy[i][0] > res:
        res = dy[i][0]
        res_idx = i

ans = list(dy[res_idx][1].split())
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
