x, y = map(int, input().split())
z = int(y*100 / x)
ans = 0

if z >= 99:
    ans = -1
else:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2 # 얼마나 게임 더할지
        new = int((y + mid)*100 / (x + mid)) # 그때 승률

        if z < new: # 승률이 바뀌었으면
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
print(ans)
