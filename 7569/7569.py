import sys
from collections import deque

sys.stdin=open('input.txt','r')

dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]

m,n,h=map(int,input().split())
tomato_zone=list(list(list(map(int,input().split())) for _ in range(n)) for _ in range(h))

Q=deque()
days=[[[0]*m for _ in range(n)] for _ in range(h)]

for x in range(h):
    for y in range(n):
        for z in range(m):
            if tomato_zone[x][y][z]==1:
                Q.append((x,y,z))

while Q:
    tmp=Q.popleft()
    for i in range(6):
        xx=tmp[0]+dx[i]
        yy=tmp[1]+dy[i]
        zz=tmp[2]+dz[i]

        if 0<=xx<h and 0<=yy<n and 0<=zz<m and tomato_zone[xx][yy][zz]==0:
            tomato_zone[xx][yy][zz]=1
            days[xx][yy][zz]=days[tmp[0]][tmp[1]][tmp[2]]+1
            Q.append((xx,yy,zz))


def all_tomato_done(tomato_zone):
    for x in range(h):
        for y in range(n):
            for z in range(m):
                if tomato_zone[x][y][z]==0:
                    return -1
    return 0


'''print(tomato_zone)
print(days)'''

if all_tomato_done(tomato_zone)==-1:
    print(-1)
else:
    ans=0
    for x in range(h):
        for y in range(n):
            for z in range(m):
                if days[x][y][z]>ans:
                    ans=days[x][y][z]
    print(ans)
