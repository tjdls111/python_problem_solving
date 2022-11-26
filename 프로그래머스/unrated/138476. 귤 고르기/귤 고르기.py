from collections import defaultdict

def solution(k, tangerines):
    tangerineCntPerSize = defaultdict(int)
    for tangerine in tangerines:
        tangerineCntPerSize[tangerine] += 1
    
    tangerineCntList = list(tangerineCntPerSize.values())
    tangerlineCntListSortBySize = sorted(tangerineCntList,reverse=True)
    
    answer = 0
    cnt = 0
    
    for tangerlineCnt in tangerlineCntListSortBySize:
        answer += 1
        cnt += tangerlineCnt
        if cnt >= k:
            break
            
    
    return answer