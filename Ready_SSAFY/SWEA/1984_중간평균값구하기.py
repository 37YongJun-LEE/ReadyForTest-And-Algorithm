T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    data.sort()

    min_num = data.pop(0)
    max_num = data.pop()
    while data[0] == min_num:
        data.pop(0)
    while data[-1] == max_num:
        data.pop()
    print('#{} {}'.format(test_case, round(sum(data)/len(data)) ) )

