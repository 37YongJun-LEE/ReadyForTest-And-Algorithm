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