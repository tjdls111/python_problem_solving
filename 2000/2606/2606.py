import sys
from collections import deque

n=int(input())
m=int(input())

computers=[[]*n for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    computers[x].append(y)
    computers[y].append(x)

visited=[False]*len(computers)

q=deque([1])

visited[1]=True
cnt=0
while q:
    v=q.popleft()
    cnt+=1
    for i in computers[v]:
        if not visited[i]:
            visited[i]=True
            q.append(i)
print(cnt-1)