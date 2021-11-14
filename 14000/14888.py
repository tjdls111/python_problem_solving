import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

min_val = 1000000001
max_val = -1000000001

N = int(input())
nums = list(MIIS())
operators_cnt = list(MIIS())

operators= dict()
operators[0] = '+'
operators[1] = '-'
operators[2] = '*'
operators[3] = '//'

def dfs(depth:int, curr_total:int):
    global min_val, max_val
    if depth == N-1:
        min_val = min(min_val, curr_total)
        max_val = max(max_val, curr_total)
        return

    for i in range(4): # 사칙 연산
        if operators_cnt[i] == 0:
            continue

        operators_cnt[i] -= 1
        if i ==3 and curr_total < 0: # 음수를 양수로 나눌 때
            tmp = (eval(str(-curr_total) + operators[i] + str(nums[depth + 1])))*(-1)
        else:
            tmp = eval(str(curr_total) + operators[i] + str(nums[depth + 1]))

        dfs(depth+1, tmp)
        operators_cnt[i] += 1

dfs(0,nums[0])
print(max_val)
print(min_val)