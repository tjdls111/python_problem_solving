import math
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().strip().split())

N, K = MIIS()

print(int(math.factorial(N) / (math.factorial(K) * math.factorial(N - K))))
