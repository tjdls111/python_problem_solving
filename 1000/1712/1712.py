import math
A,B,C=map(int, input().split())
a=0 #노트북 갯수
if B>=C: #한대 만드는 데 드는 비용이 가격보다 싸거나 같으면, 손익분기점 넘을 수 X
    print("-1")
else:
    n = math.ceil(A /(C-B))
    if n == A/(C-B):
        n += 1
    print(n)