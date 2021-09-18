n, k, b = map(int,input().split())
min_fix = float('inf')

road = [True]*(n+1)

for _ in range(b):
    road[int(input())] = False
#print(road)

s = 1
e = 0 # 이걸 0으로 해야 맞을 것 같은데,, 1로 해야 맞고 0으로 하면 틀리네 
fix = 0

# 일단 1~k 사이에 고장난 신호등을 수리하는 경우(그러면 k개니까..)
while e < k:
    e += 1
    if road[e] == False:
        fix += 1

while e < n: 
    min_fix = min(min_fix, fix)
    e += 1 # 다음부터는 s, e를 하나씩 이동해가면서
    s += 1
    if road[e] == False: # 다음 것이 고장난 신호등이면 fix 더하고
        fix += 1
    if road[s] == False: # 전에 것이 고장난 신호등이면 fix 빼고
        fix -= 1

print(min_fix)