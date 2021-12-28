import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 모든 박스를 배로 옮길 수 없는 경우
if boxes[0] > cranes[0]:
    print(-1)

else:  # 가능한 경우
    ans = 0
    while boxes:  # 화물 박스 다 옮길 때까지
        ans += 1  # 크레인들 동시에 움직일 때 +1초
        for crane in cranes:
            for i in range(len(boxes)):
                # 그 크레인으로 그 화물 박스를 옮길 수 있나 보기
                if boxes[i] > crane :  # 못 옮기면
                    pass  # i에 1 더해지니까 다음 화물은 그 크레인으로 옮길 수 있나 보기
                else:  # 옮길 수 있으면.
                    del boxes[i]  # 그 화물 빼기
                    # 다음 크레인으로 가기 위해서 break
                    break

    print(ans)
