T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    idx_table = [0] * (M+1) # 해당 숫자 개수 리스트
    order = []  # 순서 알림 리스트
    for i in data: # 중복된 숫자 개수 세기
        if idx_table[i] == 0:
            order.append(i) #  순서 넣기
        idx_table[i] += 1
    max_cnt = max(idx_table)
    print('#{}'.format(test_case), end = ' ')
    for i in range(max_cnt, -1, -1): # 최대 숫자랑 같다면
        for number in order:
            if i == idx_table[number]:
                for _ in range(i): print(number, end = ' ')
    print()

"""
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    idx_table = [0] * (M+1) # 해당 숫자 개수 리스트
    order = []  # 순서 알림 리스트

    for i in data: # 중복된 숫자 개수 세기
        if idx_table[i] == 0:
            order.append(i) #  순서 넣기
        idx_table[i] += 1

    #print(order)
    #print(idx_table, max(idx_table))
    max_cnt = max(idx_table)

    for i in range(max_cnt, -1, -1): # 최대 숫자랑 같다면
        for number in order:
            if i == idx_table[number]:
                for _ in range(i): print(number, end = ' ')
    print()

    # 정답 출력하기

"""