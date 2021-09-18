def d(n): #n과 n의 각 자리수를 더하는 함수
    ans = n
    while n:
        ans+= (n%10)
        n //= 10 
    return ans

self_number_chk = [False]*10001
self_numbers=[]

for i in range(1, 10001):
    if self_number_chk[i] == False:
        self_numbers.append(i)
        new_num = d(i)
        while new_num <= 10000:
            self_number_chk[new_num] = True
            new_num = d(new_num)

for num in self_numbers:
    print(num)


    
