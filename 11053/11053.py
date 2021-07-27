N = int(input())
arr = list(map(int,input().split()))

longest = [] # arr의 그 인덱스의 값이 가장 큰 값이라고 가정하고.
longest.append(1)
res = 0

for i in range(1, len(arr)): # 쭉~ 돌면서
    among_longest = 0 
    for j in range(i): # i보다 작은 인덱스들의 값 보면서 
        if arr[j] < arr[i] and among_longest < longest[j]:  
            among_longest = longest[j]
    
    longest.append(among_longest+1)

print(max(longest))