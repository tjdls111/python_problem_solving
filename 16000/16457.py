import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

# 조합!! (순서 중요 x)

n, m, k = MIIS()
quests = list(tuple(MIIS()) for _ in range(m))

ans = 0


def test(): # 몇 개 퀘스트 달성 가능한지
    cnt = 0
    for quest in quests: # 각 퀘스트 깰 수 있는지
        for q in quest:
            if skill_check[q] == False:
                break
        else:
            cnt += 1
    return cnt


def dfs(depth: int, before_skill_idx: int):  # n개 중 몇개 키 셋팅 했는지, (조합 만들려고) 이전에 몇 번 스킬 사용했는지
    global ans

    if depth == n:  # 키 셋팅 끝났으면
        tmp = test()  # 그 키 셋팅으로 일간 퀘스트 몇 개 달성 가능한지
        ans = max(ans, tmp)  # 더 큰 걸로 업데이트
        return

    for i in range(before_skill_idx + 1, 2*n + 1):  # 키 셋팅 어떻게 할지(몇 번 스킬을 배치할지)
        skill_check[i] = True
        dfs(depth + 1, i)
        skill_check[i] = False


skill_check = [False] * (2 * n + 1)  # 이 스킬 배치했나
dfs(0, 0)
print(ans)
