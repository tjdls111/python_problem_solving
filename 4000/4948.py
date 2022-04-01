# 먼저 소수 구하기
sosu = [False] * 246914
i = 2
while i < 246914:
    if sosu[i] == False:
        for j in range(i * 2, 246914, i):
            sosu[j] = True
    i += 1

while True:
    n = int(input())
    if n == 0: exit()

    # 이 부분을
    ans = 0
    for k in range(n + 1, n * 2 + 1):
        if sosu[k] == False:
            ans += 1
    print(ans)

    # 아래 한 줄로 가능
    # print(sum([1 for k in range(n + 1, n * 2 + 1) if sosu[k] == False]))
