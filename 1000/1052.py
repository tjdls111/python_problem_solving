import sys

input = sys.stdin.readline

N, K = map(int, input().split())

n = N
final_water_cnt = 0

while bin(n).count('1') > K:  # 물병이 K개 이하가 될 때까지
    tmp = bin(n)
    # 최소 물 양 구하기 -> 그만큼 물 구입하기
    # 물을 합치기 (젤 낮은 자릿수에서 2의 배수였던 것을 그 다음 자릿수로 올림)
    idx = len(tmp) - tmp.rfind('1') - 1

    final_water_cnt += (1 << idx)

    n = n + (1 << idx)

print(final_water_cnt)
