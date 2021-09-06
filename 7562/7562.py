import collections
T = int(input())

# 한번 이동에 가는 경우들
directions = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
for _ in range(T):
    l = int(input()) # 체스판 한 변의 길이
    start_i, start_j = map(int,input().split())
    final_i, final_j = map(int,input().split())
    check = list([0]*l for _ in range(l)) # 거기까지 출발점에서 몇 번 이동했는지 체크

    D = collections.deque()
    D.append((start_i,start_j))
    ans = 0
    while D:
        i, j = D.popleft()
        if i == final_i and j == final_j: # 목표점에 도달했으면
            break
        
        for k in range(8):
            ni = i + directions[k][0]
            nj = j +directions[k][1]
            if 0<=ni <l and 0<=nj < l and check[ni][nj]==0 : # 범위 내이고 방문하지 않았으면
                check[ni][nj]= check[i][j] + 1 # 출발점에서 몇번만에 이동했는지 체크
                D.append((ni,nj))
    print(check[final_i][final_j])