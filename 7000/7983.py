import sys

input = sys.stdin.readline

n = int(input())
day = []
for i in range(n):
    a, b = map(int, input().split())
    day.append((b - a + 1, a, b))  # 이날에는 꼭 시작해야 하는 날, 과제 할 때 걸리는 일수, 이때까지는 꼭 끝내야 하는 날

day.sort(key=lambda x: (-x[2], -x[1])) # 꼭 끝내야 하는 일 기준으로 내림차순 정렬

now = day[0][0] # 첫번째 과제를 꼭 시작해야 하는 날

for i in range(1, n):
    must_start, need, must_finish = day[i]
    if now > (must_finish): # 최대한 버티다가 시작
        now = must_start
    else: # 최대한 버티다가 시작할 순 X. 좀 더 일찍 시작
        now = now - need

print(now - 1)
