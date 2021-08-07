n = int(input())

old = [0]
old.extend([1]*9)
new = list(old)


for i in range(n-1):
    new[0] = old[1] # 길이가 i일 때 0이 몇개 들어가는지는, i-1일 때 1이 몇개 들어가는지와 같다.

    for j in range(1, 9): # 1~8이 몇개 들어가는지는, i-1일 때 각각보다 1 작은 수, 1 큰 수가 몇개 들어갔는지 합과 같다.
        new[j] = old[j-1] + old[j+1]
    
    new[9] = old[8] # 9가 몇개 들어가는지는, i-1일 때 8이 몇개 들어갔는지와 같다.

    old = list(new)

print(sum(new)%1000000000)