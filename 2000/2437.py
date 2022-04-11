import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

now_num = 0
for i in range(N):
    if arr[i] <= now_num + 1:
        now_num += arr[i]
    else:
        break
print(now_num+1)