import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(M)]
    print(N-1)

# 스패닝 트리 (spanning tree) = 최소 연결 부분 트리:  그래프 내 모든 정점을 포함하는 트리
# 연결 그래프: 모든 꼭지점 간 경로가 존재한다고 함. (모든 연결 그래프는 스패닝 트리 가짐)
# n개의 정점이 존재하면 간선은 항상 n-1이다. (더 간선이 생기면 사이클이 존재하게 되어서 트리가 아니게 됨)
