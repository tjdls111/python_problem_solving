import sys

input = sys.stdin.readline

table1 = [0] * 16
table2 = [0] * 16

a = input().strip()
b = input().strip()

# 처음 세팅(번호 번갈아서 적기)
for i in range(16):
    if i%2 ==0:
        table1[i] = a[i//2]
    else:
        table1[i] = b[i//2]

for i in range(16):
    # 홀
    if i % 2:

        for j in range(16-i-1):
            table1[j] = (int(table2[j])+int(table2[j+1]))%10
    # 짝
    else:
        for j in range(16-i-1):
            table2[j] = (int(table1[j])+int(table1[j+1]))%10

print(str(table1[0]*10+table1[1]).zfill(2))