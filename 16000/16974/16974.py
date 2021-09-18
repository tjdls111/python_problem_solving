n, x = map(int,input().split())


# 레벨-L 버거에서 각각 전체 재료, 패티 몇개씩인지 
all = [0] * (n+1)
all[0] = 1
all[1] = 5
patties =[0]*(n+1)
patties[0] = 1
patties[1] = 3

def n_bugger(n):

    if patties[n]:
        return all[n], patties[n]
    
    else:
        all[n] = n_bugger(n-1)[0]*2 + 3
        patties[n] = n_bugger(n-1)[1]*2 + 1
        
        return all[n], patties[n]


n_bugger(n)

# print(all)
# print('--------')
# print(patties)

# 아래부터 X장 먹었을 때 패티를 몇 장 먹었는지

def ate_patties(n, x):
    if n == 0: # 레벨-0 버거
        if x == 1: # 패티만으로 이뤄짐
            return 1
        elif x == 0:
            return 0
    

    if x == 1: # 항상 햄버거 번만 먹은 것이니까
        # print(n, x, '번만')
        return 0

    elif x <= all[n-1] + 1: # 절반보다 적게 먹었으면
        # print(n, x, '절반보다 적음')
        return ate_patties(n - 1, x - 1)

    elif x == all[n-1] + 2: # 절반 먹었으면
        # print(n, x, '절반')
        return patties[n-1] + 1 # 절반에는 반드시 패티가 있으니까

    elif x <= all[n] - n: # 절반보다 많이 먹었으면
        # print(n, x, '절반보다 많이')
        return patties[n-1] + 1 + ate_patties(n - 1, x - all[n-1] - 2) # 이전 햄버거, 몇 장 먹었는지 남은 것 (맨 끝에 번, 가운데 패티니까 2를 더 뺌)
    
            
    else: # 패티 전체를 먹은 것이니까(all[n] - n 보다 크면 번만 있음)
        # print(n, x, '다!')
        return patties[n]



print(ate_patties(n, x))

# print(patties[50])