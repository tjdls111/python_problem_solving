from collections import deque
import copy

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
zone=[list(map(int,input().split())) for _ in range(n)]

start=float('inf')
finish=-float('inf')
for i in zone:
    for j in i:
        if j <start:
            start=j
        elif j>finish:
            finish=j

safe_zone=[]
for rain in range(finish):
    #print('rain= ',rain)

    Q=deque()
    cnt=0
    zone_tmp=copy.deepcopy(zone)

    for w in range(n):
        for z in range(n):
            if zone_tmp[w][z]>rain:
                cnt+=1
                #print(w,z,zone_tmp[w][z])
                zone_tmp[w][z]=0
                Q.append((w,z))

                while Q:
                    tmp=Q.popleft()
                    for r in range(4):
                        xx=tmp[0]+dx[r]
                        yy=tmp[1]+dy[r]
                        if 0<=xx<n and 0<=yy<n and zone_tmp[xx][yy]>rain:
                            #print('>>',xx,yy,zone_tmp[xx][yy])
                            zone_tmp[xx][yy]=0
                            Q.append((xx,yy))
    safe_zone.append(cnt)
#print(safe_zone)
print(max(safe_zone))



