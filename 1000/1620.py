import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().strip().split())

N, M = MIIS()

# 저장
poketmon_dic_num = dict()
poketmon_dic_name = dict()

for i in range(1, N+1):
    name = input().strip()
    poketmon_dic_num[i] = name
    poketmon_dic_name[name] = i

# 문제 맞추기
for _ in range(M):
    tmp = input().strip()
    if tmp.isdigit(): # 숫자라면
        print(poketmon_dic_num[int(tmp)])
    else:
        print(poketmon_dic_name[tmp])