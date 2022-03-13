import sys

input = sys.stdin.readline

N, r, c = map(int,input().split())

ans = 0

def sol(i, j, n):
    global ans
    nn = n//2

    if n==1:
        return

    ni, nj = i // nn, j // nn

    if ni == 0 and nj == 0:
        ans += 0
        sol(i, j, nn)

    elif ni == 0 and nj == 1:
        ans += n*n//4
        sol(i, j-nn, nn)

    elif ni == 1 and nj == 0:
        ans += (n*n//4*2)
        sol(i-nn, j, nn)

    elif ni == 1 and nj == 1:
        ans += (n*n//4*3)
        sol(i-nn, j-nn, nn)

sol(r,c, 2**N)
print(ans)