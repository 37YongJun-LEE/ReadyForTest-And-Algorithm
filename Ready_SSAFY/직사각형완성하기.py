T = int(input())
for test_case in range(1, T+1):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    x_dic = {}
    y_dic = {}
    for i in x1, x2, x3:
        try:
            x_dic[i] += 1
        except:
            x_dic[i] = 1
    for j in y1, y2, y3:
        try:
            y_dic[j] += 1
        except:
            y_dic[j] = 1

    for x, y in zip(x_dic, y_dic):

        if x_dic[x] == 1:
            x4 = x
        if y_dic[y] == 1:
            y4 = y
    print('#{} {} {}'.format(test_case, x4, y4))



