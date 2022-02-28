import sys, heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    slimes = list(map(int, input().split()))
    heapq.heapify(slimes)

    price = 1
    while len(slimes) > 1:  # 슬라임이 2개 이상일 때
        a = heapq.heappop(slimes)
        b = heapq.heappop(slimes)
        power = (a * b)

        price *= power
        heapq.heappush(slimes, power)
    print(price % 1_000_000_007)