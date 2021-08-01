import math
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())

# n번째 X는 길이가 2의 n승이다.
# n이 0이거나 짝수일 때는, 절반을 나누면 같고(팰린드롬?!)
# n이 홀수일 때는, 절반을 나누어서 보면 각각 반대이다.

def sol(n, k, cnt): # n: 같거나 작은, 가장 가까운 2의 제곱이 몇 승인지, k: k번째 숫자의 값을 보자, cnt: 몇 번 조작?했는지
    if k == 1:
        return 0, cnt
    elif k == 2:
        return 1, cnt

    # 그 이전 x에서 보는 것(k를 절반?으로 줄임)
    elif  0 <= 2**(n-1) -k :
        return sol(n - 1, k, cnt)

    elif k > 2**(n-1):
        return sol(n - 1, k - 2**(n-1), cnt+1)
    



n =  math.ceil(math.log(k, 2)) # n: 같거나 큰, 가장 가까운 2의 제곱이 몇 승인지
# print(n)
num, cnt = sol(n, k, 0)
# print(num, cnt)

if cnt % 2 == 0: # 조작?한 횟수가 짝수이면 그대로
    print(num)
else: # 홀수이면 1 <-> 0 바뀌기
    if num == 1:
        print(0)
    else:
        print(1)