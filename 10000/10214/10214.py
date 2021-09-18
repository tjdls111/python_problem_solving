T=int(input())
for _ in range(T):
    Y_cnt, K_cnt = 0, 0
    for i in range(9):
        Y,K=map(int,input().split())
        Y_cnt += Y
        K_cnt += K
    if Y_cnt>K_cnt:
        print("Yonsei")
    elif Y_cnt<K_cnt:
        print("Korea")
    else:
        print("Draw")
