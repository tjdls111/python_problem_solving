N = int(input()) # 노드의 개수
tree = list([0] * 2 for _ in range(N + 1))  # 왼족 자식, 오른쪽 자식

def pre_order(node):
    if node:
        print(chr(node+64), end='')  # 할 일
        pre_order(tree[node][0])  # 왼쪽 자식
        pre_order(tree[node][1])  # 오른쪽 자식


def mid_order(node):
    if node:
        mid_order(tree[node][0])  # 왼쪽 자식
        print(chr(node+64), end='')  # 할 일
        mid_order(tree[node][1])  # 오른쪽 자식


def rear_order(node):
    if node:
        rear_order(tree[node][0])  # 왼쪽 자식
        rear_order(tree[node][1])  # 오른쪽 자식
        print(chr(node+64), end='')  # 할 일

for i in range(N):
    temp = list(input().split())
    p = ord(temp[0]) - 64
    c1 = ord(temp[1]) - 64
    c2 = ord(temp[2]) - 64

    if c1 == -18 and c2 != -18: # 첫번째 자식은 없고, 두번째 자식이 있으면
        tree[p][0] = 0
        tree[p][1] = c2

    elif c1 != -18 and c2 == -18: # 첫번째 자식은 있고, 두번째 자식만 없으면
        tree[p][0] = c1
        tree[p][1] = 0
    
    elif c1 == -18 and c2 == -18: # 두 자식 다 없으면
        tree[p][0] = 0
        tree[p][1] = 0

    else:
        tree[p][0] = c1
        tree[p][1] = c2

pre_order(1)
print()
mid_order(1)
print()
rear_order(1)