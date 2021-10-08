import sys

input = sys.stdin.readline

V = int(input())
adj = [[] for _ in range(V + 1)]

# 입력받기
for i in range(V):
    tmp = list(map(int, input().split()))
    curr_v = tmp[0]
    adj_cnt = len(tmp) // 2 - 1
    for j in range(adj_cnt):
        adj_num, adj_distance = tmp[j * 2 + 1], tmp[j * 2 + 2]
        adj[curr_v].append((adj_num, adj_distance))


def make_tree(curr_idx):
    for a in adj[curr_idx]:
        num, dis = a
        if visited[num] == True:
            continue
        parent_list[num] = curr_idx
        child_list[curr_idx].append((num, dis))
        visited[num] = True
        make_tree(num)





def visit(curr_node, curr_dis):
    global max_distance, far_node
    if curr_dis > max_distance:
        max_distance = curr_dis
        far_node = curr_node

    for v, dis in child_list[curr_node]:
        if check[v]==False:
            check[v] = True
            visit(v, curr_dis + dis)



# 트리의 지름
# 1. 임의의 정점 x 잡기(x가 루트라고 가정)
x = 1
parent_list = [0] * (V + 1)
child_list = list([] for _ in range(V + 1))
visited = [False] * (V + 1)
visited[x] = True
make_tree(x)

# 2. x에서 가장 먼 정점 y(dfs로 가장 아래까지..)
max_distance = -1
far_node = -1
check=[False]*(V+1)

visit(x, 0)
y = far_node
# print(far_node, max_distance)

# 3. y에서 가장 먼 정점 z
parent_list = [0] * (V + 1)
child_list = list([] for _ in range(V + 1))
visited = [False] * (V + 1)
visited[y] = True
make_tree(y)

max_distance = -1
far_node = -1
check=[False]*(V+1)
visit(y, 0)
# print(far_node, max_distance)


# y, z 사이의 거리가 트리의 지름이다.
print(max_distance)
