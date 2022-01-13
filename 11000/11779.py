import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

city_cnt = int(input())
bus_cnt = int(input())

graph = [[] for _ in range(city_cnt + 1)]
distance = [[INF, 0] for _ in range(city_cnt + 1)]  # 출발점부터 그 점까지 비용, 최소 비용으로 그 점에 오려면 그 전에 어디에서 오는지

for _ in range(bus_cnt):
    start, finish, cost = MIIS()
    graph[start].append((finish, cost))

start_city, target_city = MIIS()

# 다익스트라
q = []
heapq.heappush(q, (0, start_city))
distance[start_city] = [0, -1]

while q:
    dist, idx = heapq.heappop(q)
    if distance[idx][0] < dist:
        continue

    for finish_idx, cost in graph[idx]:
        now_cost = dist + cost
        if now_cost < distance[finish_idx][0]:  # 거쳐 가는 경우
            distance[finish_idx][0] = now_cost
            distance[finish_idx][1] = idx
            heapq.heappush(q, (now_cost, finish_idx))

print(distance[target_city][0])

# 지나온 경로 찾기
history = [target_city]
after_city = distance[target_city][1]
while True:
    if after_city == -1:
        break
    else:
        history.append(after_city)
    after_city = distance[after_city][1]

print(len(history))
print(' '.join(map(str, history[::-1])))
