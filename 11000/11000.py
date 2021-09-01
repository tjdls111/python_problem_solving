import heapq
import sys

input = sys.stdin.readline

N = int(input())

lectures = []

max_lecture_one_time = 1

for _ in range(N):
    start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()

Q = []
heapq.heappush(Q, (lectures[0][1], lectures[0][0]))  # 끝나는 시각, 시작하는 시각
lecture_one_time = 1

for i in range(1, N):  # 하나씩 쭉 보기
    fast_finish = heapq.heappop(Q)  # 가장 빨리 끝나는 수업
    if lectures[i][0] < fast_finish[0]:  # 가장 빨리 끝나는 수업이 끝나는 시각보다, 이번에 시작하는 수업이 더 빨리 시작하면
        lecture_one_time += 1  # 강의실 하나 더 필요함
        max_lecture_one_time = max(max_lecture_one_time, lecture_one_time)  # 항상 갱신
        heapq.heappush(Q, fast_finish)  # 가장 빨리 끝나는 수업이, 아직 안 끝났으니 더해줌
        heapq.heappush(Q, (lectures[i][1], lectures[i][0]))  # 이번 수업 시간표 추가
    else:  # 가장 빨리 끝나는 수업이, 이번에 시작하는 수업보다 빨리 끝나면
        # lecture_one_time -= 1
        heapq.heappush(Q, (lectures[i][1], lectures[i][0]))  # 이번 수업 시간표 추가
print(max_lecture_one_time)
