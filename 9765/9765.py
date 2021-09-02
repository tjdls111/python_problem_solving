# x들은 소수!!이다.
# 유클리드 호제법
# x2는 C1, C5의 최대공약수이다. x6은 c3, c6의 최대공약수이다.

def uk(a, b):  # 유클리드 호제법
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    else:
        return uk(b, a % b)


c1, c2, c3, c4, c5, c6 = map(int, input().split())

x2 = uk(c1, c5)
x1 = c1 // x2

x6 = uk(c3, c6)
x5 = c6 // x6

x3 = c5 // x2
x7 = c3 // x6

print(x1, x2, x3, x5, x6, x7)
