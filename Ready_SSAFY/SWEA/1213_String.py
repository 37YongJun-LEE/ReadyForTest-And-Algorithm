T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc = int(input())

    wanted = input()

    where = input()

    where = where.replace(wanted, ' ')

    cnt = 0
    for i in where:
        if i == ' ':
            cnt += 1

    print('#' + str(tc) , cnt)
