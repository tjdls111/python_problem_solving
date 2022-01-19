import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

testimonies = []

for _ in range(9):
    a, b = MIIS()
    testimonies.append((a, b))

candidates = []
for liar in range(9):  # 그 사람이 거짓말한다고 가정하고 볼 것
    baseman_arr = [100] + [-1] * 9  # 각 사람들이 1루수인지?
    liar_speak = [-1, -1]

    for i in range(9):

        is_baseman, baseman_num = testimonies[i]
        if i == liar:  # 거짓말 쟁이로 가정한 사람 이야기대로 말한 사람이 있으면 모순
            if baseman_arr[baseman_num] == is_baseman:
                break
            baseman_arr[baseman_num] = (1 + is_baseman) % 2  # 거짓말의 반대

            liar_speak = [is_baseman, baseman_num]
            continue

        # 만약 거짓말쟁이의 이야기와 똑같이 이야기하는 사람 있으면 모순
        if liar_speak != -1 and liar_speak[0] == is_baseman and liar_speak[1] == baseman_num:
            break

        if is_baseman == 0 and baseman_arr[baseman_num] != 1:  # 아니라고 증언했고, 맞다는 증언이 없으면
            baseman_arr[baseman_num] = 0  # 아니라고 표시

        elif is_baseman == 0 and baseman_arr[baseman_num] == 1:  # 아니라고 증언했는데, 맞다는 증언이 있으면
            break  # 모순!

        elif is_baseman == 1 and baseman_arr[baseman_num] == 0:  # 맞다고 증언했는데, 아니라는 증언이 있으면
            break  # 모순!

        elif is_baseman == 1 and baseman_arr[baseman_num] != 0:  # 맞다고 증언했는데, 아니라는 증언이 없으면
            baseman_arr[baseman_num] = 1  # 맞다고 표시

    else:  # break 안 나왔으면 baseman_arr를 쭉 보기!
        if baseman_arr.count(1) == 0:  # 모순이 없고, 아니라는 표시가 없으면 그 아이들 다 될 수 있음.
            for j in range(1, 10):
                # 그런데 거짓말쟁이 말대로는 안됨.
                if j == liar_speak[1] and liar_speak[0] == 1:
                    continue
                if baseman_arr[j] == -1:
                    candidates.append(j)

        elif baseman_arr.count(1) == 1:  # 1루수라는 표시가 1개이면
            candidates.append(baseman_arr.index(1))

if len(set(candidates)) == 1:
    print(candidates[0])
else:  # 답 구할 수 없는 경우
    print(-1)
