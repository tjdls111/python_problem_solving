import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

n = int(input())
arr = list(int(input()) for _ in range(n))  # 입력된 수얼

ans = []

stack = []
idx = 0  # 입력된 수열 어디까지 만들었는지
for i in range(1, n+1):
    stack.append(i)  # 스택에 넣는다
    ans.append('+')

    while stack:
        if stack[-1] == arr[idx]:
            stack.pop()  # 스택에서 뺀다
            ans.append('-')
            idx += 1 # 입력된 수열 일부를 만들었으니 idx 하나 증가
        else:
            break

# 답이 있으면
if idx == n:
    for a in ans:
        print(a)

else: # 답 없으면
    print('NO')