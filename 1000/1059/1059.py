# n과 같은 수가 있다면 0 출력
# n보다 작은 수 중 가장 큰 수, n보다 큰 수 중 가장 작은 수

L = int(input())
arr = list(map(int, input().split()))
n = int(input())

flag = True
for i in range(L):
    if arr[i] == n:  # n과 같은 수가 arr에 있다면
        flag = False
        break

arr.append(n)
arr.sort()

n_idx = arr.index(n)
left_idx = n_idx-1 # n보다 작은 수 중 가장 큰 수 인덱스
right_idx = n_idx+1  # n보다 큰 수 중 가장 작은 수 인덱스
right_value = arr[right_idx]
left_value = arr[left_idx]

if left_idx == -1:
    left_value = 0

if L == 1:  # L이 1개일 때
    left_value = 0

# print(left_value, n, right_value)

# ans = (n - left_value - 1) * (right_value - n) + (right_value - 1 - n)
ans = (right_value - n)*(n-left_value)-1

if flag == False:
    print(0)
else:
    print(ans)
