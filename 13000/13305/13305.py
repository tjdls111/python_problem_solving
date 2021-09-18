# 어떤 도시까지 가기 위해서는 그곳의 왼쪽 도시들 중 가격이 가장 낮은 곳에서 거기로 가기 위한 기름을 충전하면 된다. 

N = int(input())
roads = list(map(int,input().split())) 
gas_station= list(map(int,input().split())) 

cost = 0
most_cheap = 1000000001

for i in range(N - 1): # 왼 -> 오른쪽 도시 순서로 본다
    most_cheap = min(most_cheap, gas_station[i]) # 그때까지 가장 싼 주유소에서 기름 충전한다고 생각
    cost += most_cheap * roads[i] # 다음 지역까지 가기 위한 기름 넣는 비용
print(cost)
