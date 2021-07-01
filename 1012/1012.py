import sys
sys.setrecursionlimit(10**6)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    for p in range(4):
        xx = x + dx[p]
        yy = y + dy[p]

        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
            board[xx][yy] = 0
            DFS(xx, yy)


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        m,n,k=map(int,input().split())
        board=[[0]*m for _ in range(n)]

        for _ in range(k):
            x,y=map(int,input().split())
            board[y][x]=1

        '''for x in board:
            print(x)'''

        cnt=0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    cnt+=1
                    board[i][j] = 0
                    DFS(i, j)
        print(cnt)
