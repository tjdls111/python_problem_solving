from collections import deque
cows_way = input()

dq = deque()

cnt = 0
for i in range(len(cows_way)):
    cow_way = cows_way[i]
    if not dq: # 스택 안에 다른 소들의 경로가 없으면(겹칠 염려 X => 고려할 필요 X)
        dq.appendleft(cow_way)
    elif dq[0] == cow_way: # 소가 들어가고 나오는 점 사이에 다른 소가 없으면
        dq.popleft()
    elif cow_way in dq: # 소가 들어가고 나오는 점 사이에 다른 소가 있으면
        cnt += dq.index(cow_way) # 겹치는 만큼 더한다(소가 만난다는 것)
        dq.remove(cow_way)
    else:
        dq.appendleft(cow_way)

print(cnt)


