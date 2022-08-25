from collections import defaultdict
N,M =map(int,input().split())
lamps_connect_switch = defaultdict(list)
switch_connect_lamps = {}
for i in range(N):
    connect = list(map(int,input().split()))
    switch_connect_lamps[i]=connect[1:]
    for j in range(1,connect[0]+1):
        lamps_connect_switch[connect[j]].append(i + 1)

# 어느 한 스위치에 연결된 램프들은 모두 다른 스위치와 연결되어 있어야 함. -> 1
def check_connection():
    for i in range(N):
        connected_lamps = switch_connect_lamps[i]
        for lamp in connected_lamps:
            if len(lamps_connect_switch[lamp]) > 1:
                continue
            else:
                break
        else:
            return 1
    return 0

print(check_connection())