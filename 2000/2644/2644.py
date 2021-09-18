import sys
from collections import deque

n=int(input())
target_one,target_two=map(int,input().split())
m=int(input())

relatives=[[]*n for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    relatives[x].append(y)
    relatives[y].append(x)
#print(relatives)

def calculate_consu():
    visited=[-1]*len(relatives)
    q=deque([target_one])
    visited[target_one]=0
    while q:
        v=q.popleft()
        #print(v)

        if v==target_two:
            return visited[target_two]
        
        for i in relatives[v]:
            if visited[i]==-1:
                visited[i]=visited[v]+1
                q.append(i)
    return -1

tmp=calculate_consu()
print(tmp)