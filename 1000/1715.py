import sys, heapq

input = sys.stdin.readline

N = int(input())
q = list(int(input()) for _ in range(N))

heapq.heapify(q)

cnt = 0

while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a + b)
    cnt += (a + b)

print(cnt)
