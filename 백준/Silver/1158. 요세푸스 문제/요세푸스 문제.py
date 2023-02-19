from collections import deque

N, K = map(int,input().split())

q = deque(list(k+1 for k in range(N)))
ans = []

cnt = 0
while q:
    cnt += 1

    tmp = q.popleft()

    if cnt == K:
        ans.append(tmp)
        cnt = 0
    else:
        q.append(tmp)

print('<', ', '.join(map(str,ans)),'>',sep='')