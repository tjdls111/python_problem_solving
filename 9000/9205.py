from collections import deque


# 맥주를 한번 사면, 1000m를 갈 수 있다.(20병을 꽉 채웠다고 가정.)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def sol():
    Q = deque()
    Q.append(house)
    x, y = house

    while Q:
        x, y = Q.popleft()

        # 목적지 도착 가능한지
        if manhattan_distance(x, y, festival[0], festival[1]) <= 1000:
            return 'happy'

        # 편의점 도착 가능한지
        for convi in convenience_stores:
            cx, cy = convi
            if manhattan_distance(x, y, cx, cy) <= 1000 and (cx, cy) not in visited:
                Q.append((cx, cy))
                visited.add((cx, cy))

    return 'sad'


def MIIP(): return map(int, input().split())


t = int(input())
for _ in range(t):
    # 입력받기
    n = int(input())  # 편의점 수
    house = tuple(MIIP())
    convenience_stores = []
    for i in range(n):
        x, y = tuple(MIIP())
        convenience_stores.append((x, y))
    festival = tuple(MIIP())  # 페스티벌 장소

    visited = set()  # 방문 체크
    visited.add((house[0], house[1]))  # 일단 집 방문 체크

    print(sol())
