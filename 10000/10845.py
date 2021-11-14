import sys

input = sys.stdin.readline

N = int(input())
Q = [0] * 10001 # 가장 많이 들어가도 10000
top, bottom = 0, 0 # 큐에서 다음 넣을 위치, 큐 가장 앞에 있는 것(뺄 위치)
for i in range(N):
    command = input().strip()

    if command=='pop':
        if top == bottom: print(-1)
        else:
            print(Q[bottom])
            bottom += 1
    elif command=='size':
        print(top-bottom)
    elif command=='empty':
        if top == bottom:
            print(1)
        else:
            print(0)
    elif command=='front':
        if top == bottom:
            print(-1)
        else:
            print(Q[bottom])
    elif command=='back':
        if top==bottom:
            print(-1)
        else:
            print(Q[top-1])
    else: # push
        _, num = command.split()
        Q[top] = num
        top += 1
