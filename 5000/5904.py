N = int(input())


def moo(n):
    if n == 0:
        m_list[n] = 3
        return 3
    m_list[n] = moo(n - 1) * 2 + n + 3
    return m_list[n]

m_list = [0] * 31

def sol(n, idx):
    if idx == -1:
        if n == 1:
            return 'm'
        return 'o'
    tmp = m_list[idx]

    if n <= tmp:
        return sol(n, idx - 1)
    elif n <= tmp + idx + 4:
        if n == tmp + 1:
            return 'm'
        return 'o'
    else:
        return sol(n-(idx+4) - tmp, idx- 1)

if N == 1:
    print('m')
else:
    moo(30)
    idx = 0
    for i in range(30):
        tmp = m_list[i]
        if N > tmp:
            idx = i
        else:
            break

    ans = sol(N, idx)
    print(ans)

'''
39 -> m
9999 -> m
'''