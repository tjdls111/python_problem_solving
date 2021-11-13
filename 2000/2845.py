import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

L, P = MIIS()
sanggun_cnt = L * P

papers_cnt = list(MIIS())
ans = list(map(lambda x: x - sanggun_cnt , papers_cnt))
print(*ans)
