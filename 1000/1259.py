import sys

input = sys.stdin.readline

# MIIS = lambda: map(int, input().strip().split())


while True:
    tmp = input().strip()
    if tmp == '0':
        break

    if tmp == tmp[::-1]:
        print('yes')
    else:
        print('no')