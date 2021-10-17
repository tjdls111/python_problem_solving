import sys, collections
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

ans = collections.deque()

for i in range(1, n+1):
    target_num = i
    skill_type = arr[n-i]

    if skill_type == 1:
        ans.appendleft(target_num)
    elif skill_type == 3:
        ans.append(target_num)
    elif skill_type == 2:
        tmp = ans.popleft()
        ans.appendleft(target_num)
        ans.appendleft(tmp)

print(*ans)




