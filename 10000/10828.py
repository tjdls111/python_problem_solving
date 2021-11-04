import sys

input = sys.stdin.readline

N = int(input())
S = [0] * (10001)
idx = -1
for i in range(N):
    command = input().strip()

    if command == "pop":
        if idx == -1:
            print(-1)
        else:
            print(S[idx])
            idx -= 1

    elif command == "size":
        print(idx + 1)

    elif command == "empty":
        if idx == -1:
            print(1)
        else:
            print(0)

    elif command == "top":
        if idx == -1:
            print(-1)
        else:
            print(S[idx])

    else:  # push
        command, num = command.split()
        idx += 1
        S[idx] = num