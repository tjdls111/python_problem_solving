from collections import deque
n, m  = map(int,input().split())
cards = list(map(int,input().split()))


# 작은 수 두 개를 가지고 m번 활동하기
for _ in range(m):
    cards.sort()
    a = cards[0]
    b = cards[1]
    cards[0] = a + b
    cards[1] = cards[0]
   
print(sum(cards))    