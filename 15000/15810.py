import sys

input = sys.stdin.readline

MIISS = lambda : map(int,input().strip().split())

N,M = MIISS()
arr = list(MIISS())

def balloon_count(minute):
    res = 0
    for people in arr:
        res += (minute // people)
    return res


left = 1
right = 1000000000001

ans = 0
while left <= right:
    mid = (left + right) // 2

    if balloon_count(mid) >= M:
       ans = mid
       right = mid - 1
    else:
        left = mid + 1

print(ans)
