# Union-Find 알고리즘
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_group(num):
    # 어느 집합에 속하는지 찾기
    if group[num] == num:
        return num
    group[num] = find_group(group[num])
    return group[num]


def unionGroup(a, b):
    # 두 집합을 합치기
    a = find_group(a)
    b = find_group(b)

    if a < b:  # 작은 집합 번호로 합치기
        group[b] = a
    else:
        group[a] = b


def checkSameGroup(a, b):
    a = find_group(a)
    b = find_group(b)
    if a == b:
        return 'YES'
    else:
        return 'NO'


n, m = map(int, input().split())

group = [0] * (n + 1)
for i in range(n + 1):
    # 일단 자기 자신만 포함한 집합 만들기
    group[i] = i

for i in range(m):
    # 연산 처리
    order, a, b = map(int, input().split())
    if order == 0:  # 합집합
        unionGroup(a, b)
    elif order == 1:  # 같은 집합에 포함되었는지 확인
        print(checkSameGroup(a, b))
