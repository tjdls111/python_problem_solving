fibo = [[0] * 3 for _ in range(41)]
fibo[0] = [0, 1, 0]  # 값, 0 호출, 1 호출
fibo[1] = [1, 0, 1]
fibo[2] = [1, 1, 1]


def fib(n):
    if fibo[n][0]:
        return fibo[n]
    fibo[n][0] = fib(n - 1)[0] + fib(n - 2)[0]
    fibo[n][1] = fib(n - 1)[1] + fib(n - 2)[1]
    fibo[n][2] = fib(n - 1)[2] + fib(n - 2)[2]

    return fibo[n]


fib(40)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(fibo[N][1], fibo[N][2])
