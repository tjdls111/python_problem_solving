from collections import deque
import sys

input = sys.stdin.readline

# 입력 받아서 양쪽으로 연결
n,m=map(int,input().split())
connect=[[]*n for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)


dq=deque()
chk=[0]*(n+1)

ans=0

for i in connect:
    if not i: # 간선 정보가 없는 노드들은 연결이 전혀 안되어있으니 무조건 ans에 1 더하기
        ans += 1

    if i: # 1개 이상과 연결된 노드들의 경우
        if chk[i[0]]==0: # 아직 정점에 방문하지 않았으면(전에 것들과는 연결되지 않은 곳)
            dq.append(i[0]) # 큐에 넣고
            ans+=1          # ans에 1 더하고
            chk[i[0]]=1     # 그곳 방문했다고 체크
        
        while dq: # 위 정점에 연결된 정점들 모두 방문하고, 방문했다고 체크하기
            tmp=dq.popleft()
            for k in connect[tmp]:
                if chk[k]==0:
                    dq.append(k)
                    chk[k]=1

print(ans-1) # connect[0]은 의미 없는데, 인덱스 편하게 쓰려고 만든 거라서
  