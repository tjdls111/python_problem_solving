import sys
from collections import defaultdict

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N = int(input())
club_members = [tuple(MIIS()) for _ in range(N)]
club_members.sort(key=lambda x: x[1])  # 좌표 순서대로 서게 하기

if N == 2: # 두 명일 때는 따로 처리(숫자가 1 -> 0 이든 -1 -> 0 이든 이렇게 되니까..)
    if club_members[0][0] != club_members[1][0]: # 둘이 성별 다르면
        print(club_members[1][1] - club_members[0][1])

else:
    club_members_sum = defaultdict(list)

    idx = 0
    total_sum = 0
    total_sums = set()

    while idx < N:
        if club_members[idx][0] == 0:  # 남자이면
            total_sum -= 1
        else:  # 여자이면
            total_sum += 1

        total_sums.add(total_sum)

        club_members_sum[total_sum].append(idx)  # key : 누적합. value: 리스트로 거기 해당하는 인덱스를 저장.
        idx += 1

    ans = 0
    for i in total_sums:  # 누적합 하나씩 보면서
        if len(club_members_sum[i]) > 1:  # 그 누적합이었던 인덱스가 두 개 이상이라면!
            ans = max(ans, club_members[club_members_sum[i][-1]][1] - club_members[club_members_sum[i][0]+1][
                1])  # 맨 마지막에 그 인덱스 나왔을 때 좌표 - (맨 처음 +1)일 때 좌표

    print(ans)
