import sys
sys.setrecursionlimit(10**6)
dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,-1,1]

def DFS(i,j):
    for x in range(8):
        xx = i + dx[x]
        yy = j + dy[x]
        if 0 <= xx < h and 0 <= yy < w and island_map[xx][yy] == 1:
            island_map[xx][yy] = 0
            DFS(xx, yy)



if __name__=='__main__':
    while True:
        w,h=map(int,input().split())
        if w==0 and h==0: break
        island_map=[]
        for _ in range(h):
            island_map.append(list(map(int,input().split())))

        cnt=0
        for i in range(h):
            for j in range(w):
                #print(i,j,island_map[i][j])
                if island_map[i][j]==1:
                    cnt+=1
                    island_map[i][j]=0
                    DFS(i,j)
        print(cnt)