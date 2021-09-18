import sys

M = int(sys.stdin.readline())
S = 0b0 #이진수(비트) 연산하기 위해서 0b. 

for _ in range(M):
    order = sys.stdin.readline().strip()

    try: 
        command, num = order.split()
        num = int(num)
        if command == 'add': 
            S = S | (1<<num) # 1 비트를 num 만큼 왼쪽으로 이동시킴 = num번 비트만 1로, 나머지는 0으로. => S와 | (OR) 연산. (둘 중 하나가 1이면 1 ) -> 나머지는 그대로, num번 비트는 1이든 아니든 꼭 1이됨. 

        elif command == 'remove':
            S = S & ~(1<<num) # ~(1<<num) 를 하면, num번 비트만 0이고 나머지는 1이다. 이걸 S와 & (And) 연산 (&는 둘 다 1 이어야 1. 아니면 0) => num번 비트는 0이 되고,나머지는 그대로.
            
        elif command == 'check':
            if (S & (1<<num)): # num번 비트만 1로, 나머지 0으로 -> S와 &(And) 연산 => S에서도 num번 비트가 1이면 1, 아니면 9.
                print(1)
            else:
                print(0)
                 
        elif command == 'toggle':
            S = S ^ (1<<num) #   (1<<num) 해서 num번 비트만 1로. 이것과 S를 ^연산. 이는 XOR 연산. 둘이 다르면 1, 같으면 0. num번 비트만 1인 것과 S를 비교하므로, S가 1이면 0이 되고, 0이면 1이 된다. 
    
    except:
        if order == 'all':
            S = 0b111111111111111111111

        elif order == 'empty':
            S = 0b0

        

          