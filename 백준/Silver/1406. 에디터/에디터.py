import sys
from collections import deque
input  = sys.stdin.readline


cursor_left_arr = deque(list(input().strip()))
cursor_right_arr = deque()
N = int(input())

# abc
# 명령어
for i in range(N):
    command = input().split()

    if command[0] == 'L':
        if len(cursor_left_arr) > 0:
            tmp = cursor_left_arr.pop()
            cursor_right_arr.appendleft(tmp)

    elif command[0] == 'D':
        if len(cursor_right_arr) > 0 :
            tmp = cursor_right_arr.popleft()
            cursor_left_arr.append(tmp)

    elif command[0] == 'B':
        if len(cursor_left_arr) > 0:
            cursor_left_arr.pop()
    else:
       cursor_left_arr.append(command[1])

print(''.join(cursor_left_arr) + ''.join(cursor_right_arr))