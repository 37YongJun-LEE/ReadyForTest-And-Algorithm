blind = {'A': '', 'N': '', 'D': '', 'R': '', 'E': '', 'W': ''}
T = int(input())
for test_case in range(1, T + 1):
    data = list(input())
    for i in range(len(data)):
        try:
            data[i] = blind[data[i]]
        except:
            continue
    print('#{} {}'.format(test_case, ''.join(data)))
    # 생각을 좀더 해보면 굳이 끝에서 전부 출력할 필요 없고, 각 경우에서 맞다 아니다로 판별해 하나씩 출력해주면 더 빠를듯
