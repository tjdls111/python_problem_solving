import sys

input = sys.stdin.readline
MIIS = lambda:map(int,input().split())

# build - segment tree 생성(루트부터 아래로 반씩 나누면서)
def min_build(arr, node, nodeleft, noderight):
    if nodeleft == noderight: # 리프 노드- 범위에 노드가 하나니까 그걸 넣으면 됨.
        min_segment_tree[node] = arr[nodeleft]
        return min_segment_tree[node]
    
    # 범위에 노드가 두 개 이상이면
    mid = int((nodeleft + noderight)/2)
    left_value = min_build(arr, node*2, nodeleft, mid) # 왼쪽 노드
    right_value = min_build(arr, node*2+1, mid+1, noderight) # 오른쪽 노드

    min_segment_tree[node] = min(left_value,right_value)
    return min_segment_tree[node]

def max_build(arr, node, nodeleft, noderight):
    if nodeleft == noderight: # 리프 노드- 범위에 노드가 하나니까 그걸 넣으면 됨.
        max_segment_tree[node] = arr[nodeleft]
        return max_segment_tree[node]
    
    # 범위에 노드가 두 개 이상이면
    mid = int((nodeleft + noderight)/2)
    left_value = max_build(arr, node*2, nodeleft, mid) # 왼쪽 노드
    right_value = max_build(arr, node*2+1, mid+1, noderight) # 오른쪽 노드

    max_segment_tree[node] = max(left_value,right_value)
    return max_segment_tree[node]



# 구간 지정 -> 최댓값 구하기
def total_max(left, right, node, nodeleft, noderight):
    if right<nodeleft or noderight < left: # 범위 아예 바깥에 있는 노드들 
        return 0  # 그냥 무시
    
    if left <= nodeleft and noderight <= right: # 노드가 범위에 완전히 포함됨.
        return max_segment_tree[node]

    # 범위가 노드에 걸친다. (쪼개져서 내려감.)
    mid = int((nodeleft + noderight)/2)
    return max(total_max(left, right, node*2, nodeleft, mid),total_max(left, right, node*2+1, mid+1, noderight))


# 구간 지정 -> 최솟값 구하기
def total_min(left, right, node, nodeleft, noderight):
    if right<nodeleft or noderight < left: # 범위 아예 바깥에 있는 노드들 
        return 1000000001  # 그냥 무시
    
    if left <= nodeleft and noderight <= right: # 노드가 범위에 완전히 포함됨.
        return min_segment_tree[node]

    # 범위가 노드에 걸친다. (쪼개져서 내려감.)
    mid = int((nodeleft + noderight)/2)
    return min(total_min(left, right, node*2, nodeleft, mid), total_min(left, right, node*2+1, mid+1, noderight))


#입력 받기
N, M = MIIS()

arr = []
for _ in range(N):
    arr.append(int(input()))

# 세그먼트 트리 만들기
min_segment_tree = [0]*(N*4 + 1)
min_build(arr, 1, 0, N-1)
max_segment_tree = [0]*(N*4 + 1)
max_build(arr, 1, 0, N-1)

# 명령 수행
for _ in range(M):
    a, b = MIIS()
    print(total_min(a-1, b-1, 1, 0, N-1), total_max(a-1, b-1, 1, 0, N-1))


