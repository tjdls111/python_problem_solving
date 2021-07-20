N = int(input())
tiles = [0]*81
tiles[1] = 1
tiles[2] = 1

def fibo(n):
    if tiles[n]!=0:
        return tiles[n]
    
    tiles[n] = fibo(n-1)+fibo(n-2)
    return tiles[n]
    
print(fibo(N)*4 + fibo(N-1)*2)
