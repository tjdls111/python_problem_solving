N = int(input())
arr = list(map(int, input().split()))

junghun_origin_sum = 0
for i in range(N):
    if i % 2 == 0:
        junghun_origin_sum += arr[i]
ans = junghun_origin_sum
junghun_sum = junghun_origin_sum

# 밑장 빼기를 하면, 그 순간부터
# 원래 정훈이가 가질 예정이었던 카드들과 상대가 가질 예정이었던 카드들이 바뀌는 것

# (정훈이 차례에서) 맨 아래에서부터 밑장 빼기 했을 때 합 어떤지
for i in range(N-1, 0, -2):
    junghun_sum += arr[i]
    junghun_sum -= arr[i-1]
    ans = max(ans, junghun_sum)


junghun_sum = junghun_origin_sum
# 상대 차례에서
for i in range(N-2, 1, -2):
    junghun_sum -= arr[i]
    junghun_sum += arr[i-1]
    ans = max(ans, junghun_sum)

print(ans)
