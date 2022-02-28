import sys, heapq

input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
else:
    lecture_requests = list(tuple(map(int, input().split())) for _ in range(N))
    # 일자, 요금 큰 순서대로 정렬
    lecture_requests.sort(reverse=True, key=lambda x: (x[1], x[0]))
    print(lecture_requests)
    can_go_lectures = []
    ans = 0  # 최대 벌 수 있는 돈
    which_day = lecture_requests[0][1]  # 최대 일자

    for i in range(N):
        price, day = lecture_requests[i]
        if which_day == day:
            heapq.heappush(can_go_lectures, -1 * price)

        else:
            # 그 이전 날짜들 각각 -> 강연해서 벌 수 있는 돈 중에 젤 많이 주는 곳으로 가기!
            days = which_day - day
            while can_go_lectures and days:
                max_price = -1 * heapq.heappop(can_go_lectures)
                ans += max_price
                days -= 1

            which_day = day
            heapq.heappush(can_go_lectures, -1 * price)

    # 남은 날에 순회 강연하기
    for i in range(which_day, 0, -1):
        max_price = -1 * heapq.heappop(can_go_lectures)
        ans += max_price

    print(ans)
