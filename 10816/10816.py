N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))

number_cards = {}
for n in N_list:
    number_cards[n] = 0

for n in N_list:
    number_cards[n] +=1

for m in M_list:
    try:
        print(number_cards[m],end=' ')
    except:
        print(0,end=' ')
