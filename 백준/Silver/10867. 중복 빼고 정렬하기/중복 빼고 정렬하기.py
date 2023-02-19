_ = int(input())
arr = list(map(int,input().split()))
not_duplicate_arr = list(set(arr))
sorted_arr = sorted(not_duplicate_arr)
for str in sorted_arr:
    print(str, end=' ')