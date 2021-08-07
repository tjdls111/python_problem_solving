n = int(input())
l = list(map(int,input().split()))
l.insert(0,0)
dy = [0]*(n+1) # 각각 인덱스를 넣는다고 생각했을 때, 가장 큰 증가 부분 수열의 합

for i in range(n+1):
    dy[i] = l[i]  
    for j in range(i+1):
        if l[i] > l[j]:
            dy[i] = max(dy[i], dy[j]+l[i])
# print(dy, l)
print(max(dy))