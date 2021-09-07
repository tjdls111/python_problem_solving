def dfs(i,j, cnt):
    global ans
    if i == 0 and j == C-1 and cnt == K: # 집 도착
        ans += 1
        return
    
    if cnt > K: # 거리 K를 넘으면
        return
    
    for k in range(4): # 상하좌우 
        ni = i + directions[k][0]
        nj = j + directions[k][1] 
        if 0<=ni <R and 0 <= nj < C: # 범위 내
            if map[ni][nj]=='.': # 방문하지 않았으면(지나간 곳 다시 가지 않음)
                map[ni][nj]='V' # 방문 체크
                dfs(ni,nj,cnt+1)
                map[ni][nj]='.' # 방문 체크 해제

R, C, K = map(int,input().split())
ans = 0
directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
map = list(list(input()) for _ in range(R))
map[R-1][0] = 'V' # 출발 지점 체크
dfs(R-1,0,1)
print(ans)
