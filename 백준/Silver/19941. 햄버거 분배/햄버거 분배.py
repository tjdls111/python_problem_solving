import sys

n, k = map(int,sys.stdin.readline().strip().split())
s = sys.stdin.readline().strip()

personIndexList = []
hamburgerEatCheck = [False]*n

for i in range(len(s)):
    item = s[i]
    if item == 'H':
        hamburgerEatCheck[i] = False
    else:
        hamburgerEatCheck[i] = True
        personIndexList.append(i)

answer = 0

for personIndex in personIndexList:
    flag = False
    for i in range(k, 0,-1):
        if personIndex-i >= 0 and hamburgerEatCheck[personIndex-i] == False:
            answer += 1
            hamburgerEatCheck[personIndex-i] = True
            flag = True
            break
    if not flag:
        for i in range(k+1):
            if personIndex + i < n and hamburgerEatCheck[personIndex + i] == False:
                answer += 1
                hamburgerEatCheck[personIndex + i] = True
                break

print(answer)