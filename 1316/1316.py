N=int(input())
arr= list(input() for _ in range(N))
ans = 0

for i in range(N):
    check = [0]*26
    word = arr[i]

    for j in range(len(word)-1):
        chr = word[j]
        if chr == word[j+1]:
            continue
        chr_n = ord(word[j]) - 97
        if check[chr_n] == 1:
            break
        else:
            check[chr_n] = 1
    else:
        # 마지막 거 체크
        if check[ord(word[-1])-97] == 0:
            ans += 1
    
print(ans)
