import sys
from collections import deque

n,m=map(int,input().split())
computers=[[] for _ in range(m+2)]

for _ in range(m):
    a,b=map(int,input().split())
    computers[b].append(a)
#print(computers)

l=[]

for i in range(1,n+1):
    visited=[False]*len(computers)
    q=deque([i])
    visited[i]=True
    cnt=0

    while q:
        v=q.popleft()
        cnt+=1
        for j in computers[v]:
            if not visited[j]:
                visited[j]=True
                q.append(j)
    l.append(cnt)

#print(l)
largest=max(l)
#print(largest)
for i in range(n):
    if l[i]==largest:
        print(i+1,end=' ')