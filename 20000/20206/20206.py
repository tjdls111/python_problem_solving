A, B, C = map(int,input().split())
x_1, x_2, y_1, y_2 = map(int,input().split())

def equation(t):   # 방정식 결과
    x, y = t
    return A * x + B * y + C

vertexs = [(x_1, y_1), (x_2, y_2), (x_1, y_2), (x_2, y_1)] # 네 변 꼭지점

l = []
for vertex in vertexs:   # 네 변 꼭지점을 방정식에 넣은 결과를 l에 넣기
    l.append(equation(vertex))

l.sort()  # l을 정렬
if l[0] < 0 and l[-1] > 0: # l 에서 가장 작은 값이 음수이고, l에서 가장 큰 값이 양수라면 그럼 직사각형의 점 들 중에서 방정식 결과가 0이 나온다는 것이니까
    print("Poor")
else:
    print("Lucky")