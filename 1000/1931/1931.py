# 입력 받기
import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int,input().split())
    meetings.append((end, start))


cnt = 0 # 회의 개수

# 일찍 끝나는 회의를 하게 하면, 그만큼 더 많은 회의를 개최할 수 있다.
meetings.sort()
# print(meetings)

meeting_end = 0
for e, s in meetings:
    if s >= meeting_end: # 어떤 회의의 시작 시각이 그 전 회의 끝나는 시각보다 이후이거나 같으면
        cnt += 1
        meeting_end = e
print(cnt)

