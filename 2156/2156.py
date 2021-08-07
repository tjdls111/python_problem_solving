n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))
wines.insert(0,0)
drunk_wine = list([0]*(n+1) for _ in range(3))
# print(drunk_wine)

for i in range(1, n+1):
    drunk_wine[0][i] = max(drunk_wine[0][i-1], drunk_wine[1][i-1], drunk_wine[2][i-1])
    drunk_wine[1][i] = drunk_wine[0][i-1] + wines[i]
    drunk_wine[2][i] = drunk_wine[1][i-1] + wines[i]

print(max(drunk_wine[0][n], drunk_wine[1][n], drunk_wine[2][n])) 



