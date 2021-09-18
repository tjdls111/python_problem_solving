from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
visited = [False] * 200001 # 중복 검사

def sol():
    dq =deque()
    
    dq.append((N,0))
    if N == 0: # N이 0이면 -1로는 가면 안되고, *2해도 어차피 0이니까, +1로만 갈 수 있어서 따로 해줌
        dq.append((N+1,1))   # 아래에서 0 < tmp 조건이 있어서 미리 먼저 빼둠


    while dq:
        tmp, cnt = dq.popleft()

        if tmp == K: # 수빈이가 동생을 찾은 경우 ! 
            break
        if visited[tmp]==True: # 이미 검사한 거면 그냥 넘어감
            continue

        visited[tmp] = True # 이제 방문했다고 체크하기
        
        if 100000 >= tmp > 0: # N이 0인 경우는 위에서 처리. N 말고 tmp가 0이면 고려하지 않아야 함. (tmp가 0인 건 1에서 -1로 온 경우 뿐인데, 0이 갈 길은 +1뿐.. 그럼 어차피 자기가 왔던 길을 가는 거니까)
            dq.append((tmp-1, cnt+1)) # 앞으로 걷기
            dq.append((tmp+1, cnt+1)) # 뒤로 걷기
            dq.append((tmp*2, cnt+1)) # 순간이동

    return cnt

print(sol())