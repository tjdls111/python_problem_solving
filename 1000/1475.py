import sys

input = sys.stdin.readline


N = input().strip()
nums =[0]*10

for n in N:
    nums[int(n)] += 1

# 6, 9 대체 가능
if (nums[9] + nums[6]) % 2 ==0:
    nums[6] = (nums[9] + nums[6]) // 2
    nums[9] = nums[6]

else:
    nums[6] = (nums[9] + nums[6]) // 2
    nums[9] = nums[6] + 1

print(max(nums))