import heapq as hq
import sys

input= sys.stdin.readline

N = int(input())
a = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if len(a) == 0:
            print(0)
        else:
            tmp = -hq.heappop(a)
            print(tmp)
    else:
        hq.heappush(a, -n)
