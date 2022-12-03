from collections import defaultdict


def solution(topping):
    chelsuPart = defaultdict(int)
    brotherPart = defaultdict(int)

    chelsuPartTopping = set()
    brotherPartTopping = set()

    # 조각을 자르지 않았다고 가정/ 모든 토핑을 동생이 가져간다면
    for toppingType in topping:
        brotherPart[toppingType] += 1
        brotherPartTopping.add(toppingType)

    answer = 0
    # 조각 자르는 기준을 한 칸씩 옆으로 이동
    for toppingType in topping:
        chelsuPart[toppingType] += 1
        brotherPart[toppingType] -= 1

        chelsuPartTopping.add(toppingType)

        if brotherPart[toppingType] == 0:
            brotherPartTopping.remove(toppingType)

        if len(brotherPartTopping) == len(chelsuPartTopping):
            answer += 1

    return answer