N = int(input())
M = int(input())

abj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    abj[a].append(b)
    abj[b].append(a)

visited = [False] * (N+1)
visited[1] = True # 본인

ans = 0
friends = []
# 친구
for friend in abj[1]:
    ans += 1
    visited[friend] = True
    friends.append(friend)

# 친구의 친구
for friend in friends:
    for friendsfriend in abj[friend]:
        if visited[friendsfriend] == False:
            ans += 1
            visited[friendsfriend]=True

print(ans)
