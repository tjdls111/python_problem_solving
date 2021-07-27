n, k = map(int,input().split())

dy = [[] for _ in range(n)]
dy[0] = [1]

#print(dy)

for i in range(1,n):
    dy[i].append(1)
    
    for j in range(1, i):
        dy[i].append(dy[i-1][j-1] + dy[i-1][j])
    dy[i].append(1)

# print(dy)
print(dy[n-1][k-1])